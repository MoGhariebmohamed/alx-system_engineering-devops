#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """ function to return subscribers"""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    request_data = requests.get("https://www.reddit.com/r/{}/about.json"
                                .format(subreddit),
                                headers=user_agent,
                                allow_redirects=False)
    if request_data.status_code != 200:
        return 0
    return request_data.json().get("data").get("subscribers")
