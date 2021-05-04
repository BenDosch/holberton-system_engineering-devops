#!/usr/bin/python3
"""Gets API info baised on ID"""
import csv
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/".
                     format(argv[1])).json()
    s = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for each in r:
            writer.writerow([argv[1], s["username"],
                            each["completed"], each["title"]])
