#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

from aiohttp import web
import aiohttp_jinja2
import bcrypt


class LoginView(web.View):

    @aiohttp_jinja2.template('login.html')
    async def get(self):
        if self.request.cookies.get('user'):
            return web.HTTPFound('/')
        return {'title': 'Authentication'}

    @aiohttp_jinja2.template('login.html')
    async def post(self):
        response = web.HTTPFound('/')

        data = await self.request.post()
        if len(data) == 2:
            try:
                data['name']
                data['pass']
            except KeyError as e:
                print(e)
                return {'title': 'Authentication',
                        'error': 'Do you use a web browser?'}

        red_db = self.request.app.db

        users = await red_db.zrange('chat:users')
        if data['name'] in users:
            return {'title': 'Authentication',
                    'error': 'Username already in the system'}

        password = bytes(data['pass'], 'utf-8')
        passw = bcrypt.hashpw(password, bcrypt.gensalt())

        db_user_pass = await red_db.get("chat:user:" + data['name'])

        if not db_user_pass:
            await red_db.set("chat:user:" + data['name'], passw)
        elif not bcrypt.checkpw(password, db_user_pass.encode('utf-8')):
            return {'title': 'Authentication',
                    'error': 'password error'}

        response.set_cookie('user', data['name'])
        return response


async def logout_handler(request):
    # симулируем logout
    response = web.HTTPFound('/login')
    response.del_cookie('user')
    return response


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    title = 'main'
    r = request.app.db
    cache = await r.lrange('chat:msg', 0, -1)
    messages = (json.loads(x) for x in cache) if cache else []
    return {'title': title, 'messages': messages}


async def ws_handler(request):

    current_user = request.cookies.get('user')
    channel = 'main'
    chat_users = 'chat:users'
    channel_key = 'chat:msg'

    ws = web.WebSocketResponse(autoclose=False)
    await ws.prepare(request)

    chat_waiters = request.app['waiters'][channel]
    chat_waiters.append(ws)

    r = request.app.db

    try:
        count = int(await r.zcount(chat_users))

        await r.zadd(chat_users, count + 1, current_user)
        users = await r.zrange(chat_users)
        chat_waiters.broadcast(json.dumps({'user_list': users}))

        data = {
            'user': 'ChatBot',
            'body': ">>{}<< joined the chat".format(current_user)}
        data['time'] = datetime.now().strftime('%H:%M:%S %Y-%m-%d')
        data_json = json.dumps(data)
        chat_waiters.broadcast(data_json)

        async for msg in ws:

            if msg.tp == web.MsgType.text:
                data = json.loads(msg.data)
                data['time'] = datetime.now().strftime('%H:%M:%S %Y-%m-%d')
                data_json = json.dumps(data)
                await r.rpush(channel_key, data_json)
                await r.ltrim(channel_key, -50, -1)
                chat_waiters.broadcast(data_json)

            elif msg.tp == web.MsgType.error:
                print("Ahtung!!!!!!!!!")
                print('connection closed with exception {}'
                      .format(ws.exception()))
    finally:
        if ws in chat_waiters:

            data = {
                'user': 'ChatBot',
                'body': ">>{}<< leaving the chat".format(current_user)}
            data['time'] = datetime.now().strftime('%H:%M:%S %Y-%m-%d')
            data_json = json.dumps(data)
            chat_waiters.broadcast(data_json)

            await ws.close()
            chat_waiters.remove(ws)

        await r.zrem(chat_users, current_user)
        users = await r.zrange(chat_users)
        chat_waiters.broadcast(json.dumps({'user_list': users}))

    return ws
