from datetime import datetime
from flask import render_template, request
from flaskr import app, db
from flaskr.models import List, Item


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        list_name = request.form['list']
        list = List(name=list_name)
        db.session.add(list)
        db.session.commit()
    lists = List.query.all()
    return render_template('index.html', lists=lists)
