import pandas as pd
from  db import query
import pandas as pd
import youtube_dl

def download(videos):

    base_url = 'https://www.youtube.com/watch?v='

    # 240p
    kaizodo = '133'

    videos = videos[['videoId', 'title']]

    for index, video in videos.iterrows():

        url = base_url + video['videoId']

        outtmpl = video['title'] + '.%(ext)s'
        ydl = youtube_dl.YoutubeDL({'outtmpl': outtmpl,'format': kaizodo})

        with ydl:
            ydl.extract_info(
                url,
                download=True # We just want to extract the info
            )

videos = query.select_all()
download(videos)