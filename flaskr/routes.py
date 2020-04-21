from flask import render_template, redirect, url_for, request
from flaskr import app, db
from flaskr.models import List, Item


def has_favorite():
    items = Item.query.all()
    for item in items:
        if item.favorite:
            return True
    return False


@app.route('/', methods=['GET'])
def root():
    return redirect(url_for('home'))


# show all lists
@app.route('/lists')
def home():
    lists = List.query.all()
    return render_template('list.html', lists=lists, show_fav=has_favorite())


# show specific list
@app.route('/lists/<int:id>')
def show_list(id):
    lists = List.query.all()
    selected_list = List.query.get_or_404(id)
    return render_template('list.html', lists=lists, selected_list=selected_list, show_fav=has_favorite())


# show favorite list
@app.route('/lists/favorite')
def favorite_list():
    lists = List.query.all()
    items = Item.query.all()
    fav_list = []
    if items:
        for item in items:
            if item.favorite:
                fav_list.append(item)
    return render_template('favorite.html', lists=lists, fav_list=fav_list, show_fav=has_favorite())


@app.route('/lists', methods=['POST'])
def create_list():
    list_name = request.form.get('name').strip()
    list = List(name=list_name)
    db.session.add(list)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/lists/<int:id>/edit', methods=['POST'])
def edit_list(id):
    list = List.query.get_or_404(id)
    list.name = request.form.get('name').strip()
    db.session.commit()
    return redirect(url_for('show_list', id=id))


@app.route('/lists/<int:id>/delete', methods=['POST'])
def delete_list(id):
    list = List.query.get_or_404(id)
    for item in list.items:
        db.session.delete(item)
    db.session.delete(list)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/lists/<int:id>', methods=['POST'])
def create_item(id):
    title = request.form.get('title').strip()
    description = request.form.get('description').strip()
    item = Item(title=title, description=description, list_id=id)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('show_list', id=id))


@app.route('/lists/<int:id>/item/edit/<re_to_fav>', methods=['POST'])
def edit_item(id, re_to_fav):
    item = Item.query.get_or_404(id)
    item.title = request.form.get('title').strip()
    item.description = request.form.get('description').strip()
    db.session.commit()
    if re_to_fav == 'true':
        if has_favorite():
            return redirect(url_for('favorite_list'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('show_list', id=item.list_id))


@app.route('/lists/<int:id>/item/delete/<re_to_fav>', methods=['POST'])
def delete_item(id, re_to_fav):
    item = Item.query.get_or_404(id)
    list_id = item.list_id
    db.session.delete(item)
    db.session.commit()
    if re_to_fav == 'true':
        if has_favorite():
            return redirect(url_for('favorite_list'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('show_list', id=item.list_id))


@app.route('/lists/<int:id>/item/favorite/<re_to_fav>', methods=['POST'])
def toggle_favorite(id, re_to_fav):
    item = Item.query.get_or_404(id)
    if item.favorite:
        item.favorite = False
    else:
        item.favorite = True
    db.session.commit()
    if re_to_fav == 'true':
        if has_favorite():
            return redirect(url_for('favorite_list'))
        else:
            return redirect(url_for('home'))
    else:
        return redirect(url_for('show_list', id=item.list_id))
