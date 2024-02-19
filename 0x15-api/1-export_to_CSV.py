#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to CSV format.
"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csv_f:
        writer = csv.writer(csv_f, quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([user_id, user.get("username"),
                            todo.get("completed"), todo.get("title")])
