from aiohttp import web

from settings import config
from routes import setup_routes

# pip install pip install aioredis
# import aioredis
# Чат с использованием aiohttp и redis

async def init_db():
    conf = app['config']['redis']
    



app = web.Application()
setup_routes(app)
app['config'] = config

web.run_app(app)
