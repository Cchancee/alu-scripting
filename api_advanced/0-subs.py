#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


# Define the User-Agent header as a constant
USER_AGENT = '0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)'

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    try:
        # Make the request to the Reddit API
        response = requests.get(
            f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={'User-Agent': USER_AGENT}
        )
        # Raise an exception if the request was not successful
        response.raise_for_status()
        # Get the number of subscribers from the JSON response
        return response.json()['data']['subscribers']
    except (requests.RequestException, ValueError, KeyError):
        # Handle errors by returning 0
        return 0
