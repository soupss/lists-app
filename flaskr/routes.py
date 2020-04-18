from flask import render_template, redirect, url_for, request
from flaskr import app, db
from flaskr.models import List, Item


@app.route('/create-list', methods=['POST'])
def create_list():
    list_name = request.form['list']
    list = List(name=list_name)
    db.session.add(list)
    db.session.commit()
    return redirect(url_for('list', id=list.id))


@app.route('/<id>', methods=['GET', 'POST'])
def list(id):
    if request.method == 'POST':
        item = Item(title=request.form['title'], description=request.form['description'], list_id=id)
        db.session.add(item)
        db.session.commit()

    selected_list = List.query.get(id)
    lists = List.query.all()
    return render_template('home.html', lists=lists, selected_list=selected_list)


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('list', id=List.query.first().id))
