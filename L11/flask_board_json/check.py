#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from db import number_creator_likes, number_creator_comments, user_in_db


def check_login(data):
    error = []
    count = 0

    username = data['username']
    password = data['password']
    confirm_password = data['confirm_password']

    if not (0 < len(username) <= 20):
        error.append("username is necessarily, max 20")
        count += 1
    if not (0 < len(password) <= 50):
        error.append("password is necessarily, max 20")
        count += 1
    if not (0 < len(confirm_password) <= 20):
        error.append("confirm_password is necessarily, max 20")
        count += 1
    if password != confirm_password:
        error.append("password not equel confirm_password")
        count += 1
    if user_in_db(username):
        error.append("User with nickname {} exists".format(username))
        count += 1

    if count != 0:
        return (False, error)
    return (True, )


def advert_is_valid(creator, advert_name):
    error = []
    count = 0

    if not (0 < len(creator) <= 20):
        error.append("Username is necessarily, max 20")
        count += 1
    if not (0 < len(advert_name) <= 50):
        error.append("Text is necessarily, max 50")
        count += 1

    if count != 0:
        return (False, error)
    return (True, )


def comment_is_valid(creator, comment):
    error = []
    count = 0

    if not (0 < len(creator) <= 20):
        error.append("Username is necessarily, max 20")
        count += 1
    if not (0 < len(comment) <= 255):
        error.append("Comment is necessarily, max 255")
        count += 1

    if count != 0:
        return (False, error)
    return (True, )


def comments_limit(creator):

    number = number_creator_comments(creator)

    if number > 5:
        return (False, "exceeded the limit of comments (5 in hours)")
    else:
        return(True, )


def likes_limit(creator):

    number = number_creator_likes(creator)

    if number > 5:
        return (False, "exceeded the limit of likes (5 in hours)")
    else:
        return(True, )
