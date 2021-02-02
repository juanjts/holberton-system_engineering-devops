#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
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
    id_tasks = {USER_ID: []}
    task_dic = {}
    with open(str(USER_ID) + ".json", mode='w') as f:
        for tasks in todos_jsn:
            task_dic["task"] = tasks.get('title')
            task_dic["completed"] = tasks.get('completed')
            task_dic["username"] = USERNAME
            id_tasks[USER_ID].append(task_dic)
        json.dump(id_tasks, f)
