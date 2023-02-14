#!/usr/bin/env python3
'''updates documents'''
if __name__ == '__main__':
    from pymongo import MongoClient
    with MongoClient() as c:
        coll = c.logs.nginx
        print(f'{coll.count_documents({})} logs')
        print('Methods:')
        print(f"\tmethod GET: {coll.count_documents({'method': 'GET'})}")
        print(f"\tmethod POST: {coll.count_documents({'method': 'POST'})}")
        print(f"\tmethod PUT: {coll.count_documents({'method': 'PUT'})}")
        print(f"\tmethod PATCH: {coll.count_documents({'method': 'PATCH'})}")
        print(f"\tmethod DELETE: {coll.count_documents({'method': 'DELETE'})}")
        stat_chck = coll.count_documents({'method': 'GET', 'path': '/status'})
        print(f"{stat_chck} status check")
