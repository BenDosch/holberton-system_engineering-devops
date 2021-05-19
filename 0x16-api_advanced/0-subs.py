#!/usr/bin/python3
""" Module containing a function that gets the
number of subscribers of a subreddit. """

import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API and returns the number
    of subscribers (not active users, total subscribers) for a given
    subreddit. If an invalid subreddit is given, the function should
    return 0. """
    # Set up url's
    reddit_url = 'https://reddit.com/'
    reddit_api_url = reddit_url + 'api/v1/'
    oauth_api_url = 'https://oauth.reddit.com/api/v1/'
    sub_url = reddit_url + 'r/' + subreddit
    sub_api_url = oauth_api_url + 'r/' + subreddit
    # Set up variables
    client_id = 'wcCpb6wT9YQ7tA'
    secret_key = 'telQ_XfvpjJcBF8QdMkwfrY_Qq-OHQ'
    auth = requests.auth.HTTPBasicAuth(client_id, secret_key)
    data = {
        'grant_type': 'password',
        'user_name': 'BenHolbertonSchool',
        'password': '%74g95qS11'
        }
    headers = {
        'User-agent': 'my_api'
    }
    """ # Get access token and add to headers
    res1 = requests.post(reddit_api_url + 'access_token',
                        auth=auth, data=data, headers=headers)
    token = res1.json()
    headers['Authorization'] = 'bearer ' + token """

    #Start
    subereddit_test = requests.get(sub_url, headers=headers)
    if subereddit_test.status_code is not 200:
        return (0)
    about_json = requests.get(sub_url + "/about.json",
                              headers=headers,
                              allow_redirects=False)
    subscribers = about_json.json()['data']['subscribers']
    return (subscribers)

    #tests
    """print('Check access token')
    print(token)
    print('------------------')
    print('Check authorization')
    print(requests.get(oauth_api_url + 'me', headers=headers))
    print('------------------')
    print("Whats inside????????")
    print(res2.json())"""

if __name__ == '__main__':
    """ For testing """
    number_of_subscribers('Python')
