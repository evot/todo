import time
import uuid

from flask import session


def format_time(timestamp):
    now = int(time.time())
    n = time.localtime(now)
    t = time.localtime(timestamp)
    this_year = time.strftime('%Y', n)
    timestamp_year = time.strftime('%Y', t)
    if this_year != timestamp_year:
        time_format = '%y-%m-%d %H:%M'
    else:
        time_format = '%m-%d %H:%M'
    ft = time.strftime(time_format, t)
    return ft


def gen_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid.uuid4())
    return session['_csrf_token']
