#!/usr/bin/python3
"""Gets API info baised on ID"""
import json
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/".
                     format(argv[1])).json()
    s = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(argv[1])).json()
    with open('{}.json'.format(argv[1]), mode='w') as f:
        data = []
        for each in r:
            data.append({"task": each["title"],
                         "completed": each["completed"],
                         "username": s["username"]})
        json.dump({argv[1]: data}, f)
