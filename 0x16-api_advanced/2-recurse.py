#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers """
import json
import requests


def recurse(subreddit, hot_list=[], after=None, my_flag=0):
    """recursive function to return hot titles"""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    if after is None:
        if my_flag == 1:
            return hot_list
        data = requests.get("https://www.reddit.com/r/{}/hot/.json"
                            .format(subreddit),
                            headers=user_agent,
                            allow_redirects=False)
        if data.status_code != 200:
            return None
        else:
            json_data = data.json().get("data").get("children", [])
            for req_post in json_data:
                hot_list.append(req_post.get("data").get("title"))
            my_flag = 1
            after = data.json().get("data").get("after")
            return recurse(subreddit, hot_list, after, my_flag)
    else:
        data = requests.get("https://www.reddit.com/r/{}/hot/.json?after={}"
                            .format(subreddit, after),
                            headers=user_agent,
                            allow_redirects=False)
        json_data = data.json().get("data").get("children", [])
        for post in json_data:
                hot_list.append(post.get("data").get("title"))
        after = data.json().get("data").get("after")
        return recurse(subreddit, hot_list, after, my_flag)
