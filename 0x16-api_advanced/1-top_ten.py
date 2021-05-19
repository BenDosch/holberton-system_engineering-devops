#!/usr/bin/python3
""" Module containing a function that gets the
top then hot posts of a subreddit """

import requests


def top_ten(subreddit):
    """ Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit. """
    # Set up url's
    reddit_url = 'https://reddit.com/'
    sub_url = reddit_url + 'r/' + subreddit
    # Set up variables
    headers = {
        'User-agent': 'my_api'
    }
    params = {
        "limit": "10"
    }
    #Start
    subereddit_test = requests.get(sub_url, headers=headers)
    if subereddit_test.status_code is not 200:
        print('None')
        return
    about_json = requests.get(sub_url + "/hot.json",
                              headers=headers,
                              params=params)
    hot = about_json.json()['data']['children']
    for item in hot:
        print(item['data']['title'])
