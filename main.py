from flask import Flask, render_template, request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    note = db.Column(db.String(120))

    def __init__(self, username, email, note):
        self.username = username
        self.email = email
        self.note = note

    def __repr__(self):
        return '<Note %r>' % self.username

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_note(self):
        return self.note


@app.route('/detail')
def detail_get():
    i = request.args.get('id')
    list = Todo.query.get(i)
    return jsonify(
        id=list.get_id(),
        username=list.get_username(),
        email=list.get_email(),
        note=list.get_note()
    )


@app.route('/')
def index():
    list = Todo.query.all()



@app.route('/create', methods=['POST'])
def add_note():
    if request.method == 'POST':
        username = request.json['username']
        email = request.json['email']
        note = ['note'][0]
        todo = Todo(username, email, note)
        db.session.add(todo)
        db.session.commit()
        return request.json


if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")
