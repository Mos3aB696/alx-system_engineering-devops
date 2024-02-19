#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    the_list = {}
    for user in users:
        user_id = user.get("id")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        the_list[user_id] = []
        for todo in todos:
            the_list[user_id].append({
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            })
        with open("todo_all_employees.json", "w") as json_f:
            json.dump(the_list, json_f)
