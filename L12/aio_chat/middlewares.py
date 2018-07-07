#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aiohttp import web
from aiohttp.web import middleware
from aiohttp_session import get_session
# from settings import *


@middleware
async def authorize(request, handler):
    def check_path(path):
        result = True
        for r in ['/login', '/static/', '/signin',
                  '/signout', '/_debugtoolbar/']:
            if path.startswith(r):
                result = False
        return result

    session = await get_session(request)
    if session.get("user"):
        return await handler(request)
    elif check_path(request.path):
        url = request.app.router['login'].url()
        raise web.HTTPFound(url)
        return handler(request)
    else:
        return await handler(request)


async def db_handler(app, handler):
    async def middleware(request):
        if (request.path.startswith('/static/') or
                request.path.startswith('/_debugtoolbar')):
            response = await handler(request)
            return response

        request.db = app.db
        response = await handler(request)
        return response
    return middleware
