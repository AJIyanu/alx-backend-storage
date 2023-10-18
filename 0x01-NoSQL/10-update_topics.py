#!/usr/bin/env python3
"""update topics based on name"""


def update_topics(mongo_collection, name, topics):
    """reurns nothing just updates topics"""
    match = {"name": name}
    update = {"$set": {"topics": topics}}
    mongo_collection.update_one(match, update)
