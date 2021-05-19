#!/usr/bin/python3
""" Module containing a recursive function that gets the
top then hot posts of a subreddit """

import requests


def recurse(subreddit, hot_list=[], after=None):
    """ A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit. If no
    results are found for the given subreddit, the function should return
    None. """
    # Set up url's
    reddit_url = 'https://reddit.com/'
    sub_url = reddit_url + 'r/' + subreddit
    # Set up variables
    headers = {
        'User-agent': 'my_api'
    }
    params = {
        "after": after,
        "limit": 100
    }
    #Start
    subereddit_test = requests.get(sub_url, headers=headers)
    if subereddit_test.status_code is not 200:
        return (None)
    about_json = requests.get(sub_url + "/hot.json",
                              headers=headers,
                              params=params)
    hot = about_json.json()['data']['children']
    checkpoint = about_json.json()['data']['after']
    for item in hot:
        hot_list.append(item['data']['title'])
    if checkpoint is None:
        return hot_list
    else:
        return recurse(subreddit, hot_list, checkpoint)