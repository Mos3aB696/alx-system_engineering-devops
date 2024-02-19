#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3  0-gather_data_from_an_API.py EMPLOYEE_ID")
        exit(1)

    employee_id = argv[1]

    # Make a GET request to retrieve employee information
    response_user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    user_data = response_user.json()
    employee_name = user_data.get('name')

    # Make a GET request to retrieve employee's TODO list
    response_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id))
    todos_data = response_todos.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Print the employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_tasks, total_number_of_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
