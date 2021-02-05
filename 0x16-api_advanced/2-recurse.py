#!/usr/bin/python3
"""
function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """the all titles from hot posts listed for a given subreddit."""
    usr_agnt = {'User-agent': 'jjts'}
    query = requests.get('https://www.reddit.com/r/{}/hot.json'.
                         format(subreddit), headers=usr_agnt,
                         params={'after': after}, allow_redirects=False).json()
    if not query:
        return (None)
    else:
        child_data = query.get('data').get('children')

        for title_data in child_data:
            hot_list.append(title_data.get('data').get('title'))

        if query.get('data').get('after') is not None:
            after = query.get('data').get('after')
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
