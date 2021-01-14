import tweepy
import praw
import time

from datetime import datetime
from time import sleep
from os import environ

import TwitterFunctions as tf
import redditFunctions as redFunc

# twitter environment variables
consumer_key = environ['TWITTER_CONSUMER_KEY']
consumer_secret = environ['TWITTER_CONSUMER_SECRET']
key = environ['TWITTER_ACCESS_KEY']
secret = environ['TWITTER_ACCESS_SECRET']

#twitter authorize time
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api = tweepy.API(auth)

# reddit environment variables
reddit_client_id = environ['REDDIT_CLIENT_ID']
reddit_client_secret = environ['REDDIT_CLIENT_SECRET']
reddit_password = environ['REDDIT_PASSWORD']
reddit_user_agent = environ['REDDIT_USER_AGENT']
reddit_username = environ['REDDIT_USERNAME']


#reddit authentation
reddit = praw.Reddit(client_id= reddit_client_id,
                     client_secret= reddit_client_secret,
                     password= reddit_password,
                     user_agent=reddit_user_agent,
                     username=reddit_username)



FILE_NAME = 'static/last_tweet.txt'

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if ("23:11" <= current_time <= "23:12"):
        redFunc.createImage(reddit, api)
        print("poggers")
        sleep(60)

    tf.reply(api, FILE_NAME)
    sleep(5)
    print("here")
