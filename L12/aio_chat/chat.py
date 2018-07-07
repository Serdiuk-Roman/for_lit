#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
import aiohttp_jinja2


class Message():
    def __init__(self, db, **kwargs):
        self.collection = db[MESSAGE_COLLECTION]


    async def save(self, user, msg, **kw):
        result = await self.collection.insert(
            {'user': user, 'msg': msg, 'time': datetime.now()}
        )
        return result

    async def get_messages(self):
        messages = self.collection.find().sort([('time', 1)])
        return await messages.to_list(length=None)


class ChatList(web.View):
    @aiohttp_jinja2.template('chat/index.html')
    async def get(self):
        message = Message(self.request.db)
        messages = await message.get_messages()
        return {'messages': messages}


class WebSocket(web.View):
    pass
