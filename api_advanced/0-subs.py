#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    try:
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={'User-Agent': USER_AGENT}
        )
        response.raise_for_status()
        return response.json()['data']['subscribers']
    except (requests.RequestException, ValueError, KeyError):
        return 0
