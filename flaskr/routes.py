from flask import render_template, redirect, url_for, request
from flaskr import app, db
from flaskr.models import List


@app.route('/create-list', methods=['POST'])
def create_list():
    list_name = request.form['list']
    list = List(name=list_name)
    db.session.add(list)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/')
def re():
    return redirect(url_for('home'))


@app.route('/home', methods=['GET'])
def home():
    # TODO: check if there are lists
    lists = List.query.all()
    return render_template('home.html', lists=lists)
