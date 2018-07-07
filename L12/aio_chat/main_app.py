#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import aioredis
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
from aiohttp_session import session_middleware
from aiohttp_session.redis_storage import RedisStorage
from aiohttp import web, log

from routes import routes
from middlewares import authorize

import hashlib
import handlers
from collections import defaultdict


async def static_processor(request):
    return {'STATIC_URL': '/static/'}


async def auth_processor(request):
    return {'current_user': request.cookies.get('user')}


async def auth_cookie_factory(app, handler):
    async def auth_cookie_handler(request):
        if request.path != '/login' and request.cookies.get('user') is None:
            # redirect
            return web.HTTPFound('/login')
        return await handler(request)
    return auth_cookie_handler


class BList(list):
    def broadcast(self, message):
        for waiter in self:
            try:
                waiter.send_str(message)
            except Exception:
                print('Error was happened during broadcasting')


async def main():

    redis_pool = await aioredis.create_pool(
        'redis://localhost',
        minsize=5,
        maxsize=10,
    )

    middle = [
        session_middleware(RedisStorage(redis_pool)),
        authorize,
    ]

    # if DEBUG:
    #     middle.append(aiohttp_debugtoolbar.middleware)

    app = web.Application(middlewares=middle)

    # if DEBUG:
    #     aiohttp_debugtoolbar.setup(app)

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader('templates')
    )

    # route part
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
    app['static_root_url'] = '/static'
    app.router.add_static('/static', 'static', name='static')
    # end route part

    # db connect
    # app['redis'] = await aioredis.create_redis(
    app.db = await aioredis.create_redis(
        # ('localhost', 6379),
        'redis://localhost',
        encoding='utf-8'
    )
    # app.client = ma.AsyncIOMotorClient(MONGO_HOST)
    # app.db = app.client[MONGO_DB_NAME]
    # end db connect

    app.on_cleanup.append(on_shutdown)
    app['websockets'] = []
    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(main())
    web.run_app(app)
