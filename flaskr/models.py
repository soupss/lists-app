from flaskr import db
from datetime import datetime


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    items = db.relationship('Item', backref='list', lazy=True)

    def __repr__(self):
        return f"List('{self.name}')"


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text, nullable=True)
    date_posted = db.Column(db.DateTime(), nullable=False,
                            default=datetime.utcnow)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)

    def __repr__(self):
        return f"Item('{self.title}', '{self.date_posted}', '{self.list_id}')"
