#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from handlers import index_handler, ws_handler, \
    LoginView, logout_handler

routes = [
    ('GET', '/', index_handler, 'main'),
    ('GET', '/ws', ws_handler, 'ws_chat'),
    ('*', '/login', LoginView, 'login'),
    ('*', '/logout', logout_handler, 'logout'),
]
