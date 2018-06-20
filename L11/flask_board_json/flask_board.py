#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, request, jsonify, make_response

from auth import requires_auth, add_new_user
from db import get_board, get_advert, get_comments, get_likes, \
    insert_advert, insert_comment, insert_like
from check import check_login, advert_is_valid, comment_is_valid, \
    comments_limit, likes_limit


app = Flask(__name__)


@app.route('/')
def index():
    with open('README.md') as info:
        return str(info.read())


@app.route('/login/', methods=['POST'])
def login():
    if request.method == 'POST':
        post_data = request.get_json()
        check = check_login(post_data)

        if check[0] is False:
            return jsonify(check[1])

        add_new_user(post_data['username'], post_data['password'])

        return jsonify([
            "Congratulations!!!",
            "add in Basic Auth:",
            "Authorization: {username}:{password}"
        ])


@app.route('/api/board/', methods=['GET'])
@requires_auth
def board():
    board = get_board()
    if not board:
        return jsonify("There are no ads")
    return jsonify([
        'dict: {advert_id: advert_text}',
        {'board': board},
        'detail view: /api/advert/<advert_id>',
        'add advert: /api/add_advert/',
    ])


@app.route('/api/add_advert/', methods=['POST'])
@requires_auth
def add_advert():
    creator = request.authorization.username
    try:
        advert_name = request.get_json()['advert_name']
    except Exception as e:
        print(e)
        return jsonify("Should be a field 'advert_name'")

    check = advert_is_valid(creator, advert_name)

    if check[0] is False:
        return jsonify(check[1])

    status = insert_advert(creator, advert_name)
    return jsonify(status)


@app.route('/api/advert/<advert_id>')
@requires_auth
def advert(advert_id):

    advert = get_advert(advert_id)

    likes = get_likes(advert_id)

    comments = get_comments(advert_id)

    return jsonify(
        advert=advert,
        likes=likes,
        comments=comments
    )


@app.route('/api/advert/<advert_id>/add_comment/', methods=['POST'])
@requires_auth
def add_comment(advert_id):
    creator = request.authorization.username

    check = comments_limit(creator)

    if check[0] is False:
        return jsonify(check[1])

    try:
        comment = request.get_json()['comment']
    except Exception as e:
        print(e)
        return jsonify("Should be a field 'comment'")

    check = comment_is_valid(creator, comment)

    if check[0] is False:
        return jsonify(check[1])

    status = insert_comment(creator, comment, advert_id)
    return jsonify([
        status,
        "detail view: /api/advert/{}".format(advert_id)
    ])


@app.route('/api/advert/<advert_id>/add_like/', methods=['GET'])
@requires_auth
def add_like(advert_id):
    creator = request.authorization.username

    check = likes_limit(creator)

    if check[0] is False:
        return jsonify(check[1])

    status = insert_like(creator, advert_id)
    return jsonify([
        status,
        "detail view: /api/advert/{}".format(advert_id)
    ])


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # app.debug = True
    # app.run()
    pass
