import pandas as pd
import numpy as np

import requests

#got these libraries from the zoom-video Varun posted in Slack
from time import sleep 
import datetime
import warnings
import sys

#this function was taken from the zoom-video Varun posted in Slack
def get_posts(subreddit, n_iter, epoch_right_now):
    base_url = 'https://api.pushshift.io/reddit/search/submission/?subreddit='
    df_list = []
    current_time = epoch_right_now
    for post in range(n_iter):
        res = requests.get(base_url, params={'subreddit' : subreddit,
                                            'size' : 100,
                                            'lang' : True,
                                            'before': current_time})
        df = pd.DataFrame(res.json()['data'])
        df = df.loc[:, ['title', 'created_utc', 'selftext', 'subreddit', 'author', 'media_only', 'permalink']]
        df_list.append(df)
        current_time = df['created_utc'].min()
        sleep(10)
    return pd.concat(df_list, axis=0)


#getting 15,000 post from the Showerthoughts & Unpopular Opinion subreddits
rant = get_posts('rant', 150, 1617068868)
pins = get_posts('unpopularopinion', 150, 1617068868)

#concated df of 15,000 posts from Rant and 15,000 posts from UnpopularOpinions
unpopular_rants = pd.concat([rant, pins])

unpopular_rants.to_csv('data/unpopular_rants_30k.csv', index=False)