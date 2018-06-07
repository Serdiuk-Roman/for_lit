#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import redis
from datetime import datetime
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader


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
    """docstring for Board"""

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

    def error_404(self):
        response = self.render_template('404.html')
        response.status_code = 404
        return response

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound as e:
            return self.error_404()
        except HTTPException as e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def insert_board(self, values):
        board_num = self.redis.incr('last-board-id')
        board_id = base36_encode(board_num)
        self.redis.set('board:' + board_id, values[0])
        self.redis.set('creator:board:' + board_id, values[1])

        dt = str(datetime.now()).split('.')[0]
        self.redis.set(
            'datetime:board:' + board_id,
            dt
        )
        return board_id
    #     short_id = self.redis.get('reverse-url:' + url)
    #     if short_id is not None:
    #         return short_id
    #     url_num = self.redis.incr('last-url-id')
    #     short_id = base36_encode(url_num)
    #     self.redis.set('url-target:' + short_id, url)
    #     self.redis.set('reverse-url:' + url, short_id)
    #     return short_id

    def insert_comment(self, values, board_id):
        comments = self.redis.get('comments:board:' + board_id)
        if comments is None:
            json_values = json.dumps([values])
            self.redis.set('comments:board:' + board_id, json_values)
            return
        unpacked_comments = json.loads(comments.decode('utf-8'))
        unpacked_comments.append(values)
        insert_value = json.dumps(unpacked_comments)
        self.redis.set('comments:board:' + board_id, insert_value)

    def on_base(self, request):

        error = None
        boards = []
        values = []

        keys = self.redis.keys('board:*')
        keys = [
            key.decode('utf-8')
            for key in keys
        ]
        keys.sort()

        boards = self.redis.mget(keys)
        boards = [
            board.decode('utf-8')
            for board in boards
        ]

        if request.method == 'POST':
            creator = request.form['creator']
            board_name = request.form['board_name']
            values = [board_name, creator]
            if not 0 < len(creator) <= 30:
                error = 'Username max 30'
            elif not 0 < len(board_name) <= 50:
                error = 'Board_name max 50'
            else:
                board_id = self.insert_board(values)
                return redirect('/board:{}'.format(board_id))

        return self.render_template(
            'board.html',
            error=error,
            keys=keys,
            boards=boards,
            values=values
        )

    def on_board_detail(self, request, board_id):

        error = None
        values = []

        try:
            board = self.redis.get('board:' + board_id).decode('utf-8')
        except AttributeError:
            return self.error_404()
        creator = self.redis.get('creator:board:' + board_id).decode('utf-8')
        dt = self.redis.get('datetime:board:' + board_id).decode('utf-8')

        if request.method == 'POST':
            comment_creator = request.form['comment_creator']
            comment = request.form['comment']
            values = [comment, comment_creator]
            if not 0 < len(comment_creator) <= 30:
                error = 'Username max 30'
            elif not 0 < len(comment) <= 255:
                error = 'Comment max 255'
            else:
                self.insert_comment(values, board_id)
                values = []
        try:
            comments = self.redis.get('comments:board:' + board_id)
            unpacked_comments = json.loads(comments.decode('utf-8'))
        except AttributeError:
            unpacked_comments = []

        return self.render_template(
            'board_details.html',
            board=board,
            creator=creator,
            dt=dt,
            error=error,
            values=values,
            comments=unpacked_comments
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
