#!/usr/bin/env python3
'''returns list of documents'''


def schools_by_topic(mongo_collection, topic):
    '''returns the list of school having a specific topic'''
    documents = mongo_collection.find()
    if documents:
        return [doc for doc in documents if topic in doc.topics]
    else:
        return []
