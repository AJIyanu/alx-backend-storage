#!/usr/bin/env python3
"""
track how many times a particular URL was accessed in the key
and cache the result with an expiration time of 10 seconds
"""


import requests
import functools
import redis
from typing import Callable


storage = redis.Redis()


def countcache(func: Callable) -> Callable:
    """counts the url calls and cache result"""
    @functools.wraps(func)
    def wrapper(arg):
        """wrap me please"""
        if storage.get(f"count:{arg}"):
            storage.incr(f"count:{arg}")
        else:
            storage.set(f"count:{arg}", 1)
        result = storage.get(f"result:{arg}")
        if result:
            return result.decode("utf-8")
        else:
            storage.setex(f"result:{arg}", 10, func(arg))
        return storage.get(f"result:{arg}").decode("utf-8")
    return wrapper


@countcache
def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL and returns it."""
    return requests.get(url).text
