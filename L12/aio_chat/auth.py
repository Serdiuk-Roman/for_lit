#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_session import get_session


class Login(web.View):

    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            url = request.app.router['main'].url()
            raise web.HTTPFound(url)
        return b'Please enter login or email'


class SignIn(web.View):
    pass


class SignOut(web.View):
    pass
