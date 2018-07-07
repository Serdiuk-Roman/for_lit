import logging
import json
import ast
import aiohttp
from datetime import datetime
import aiohttp_jinja2
from aiohttp import web
from chat.core.models.message_model import Message
log = logging.getLogger(__name__)


async def index(request):
    message = Message()
    ws_current = web.WebSocketResponse()
    ws_ready = ws_current.can_prepare(request)
    if not ws_ready.ok:
        return aiohttp_jinja2.render_template('chat/index.html', request, {})

    await ws_current.prepare(request)
    msg = await ws_current.receive()
    name = ast.literal_eval(msg.data)['user_name']



    log.info('%s joined.', name)
    if len(msg.data) > 0:
        await ws_current.send_json({'action': 'connect', 'name': name})

    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'join', 'name': name})
    request.app['websockets'][name] = ws_current

    messages = await message.get_all()
    for msg in messages:
        await ws_current.send_json({'action': 'sent', 'name': msg['name'], 'text': msg['text'], 'time': msg['time']})

    while True:
        msg = await ws_current.receive()

        if msg.type == aiohttp.WSMsgType.text:
            for ws in request.app['websockets'].values():
                if ws is not ws_current:
                    s = datetime.now().second
                    m = datetime.now().minute
                    h = datetime.now().hour
                    await message.message_create(name, msg.data, "{}:{}:{}".format(h,m,s))
                    await ws.send_json({'action': 'sent', 'name': name, 'text': msg.data, 'time': "{}:{}:{}".format(h,m,s)})
        else:
            break

    del request.app['websockets'][name]
    log.info('%s disconnected.', name)
    for ws in request.app['websockets'].values():
        await ws.send_json({'action': 'disconnect', 'name': name})

    return ws_current
