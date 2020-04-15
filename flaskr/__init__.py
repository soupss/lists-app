from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.String(1000), nullable=True)

    def __repr__(self):
        return f'<{self.task}:{self.desc}>'


@app.route('/')
def index():
    return render_template('index.html')
