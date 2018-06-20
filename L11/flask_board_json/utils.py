#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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
