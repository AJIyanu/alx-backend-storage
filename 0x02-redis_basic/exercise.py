#!/usr/bin/env python3
"""
Learn how to use redis for basic operations
Learn how to use redis as a simple cache
"""

import redis
import uuid
from functools import wraps
# import json
from typing import Union, Callable, Any


def count_calls(method: Callable[[Any], Any])-> Callable:
    """decorator to count numer of times a func is called"""
    @wraps(method)
    def wrapper(self, key):
        wrapper.count += 1
        self._redis.mset({method.__qualname__: wrapper.count})
        return method(self, key)
    wrapper.count = 0
    return wrapper

class Cache:
    """
    Basic redis operations
    simple cache with redis
    """

    def __init__(self)-> None:
        """creates an instance of reddis with empty data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float])-> str:
        """stores a data to redis and returns the key"""
        key = str(uuid.uuid4())
        new_insert = {key: data}
        self._redis.mset(new_insert)
        return key

    def get(self, key: str, fn: Callable[[Any], Any]=None)-> Any:
        """gets data stored by key and returns the data"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str)-> str:
        """returns a stringed get"""
        data = self._redis.get(key)
        if data is None:
            return None
        return str(data)

    def get_int(self, key: str)-> int:
        """returnis int value"""
        data = self._redis.get(key)
        if data is None:
            return None
        return int(data)
