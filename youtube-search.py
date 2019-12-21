import os
import time
import requests
import json
import pandas as pd
import datetime as dt
import db_connection

API_KEY = os.environ['API_KEY']

CHANNEL_ID = 'UCiPWgxymXUATul-vG_Jzhsw'

base_url = 'https://www.googleapis.com/youtube/v3'
url = base_url + '/search?key=%s&channelId=%s&part=snippet,id&order=date&maxResults=50'
infos = []

res = requests.get(url % (API_KEY, CHANNEL_ID))
result = res.json()

infos.extend([
    [item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['publishedAt']]
    for item in result['items'] if item['id']['kind'] == 'youtube#video'
])

videos = pd.DataFrame(infos, columns=['videoId', 'title', 'description', 'publishedAt'])
videos['publishedAt'] = pd.to_datetime(videos['publishedAt'], format='%Y-%m-%d')
videos['channel_id'] = CHANNEL_ID
videos.to_csv('videos.csv', index=None)

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
def add(videos):

    conn = db_connection.connect()
    cur = conn.cursor()

    columns = ['videoId', 'title', 'description', 'channel_id','publishedAt']

    add_video = ("INSERT INTO youtube "
    "(videoId, title, description, channel_id, publishedAt) "
    "VALUES (%(videoId)s, %(title)s, %(description)s, %(channel_id)s, %(publishedAt)s)")

    try:
        for video in videos.itertuples():

            data_video = {
                'videoId': video.videoId,
                'title': video.title,
                'description': video.description,
                'channel_id': video.channel_id,
                'publishedAt': video.publishedAt.strftime('%Y-%m-%d %H:%M:%S')
            }

            cur.execute(add_video, data_video)
        conn.commit()
    except:
        conn.rollback()
        raise

    cur.close()
    conn.close()

add(videos)