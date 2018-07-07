from chat.core.models.user_model import User
from aiohttp import web
import json

async def handler(request):
    lol = await request.post()
    user = User(lol.get('user'), lol.get('password'))
    if not await user.create_user():
        if not await user.check_password():
            return web.Response(content_type='application/json', text=json.dumps({'error': "Wrong password"}))
    return web.Response(content_type='application/json', text=json.dumps({'user': lol.get('user')}))