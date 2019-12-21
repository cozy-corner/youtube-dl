from urllib.parse import urlparse
import mysql.connector

url = urlparse('mysql://docker:docker@mysql_host:3306/youtube_db')

def connect():
    conn = mysql.connector.connect(
        host = url.hostname,
        port = url.port,
        user = url.username,
        password = url.password,
        database = url.path[1:],
    )

    assert(conn.is_connected())
    
    return conn


# https://dev.mysql.com/doc/connector-python/en/