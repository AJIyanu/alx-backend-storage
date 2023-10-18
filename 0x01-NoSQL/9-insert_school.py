#!/usr/bin/env python3
"""insert document into db"""


def insert_school(mongo_collections, **kwargs):
    """returns id of successful insert"""
    return mongo_collections.insert_one(kwargs).inserted_id
