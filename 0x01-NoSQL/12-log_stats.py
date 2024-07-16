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


def print_nginx_stat():
    """Prints some stats about Nginx stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    print('{} logs'.format(nginx.count_documents({})))
    print('Methods:')


    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx.count_documents({ 'method': method })
        print('\tmethod {}: {}'.format(method, method_count))

    print('{} status check'.format(nginx.count_documents(
        {
            'method': 'GET',
            'path': '/status'
        }
    )))


if __name__ == '__main__':
    print_nginx_stat()
