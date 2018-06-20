#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json
from datetime import datetime

import redis

from utils import base62_encode
from auth import users


redis_db = redis.Redis('localhost', 6379)


def get_board():
    keys = []
    adverts = []

    try:
        keys = redis_db.keys('advert:*')
    except AttributeError:
        return False
    keys = [
        key.decode('utf-8')
        for key in keys
    ]
    keys.sort()

    print("keys: ", keys)
    if not keys:
        return False

    try:
        adverts = redis_db.mget(keys)
    except AttributeError:
        return False
    adverts = [
        advert.decode('utf-8')
        for advert in adverts
    ]

    board = {
        keys[i].split(':')[1]: adverts[i]
        for i in range(len(keys))
    }
    return board


def get_advert(advert_id):
    try:
        advert = redis_db.get('advert:' + advert_id).decode('utf-8')
    except AttributeError:
        return "404 Not found"
    creator = redis_db.get('creator:advert:' + advert_id).decode('utf-8')
    dt = redis_db.get('datetime:advert:' + advert_id).decode('utf-8')
    values = {
        "id": advert,
        "creator": creator,
        "advert name": advert,
        "date": dt
    }
    return values


def insert_advert(creator, advert_name):

    advert_num = redis_db.incr('last-advert-id')
    advert_id = base62_encode(advert_num)

    dt = str(datetime.now()).split('.')[0]
    try:
        redis_db.set('advert:' + advert_id, advert_name)
        redis_db.set('creator:advert:' + advert_id, creator)
        redis_db.set('datetime:advert:' + advert_id, dt)
    except Exception:
        return "Error DB"

    res = [
        "new advert has been added with id: {}".format(advert_id),
        "detail view: /api/advert/{}".format(advert_id)
    ]
    return res


def get_comments(advert_id):
    try:
        raw_comments = redis_db.get('comments:advert:' + advert_id)
        comments = json.loads(raw_comments.decode('utf-8'))
    except AttributeError:
        comments = []
    return comments


def insert_comment(creator, comment, advert_id):
    comments = redis_db.get('comments:advert:' + advert_id)

    if comments is None:
        json_values = json.dumps([[creator, comment], ])
        redis_db.set('comments:advert:' + advert_id, json_values)
        return "new coment has been added "

    unpacked_comments = json.loads(comments.decode('utf-8'))
    unpacked_comments.append([creator, comment])

    insert_value = json.dumps(unpacked_comments)
    redis_db.set('comments:advert:' + advert_id, insert_value)

    creator_num_comments = redis_db.get('comments:creator:' + creator)

    if creator_num_comments is None:
        creator_num_comments = 1
        redis_db.setex(
            'comments:creator:' + creator,
            creator_num_comments,
            3600
        )
    else:
        creator_num_comments = creator_num_comments.decode('utf-8')
        redis_db.incr('comments:creator:' + creator)

    res = [
        "new comment has been added",
        "You limit: {} comments from {} sec".format(
            5 - int(creator_num_comments),
            redis_db.ttl('comments:creator:' + creator)
        )
    ]

    return res


def insert_like(creator, advert_id):

    redis_db.incr('likes:advert:' + advert_id)

    creator_num_likes = redis_db.get('likes:creator:' + creator)

    if creator_num_likes is None:
        creator_num_likes = 1
        redis_db.setex(
            'likes:creator:' + creator,
            creator_num_likes,
            3600
        )
    else:
        creator_num_likes = creator_num_likes.decode('utf-8')
        redis_db.incr('likes:creator:' + creator)

    return (
        "You limit: {} likes from {} sec".format(
            5 - int(creator_num_likes),
            redis_db.ttl('likes:creator:' + creator)
        )
    )


def get_likes(advert_id):
    likes = redis_db.get('likes:advert:' + advert_id)
    if likes is None:
        likes = 0
    else:
        likes = int(likes)
    return likes


def number_creator_likes(creator):
    number = redis_db.get('likes:creator:' + creator)
    if number is None:
        return 0
    return int(number.decode('utf-8'))


def number_creator_comments(creator):
    number = redis_db.get('comments:creator:' + creator)
    if number is None:
        return 0
    return int(number.decode('utf-8'))


def user_in_db(user):
    return user in users


if __name__ == "__main__":
    pass
