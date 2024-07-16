#!/usr/bin/env python3
""" Improvement 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs """

from pymongo import MongoClient


def nginx_stats_check():
    """ Shows some stats about Nginx logs stored in MongoDB:"""
    client = MongoClient()
    rec = client.logs.nginx

    docs_count = rec.count_documents({})
    print("{} logs".format(num_of_docs))
    print("Methods:")
    methods_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods_list:
        method_count = rec.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    status = rec.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))

    print("IPs:")

    top_IPs = rec.aggregate([
        {"$group":
         {
             "_id": "$ip",
             "count": {"$sum": 1}
         }
         },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])
    for top_ip in top_IPs:
        cnt = top_ip.get("count")
        ip_address = top_ip.get("ip")
        print("\t{}: {}".format(ip_address, cnt))


if __name__ == "__main__":
    nginx_stats_check()
