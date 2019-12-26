# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 16:21:08 2019

@author: chenp
"""

import praw 
#https://towardsdatascience.com/scraping-reddit-data-1c0af3040768


reddit = praw.Reddit(client_id='OtBVnyEJ_YCE-g', client_secret='x9Lq_Nk4XnX1tSbZ7_vVrJ5U3ck', user_agent='RedditWebScraping')
subreddit = input('Please enter the subreddit that you would like to display:')
# get 10 hot posts from the MachineLearning subreddit
a = []
hot_posts = reddit.subreddit(subreddit).hot(limit=10)
for post in hot_posts:
    a.append("Upvotes:"+str(post.score)+" "+post.title+"\n")
print(a)

    
