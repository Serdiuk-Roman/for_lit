#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from functools import wraps

from flask import Response, request


users = {}
users['zim'] = '123'


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username in users and \
        password == users[username]


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
        'Unauthorized\nCould not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def add_new_user(user, passw):
    global users
    users[user] = passw
