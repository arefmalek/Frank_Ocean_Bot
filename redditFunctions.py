import json
import praw
import requests
import os


with open("keys.json") as f:
    info = json.load(f)

def redAuth():
    reddit = praw.Reddit(client_id= info["reddit"]["client_id"],
                        client_secret= info["reddit"]["client_secret"],
                        password=info["reddit"]["password"],
                        user_agent=info["reddit"]["user_agent"],
                        username=info["reddit"]["username"])
    return reddit


def createImage(reddit, api):
    for submission in reddit.subreddit("frankocean").search(
        'flair:"fan art"', 
        limit=5,
        time_filter="day"
        ):
        if ".jpg" in submission.url:
            post = submission
            break
    print(post.author)
    message = "Today's post is from u/" + str(post.author)

    filename = 'pics/temp.jpg'
    request = requests.get(post.url, stream=True)

    if request.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else: print('cannot download')
