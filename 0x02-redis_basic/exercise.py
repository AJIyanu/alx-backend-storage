#!/usr/bin/env python3
"""
Learn how to use redis for basic operations
Learn how to use redis as a simple cache
"""

import redis
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

