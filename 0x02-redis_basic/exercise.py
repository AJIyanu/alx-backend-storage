#!/usr/bin/env python3
"""This is a Reddis Module"""


import redis
import uuid


class Cache:
    """Cache class instance of reddis"""


    def __init__(self):
        """create redis sharp sharp"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float)-> uuid.uuid4():
        """stores data with a random key"""
        key = uuid.uuid4()
        self._redis.mset({key: data})
        return key
