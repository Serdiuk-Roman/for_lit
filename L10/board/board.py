#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import redis
from urllib.parse import urlparse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


def is_valid_url(url):
    parts = urlparse(url)
    return parts.scheme in ('http', 'https')


def is_valid_creator(name):
    return 0 < len(name) < 30


def is_valid_board_text(text):
    return 0 < len(text) < 50


def base36_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base36 = []
    while number != 0:
        number, i = divmod(number, 36)
        base36.append('0123456789abcdefghijklmnopqrstuvwxyz'[i])
    return ''.join(reversed(base36))


class Board():
    """docstring for Shortly"""

    def __init__(self, config):
        self.redis = redis.Redis(config['redis_host'], config['redis_port'])
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
                                     autoescape=True)
        self.url_map = Map([
            Rule('/', endpoint='base'),
            Rule('/board:<board_id>', endpoint='board_detail')
        ])

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    # def insert_board(self, url):
    #     short_id = self.redis.get('reverse-url:' + url)
    #     if short_id is not None:
    #         return short_id
    #     url_num = self.redis.incr('last-url-id')
    #     short_id = base36_encode(url_num)
    #     self.redis.set('url-target:' + short_id, url)
    #     self.redis.set('reverse-url:' + url, short_id)
    #     return short_id

    def on_base(self, request):
        error = ''
        boards = []
        values = []
        if request.method == 'POST':
            creator = request.form['creator']
            board_name = request.form['board_name']
            values = [creator, board_name]
            if not is_valid_creator(creator):
                error += 'Username max 30\n'
            elif not is_valid_board_text(board_name):
                error += 'Board_name max 50\n'
            else:
                # short_id = self.insert_url(url)
                return redirect('/')
        return self.render_template(
            'board.html',
            error=error,
            boards=boards,
            values=values
        )

    def on_follow_short_link(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        self.redis.incr('click-count:' + short_id)
        return redirect(link_target)

    def on_short_link_details(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        click_count = int(self.redis.get('click-count:' + short_id) or 0)
        return self.render_template(
            'short_link_details.html',
            link_target=link_target,
            short_id=short_id,
            click_count=click_count
        )

    


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Board({
        'redis_host': redis_host,
        'redis_port': redis_port
    })
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
