#!/usr/bin/env python3
"""This is a Reddis Module"""


import redis
import uuid
from typing import Callable, Union


class Cache:
    """Cache class instance of reddis"""


    def __init__(self):
        """create redis sharp sharp"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int,float])-> str:
        """stores data with a random key"""
        key = String(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Callable = None)->str | Callable:
        """returns desired datatype"""
        if fn is None:
            return None
        else:
            return fn(self._redis.get(key))

    def get_str(self, key: str):
        """return string value"""
        return String(self._redis.get(key))

    def get_int(self, key: str)->int:
        """returns integer"""
        return Int(self._redis.get(key))
