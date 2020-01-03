import os
import time
import requests
import json
import pandas as pd
import datetime as dt
from  db import query
import download

API_KEY = os.environ['API_KEY']

with open("params.json", 'r') as f:
    channels = json.load(f)['channels']

base_url = 'https://www.googleapis.com/youtube/v3'
url = base_url + '/search?key=%s&channelId=%s&part=snippet,id&order=date&maxResults=50'
infos = []

videos = pd.DataFrame()

for channel in channels.values():
    res = requests.get(url % (API_KEY, channel))
    result = res.json()

    infos.extend([
    [item['id']['videoId'], item['snippet']['title'], item['snippet']['description'], item['snippet']['publishedAt']]
    for item in result['items'] if item['id']['kind'] == 'youtube#video'
    ])

    video = pd.DataFrame(infos, columns=['videoId', 'title', 'description', 'publishedAt'])
    video['publishedAt'] = pd.to_datetime(video['publishedAt'], format='%Y-%m-%d')
    video['channel_id'] = channel
    videos = pd.concat([videos,video])

query.add(videos)
