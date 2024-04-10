#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """
import json
import requests


def number_of_subscribers(subreddit):
    """ function to return subscribers"""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    request_data = requests.get("https://www.reddit.com/r/{}/hot/.json"
                                .format(subreddit),
                                headers=user_agent,
                                allow_redirects=False)
    if request_data.status_code != 200:
        print("None")
        return 0
    json_data = request_data.json().get("data").get("children", [])
    if len(json_data) == 0:
        print("None")
        return
    for any_post in json_data[0:10]:
        print(any_post.get("data").get("title"))
