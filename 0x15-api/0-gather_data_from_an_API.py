#!/usr/bin/python3
"""
The script must display on the standard output the employee TODO list
"""


import re
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employ_ID = int(sys.argv[1])
            url_request = requests.get('{}/users/{}'
                                       .format(API_URL, employ_ID)).json()
            url_tasks = requests.get('{}/todos'.format(API_URL)).json()
            emp_name = url_request.get('name')
            emp_tasks = list(filter(lambda x: x.get('userId') == employ_ID,
                                    url_tasks)
                             )
            emp_complt_tsk = list(filter(lambda x: x.
                                         get('completed'), emp_tasks))
            print('Employee {} is done with tasks({}/{}):'
                  .format(emp_name, len(emp_complt_tsk), len(emp_tasks)))

        if len(emp_complt_tsk) > 0:
            for tasks in emp_complt_tsk:
                print('\t {}'.format(tasks.get('title')))
