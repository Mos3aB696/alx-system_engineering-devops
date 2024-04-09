#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    (total subscribers) for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    base_url = "https://www.reddit.com/r/"
    url = f"{base_url}{subreddit}/about.json"

    headers = {
        "User-Agent": "Custom User Agent (your choice)"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["data"]["subscribers"]
    except (requests.RequestException, KeyError):
        return 0
