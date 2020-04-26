from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


def get_list_from_id(id):
    return List.query.get(id)


def get_datetime_diff(id):
    item = Item.query.get(id)
    diff = datetime.now() - item.date_posted
    if diff.days > 7:
        return diff.str(D)
    return repr(diff)


app.jinja_env.globals.update(get_list_from_id=get_list_from_id, get_datetime_diff=get_datetime_diff)

from flaskr.models import List, Item
from flaskr import routes
