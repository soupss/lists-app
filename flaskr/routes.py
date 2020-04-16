from datetime import datetime
from flask import render_template
from flaskr import app

items = [
    {
        'title': 'Clean the house',
        'desc': 'Bla bla bla bla bla',
        'id': 'demo',
        'date_posted': datetime.utcnow(),
    },
    {
        'title': 'Walk the dog',
        'desc': 'Bla bla bla bla bla',
        'id': 'demo2',
        'date_posted': datetime.utcnow(),
    },
    {
        'title': 'Make an app',
        'desc': 'Bla bla bla bla bla',
        'id': 'demo3',
        'date_posted': datetime.utcnow(),
    }
]


@app.route('/')
def index():
    return render_template('index.html', items=items)
