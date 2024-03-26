#!/usr/bin/python3
"""
The script must display on the standard output the employee TODO list
"""


import csv
import json
import re
import requests
import sys


if __name__ == '__main__':
    API_URL = "https://jsonplaceholder.typicode.com"
    url_request = requests.get('{}/users'
                               .format(API_URL)).json()

    employs_dict = {}
    for employe in url_request:
        employ_ID = employe.get('id')
        employ_name = employe.get('username')
        employ_url = requests.get('{}/users/{}/todos'.format(API_URL,
                                                             employ_ID))
        tasks_json = employ_url.json()
        employs_dict[employ_ID] = []
        for task in tasks_json:
            done = task.get('completed')
            done_title = task.get('title')
            employs_dict[employ_ID].append({"task": done_title,
                                            "completed": done,
                                            "username": employ_name})
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(employs_dict, jsonfile)
