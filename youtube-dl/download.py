import pandas as pd
from  db import query
import pandas as pd
import youtube_dl

def download():

    videos = query.select_all()

    base_url = 'https://www.youtube.com/watch?v='

    # 240p
    kaizodo = '133'

    url = base_url + videos['videoId'].values[0]

    outtmpl = videos['title'].values[0] + '.%(ext)s'
    ydl = youtube_dl.YoutubeDL({'outtmpl': outtmpl,'format': kaizodo})

    with ydl:
        result = ydl.extract_info(
            url,
            download=True # We just want to extract the info
        )
    return result

download()
