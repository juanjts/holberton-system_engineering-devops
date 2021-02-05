#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """the titles of the first 10 hot posts listed for a given subreddit."""
    usr_agnt = {'User-agent': 'jjts'}
    query = requests.get('https://www.reddit.com/r/{}/hot.json'.
                         format(subreddit),
                         headers=usr_agnt, allow_redirects=False).json()
    try:
        child_data = query.get('data').get('children')
        for top in range(10):
            print(child_data[top].get('data').get('title'))
        return
    except Exception:
        pass
    print(None)
    return
