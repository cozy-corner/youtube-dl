from . import db_connection
import pandas.io.sql as psql
import binascii
import pandas as pd

# https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
def add(videos):

    conn = db_connection.connect()
    cur = conn.cursor()

    columns = ['videoId', 'title', 'description', 'channel_id','publishedAt']

    add_video = ("INSERT IGNORE INTO youtube "
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
    finally:
        cur.close()
        conn.close()

def select_all():

    conn = db_connection.connect()

    select_video = ("SELECT videoId, title, description, channel_id FROM youtube "
         "WHERE download_url is null;")

    try:    
        videos = psql.read_sql(sql=select_video, con=conn, coerce_float=False)
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        conn.close()
    
    videos['videoId'] = videos['videoId'].str.decode('utf-8')
    videos['title'] = videos['title'].str.decode('utf-8')
    videos['description'] = videos['description'].str.decode('utf-8')
    videos['channel_id'] = videos['channel_id'].str.decode('utf-8')

    return videos