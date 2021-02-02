#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    users = requests.get('https://jsonplaceholder.typicode.com/users',
                         params={"id": argv[1]})
    todos = requests.get('https://jsonplaceholder.typicode.com/todos',
                         params={"userId": argv[1]})

    todos_jsn = todos.json()
    users_jsn = users.json()

    for u_name in users_jsn:
        USERNAME = u_name.get('username')
        USER_ID = u_name.get('id')

    with open(str(USER_ID) + ".csv", mode='w') as f:
        csv_obj = csv.writer(f, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todos_jsn:
            TASK_STATUS = tasks.get("completed")
            TASK_TITLE = tasks.get("title")
            csv_obj.writerow([USER_ID, USERNAME, TASK_STATUS, TASK_TITLE])
