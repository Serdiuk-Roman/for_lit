#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
from datetime import datetime

import redis
from flask import Flask, request, render_template, redirect  # , jsonify

tasks = []

app = Flask(__name__)

redis_db = redis.Redis('localhost', 6379)


def base62_encode(number):
    assert number >= 0, 'positive integer required'
    if number == 0:
        return '0'
    base62 = []
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while number != 0:
        number, i = divmod(number, 62)
        base62.append(chars[i])
    return ''.join(reversed(base62))


def insert_comment(values, board_id):
    comments = redis_db.get('comments:board:' + board_id)
    if comments is None:
        json_values = json.dumps([values])
        redis_db.set('comments:board:' + board_id, json_values)
        return
    unpacked_comments = json.loads(comments.decode('utf-8'))
    unpacked_comments.append(values)
    insert_value = json.dumps(unpacked_comments)
    redis_db.set('comments:board:' + board_id, insert_value)


@app.route('/')
def boards():
    boards = []

    keys = redis_db.keys('board:*')
    keys = [
        key.decode('utf-8')
        for key in keys
    ]
    keys.sort()

    boards = redis_db.mget(keys)
    boards = [
        board.decode('utf-8')
        for board in boards
    ]

    return render_template(
        'boards.html',
        keys=keys,
        boards=boards
    )


@app.route('/add_board', methods=['GET'])
def form_add_board():
    values = []
    return render_template('add_board.html', values=values)


@app.route('/add_board', methods=['POST'])
def add_board():

    creator = request.form.get('creator')
    board_name = request.form.get('board_name')
    dt = str(datetime.now()).split('.')[0]

    board_num = redis_db.incr('last-board-id')
    board_id = base62_encode(board_num)

    redis_db.set('board:' + board_id, board_name)
    redis_db.set('creator:board:' + board_id, creator)
    redis_db.set('datetime:board:' + board_id, dt)

    return redirect('/view_board/{}'.format(board_id))


@app.route('/view_board/<board_id>')
def view_board(board_id):

    try:
        board = redis_db.get('board:' + board_id).decode('utf-8')
    except AttributeError:
        return render_template('404.html')
    creator = redis_db.get('creator:board:' + board_id).decode('utf-8')
    dt = redis_db.get('datetime:board:' + board_id).decode('utf-8')
    values = [board, creator, dt, board_id]

    try:
        comments = redis_db.get('comments:board:' + board_id)
        unpacked_comments = json.loads(comments.decode('utf-8'))
    except AttributeError:
        unpacked_comments = []

    return render_template(
        'board_detail.html',
        values=values,
        comments=unpacked_comments
    )


@app.route('/add_comment/for_<board_id>', methods=['GET'])
def form_add_comment(board_id):
    values = []
    return render_template(
        'add_comment.html',
        values=values,
        board_id=board_id
    )


@app.route('/add_comment/for_<board_id>', methods=['POST'])
def add_comment(board_id):
    comment_creator = request.form.get('comment_creator')
    comment = request.form.get('comment')
    values = [comment, comment_creator]
    insert_comment(values, board_id)
    return redirect('/view_board/{}'.format(board_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login'
    else:
        values = []
        return render_template(
            'signup.html',
            values=values
        )


if __name__ == '__main__':
    app.debug = True
    app.run()
