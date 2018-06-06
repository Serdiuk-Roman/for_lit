# -*- coding: utf-8 -*-
from werkzeug.wrappers import Request, Response


def application(environ, start_response):
    request = Request(environ)
    text = "Hello {}!".format(request.args.get('name', 'World'))
    response = Response(text, mimetype='text/plain')
    return response(environ, start_response)


if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('127.0.0.1', 5000, application)
