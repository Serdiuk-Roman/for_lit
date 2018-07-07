#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from chat import ChatList, WebSocket
from auth import Login, SignIn, SignOut

routes = [
    ('GET', '/', ChatList, 'main'),
    ('GET', '/ws', WebSocket, 'chat'),
    ('*', '/login', Login, 'login'),
    ('*', '/signin', SignIn, 'signin'),
    ('*', '/signout', SignOut, 'signout'),
]
