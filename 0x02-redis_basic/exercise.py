#!/usr/bin/env python3
"""
Learn how to use redis for basic operations
Learn how to use redis as a simple cache
"""

import redis
import uuid
# import json
from typing import Union


class Cache:
    """
    Basic redis operations
    simple cache with redis
    """

    def __init__(self)-> None:
        """creates an instance of reddis with empty data"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float])-> str:
        """stores a data to redis and returns the key"""
        key = str(uuid.uuid4())
        new_insert = {key: data}
        self._redis.mset(new_insert)
        return key

