import logging

import jinja2
from motor import motor_asyncio as ma
import aiohttp_jinja2
from aiohttp import web
from chat.core.controller.index import index
from chat.core.controller.login import handler
import os


path = os.path.dirname(__file__)

async def init_app():

    app = web.Application()

    app['websockets'] = {}

    app.on_shutdown.append(shutdown)

    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(path + '/templates'))

    app.router.add_get('/', index)
    app.router.add_post('/login', handler)
    app['static_root_url'] = path + '/static'
    app.router.add_static('/static', app['static_root_url'], name='static')

    return app


async def shutdown(app):
    for ws in app['websockets'].values():
        await ws.close()
    app['websockets'].clear()


def main():
    logging.basicConfig(level=logging.DEBUG)

    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
