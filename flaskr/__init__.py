from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskr.models import List
from flaskr import routes


def get_list_from_id(id):
    return List.query.get(id)


app.jinja_env.globals.update(get_list_from_id=get_list_from_id)
