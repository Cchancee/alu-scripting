#!/usr/bin/python3
"""A simple script to get the number of subscribers for a given subreddit."""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    try:
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={'User-Agent': '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        )
        response.raise_for_status()
        return response.json()['data']['subscribers']
    except (requests.RequestException, ValueError, KeyError):
        return 0

# Example usage:
print(number_of_subscribers('python'))
