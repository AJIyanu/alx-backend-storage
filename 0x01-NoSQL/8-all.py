#!/usr/bin/env python3
"""script to lsit all document in a db"""


from typing import List

def list_all(mongo_collection) -> List[]:
    """returns a list of all document and 
    empty if empty"""
    return list(mongo_collection.find())
