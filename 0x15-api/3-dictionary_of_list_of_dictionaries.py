#!/usr/bin/python3
"""Exports from JSON"""
import json
import requests


if __name__ == "__main__":
    all_ut = {}

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    for a_user in users:
        List = []
        for data in todos:
            if data.get('userId') == a_user.get('id'):
                task_dict = {"username": a_user.get('username'),
                             "task": data.get('title'),
                             "completed": data.get('completed')}
                List.append(task_dict)
        all_ut[a_user.get('id')] = List

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(all_ut, f)
