#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
from sys import argv
if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    the_list = []
    for todo in todos:
        the_list.append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        })

    with open("{}.json".format(user_id), "w") as json_f:
        json.dump({user_id: the_list}, json_f)
