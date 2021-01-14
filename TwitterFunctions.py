import tweepy
from datetime import datetime


def read_last_tweet(filename):
    """opens a text file with the id of the last tweet
    copies that down to an an integer last_seen_tweet then returns that"""
    file_read = open(filename, 'r')
    last_seen_tweet = int(file_read.read().strip())
    file_read.close()
    return last_seen_tweet


def store_last_tweet(filename, last_tweet_id):
    """opens the file where the id of the last tweet was stored
    overwrites the previous data with the id of the most recent '@ tweet'"""
    file_write = open(filename, 'w')
    file_write.write(str(last_tweet_id))
    file_write.close()
    return


def reply(api, FILE_NAME):
    tweets = api.mentions_timeline(read_last_tweet(FILE_NAME), tweet_mode='extended')
    for tweet in reversed(tweets):
        if (tweet.id == read_last_tweet(FILE_NAME)):
            print("same")
            return
        
        if "#blondedbot" in tweet.full_text.lower():
            print(str(tweet.id) + " - " + tweet.full_text)
            api.update_status('@' + tweet.user.screen_name +
                              " Yeah it's working! Current time is " + 
                              datetime.now().strftime("%H:%M:%S"), tweet.id)
            # api.create_favorite(tweet.id)
            # api.retweet(tweet.id)
            store_last_tweet(FILE_NAME, tweet.id)
            print("completed reading!")
