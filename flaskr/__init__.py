import math
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


def get_list_from_id(id):
    return List.query.get(id)


def pretty_reldate(datetime_obj):
    # d = Difference
    # The difference of two datetime objects automatically becomes a timedelta object
    d = datetime.now() - datetime_obj

    if d.seconds < 60:  # < a minute
        return 'Just now'
    elif d.seconds / 60 / 60 < 1:  # < a hour
        min = math.floor(d.seconds / 60)
        return str(min) + ' minute ago' if min == 1 else str(min) + ' minutes ago'
    elif d.days < 1:  # < a day
        hours = math.floor(d.seconds / 60 / 60)
        return str(hours) + ' hour ago' if hours == 1 else str(hours) + ' hours ago'
    elif d.days / 7 < 1:  # < a week
        days = d.days
        return str(days) + ' day ago' if days == 1 else str(days) + ' days ago'
    elif d.days / (365/12) < 1:  # < a month
        weeks = math.floor(d.days / 7)
        return str(weeks) + ' week ago' if weeks == 1 else str(weeks) + ' weeks ago'
    elif d.days / 365 < 1:  # < a year
        months = math.floor(d.days / (365/12))
        return str(months) + ' month ago' if months == 1 else str(months) + ' months ago'
    else:
        years = math.floor(d.days / 365)
        return str(years) + ' year ago' if years == 1 else str(years) + ' years ago'


app.jinja_env.globals.update(get_list_from_id=get_list_from_id, pretty_reldate=pretty_reldate)

from flaskr.models import List, Item
from flaskr import routes
