#!/usr/bin/env python3
'''inserts a document in a collection'''


def insert_school(mongo_collection, **kwargs):
    '''adds a document to a collection'''
    insert = mongo_collection.insertOne(kwargs)
    return insert.inserted_id
