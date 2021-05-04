#!/usr/bin/python3
"""Gets API info baised on ID"""
import requests
from sys import argv

if __name__ == "__main__":

    r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/".format(argv[1])).json()
    s = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(argv[1])).json()
    completed = 0
    total = 0
    for each in r:
        if each["completed"] == True:
            completed += 1
        total += 1
    print("Employee {} is done with tasks({}/{}):".format(s["name"], completed, total))
    for each in r:
        if each["completed"] == True:
            print("\t" + " " + each["title"])