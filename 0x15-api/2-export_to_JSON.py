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
    employ_ID = sys.argv[1]
    url_request = requests.get('{}/users/{}'
                               .format(API_URL, employ_ID)).json()
    url_tasks = requests.get('{}/todos'.format(API_URL)).json()
    usr_name = url_request.get('username')
    tasks_stat = requests.get('{}/users/{}/todos'
                              .format(API_URL, employ_ID)).json()

    dictionary_data = {employ_ID : []}
    for task in tasks_stat:
            done = task.get('completed')
            done_title = task.get('title')
            dictionary_data[employ_ID].append({"task" : done_title,
                                               "completed" : done,
                                               "username" : usr_name})
    with open('{}.json'.format(employ_ID), 'w') as jsonfile:
        json.dump(dictionary_data, jsonfile)
