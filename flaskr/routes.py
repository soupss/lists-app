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


@app.route('/list/<id>', methods=['GET', 'POST'])
def list(id):
    if request.method == 'POST':  # create item
        title = request.form['title'].strip()
        description = request.form['description'].strip()
        item = Item(title=title, description=description, list_id=id)
        db.session.add(item)
        db.session.commit()

    lists = List.query.all()
    if id == 'none':
        return render_template('home.html', lists=lists)
    else:
        selected_list = List.query.get_or_404(id)
        return render_template('home.html', lists=lists, selected_list=selected_list)


@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('list', id='none'))
