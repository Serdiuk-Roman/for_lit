#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import asyncio
import aioredis
import aiohttp_jinja2
import jinja2
from aiohttp import web
from collections import defaultdict

from routes import routes
import handlers


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

    async def close_redis(app):
        keys = await app.db.keys('chat:users')

        for key in keys:
            await app.db.delete(key)
        app.db.close()

    async def close_websockets(app):

        for channel in app['waiters'].values():
            while channel:
                ws = channel.pop()
                await ws.close(code=1000, message='Server shutdown')

    middlewares = [
        # session_middleware(RedisStorage(redis_pool)),
        auth_cookie_factory
    ]

    app = web.Application(middlewares=middlewares)

    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader('templates'),
        context_processors=[static_processor, auth_processor])

    # route part
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
    app['static_root_url'] = '/static'
    app.router.add_static('/static', 'static', name='static')

    # db connect
    app.db = await aioredis.create_redis(
        ('localhost', 6379),
        encoding='utf-8'
    )

    app['waiters'] = defaultdict(BList)

    app.on_shutdown.append(close_websockets)
    app.on_shutdown.append(close_redis)

    # app.on_cleanup.append(on_shutdown)
    app['websockets'] = []

    return app


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(main())
    web.run_app(app)
