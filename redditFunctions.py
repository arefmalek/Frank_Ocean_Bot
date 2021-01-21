import praw
import requests
import os

from random import randint


def createImage(reddit, api):
    choices = []

    for submission in reddit.subreddit("frankocean").search(
        'flair:"fan art"', 
        limit=10,
        time_filter="day"
        ):
        if ".jpg" in submission.url:
            choices.append(submission)
    
    pick = randint(0, len(choices) - 1)
    post = choices[pick]
    print(post.author)
    message = "Today's post is from u/" + str(post.author)

    filename = 'static/temp.jpg'
    request = requests.get(post.url, stream=True)

    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else: print('cannot download')
