#!/usr/bin/python3
"""
  The function `number_of_subscribers` retrieves the number
  of subscribers for a given subreddit using the Reddit API.

  :param subreddit: The `number_of_subscribers` function
  takes a subreddit name as a parameter and
  returns the number of subscribers for that subreddit
  by making a request to the Reddit API
  :return: The function `number_of_subscribers(subreddit)`
  returns the number of subscribers for a
  given subreddit. If the request to the Reddit API is
  successful (status code 200), it returns the
  number of subscribers. If there is an issue with
  the request, it returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    return response.json().get('data').get('subscribers')
