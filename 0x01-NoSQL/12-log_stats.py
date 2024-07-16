#!/usr/bin/env python3
"""
A function that Provides some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient

def print_nginx_request_logs(nginx_collection):
    """Shows some stats about Nginx logs stored in MongoDB.

    Args:
        nginx_collection (pymongo.collection.Collection): collection to analyze
    """
    print('{} logs'.format(nginx_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        cnt = len(list(nginx_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method,cnt))
    confirm_checks_count = len(list(
        nginx_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(confirm_checks_count))


def run():
    """shows some stats about Nginx logs stored in MongoDB.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
