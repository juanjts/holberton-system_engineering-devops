#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API"""
    usr_agnt = {'User-agent': 'jjts'}
    query = requests.get('https://www.reddit.com/r/{}/about.json'.
                         format(subreddit),
                         headers=usr_agnt, allow_redirects=False).json()
    try:
        return query.get('data').get('subscribers')
    except Exception:
        pass
    return 0
