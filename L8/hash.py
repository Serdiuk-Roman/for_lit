from hashlib import md5


def hash_md5(str):
    return md5(str.encode())
