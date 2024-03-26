#!/usr/bin/python3
"""
The script must display on the standard output the employee TODO list
"""


import csv
import re
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
            employ_ID = int(sys.argv[1])
            url_request = requests.get('{}/users/{}'
                                       .format(API_URL, employ_ID)).json()
            url_tasks = requests.get('{}/todos'.format(API_URL)).json()
            usr_name = url_request.get('username')
            tasks_stat = requests.get('{}/users/{}/todos'
                                       .format(API_URL, employ_ID)).json()
            with open('{}.csv'.format('employ_ID'), 'w') as csvfile:
                for task in tasks_stat:
                    done = task.get('complete')
                    done_title = task.get('title')
                    csvfile.write('"{}","{}","{}","{}"\n'.format(
                                  employ_ID, usr_name, done, done_title))
