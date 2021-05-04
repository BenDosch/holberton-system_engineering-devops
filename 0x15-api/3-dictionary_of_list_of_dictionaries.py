#!/usr/bin/python3
"""Gets API info baised on ID"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    with open('todo_all_employees.json', mode='w') as f:
        r = requests.get("https://jsonplaceholder.typicode.com/users/").json()
        data_dict = {}
        for each in r:
            s = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                             format(each["id"]) + "/todos").json()
            data = []
            for task in s:
                data.append({"task": task["title"],
                             "completed": task["completed"],
                             "username": each["username"]})
            data_dict[each["id"]] = data

        json.dump(data_dict, f)
