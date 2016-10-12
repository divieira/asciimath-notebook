from flask import Flask, redirect, render_template, request
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
import datetime as dt
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
heroku = Heroku(app)
db = SQLAlchemy(app)

app.debug = True


class Note(db.Model):
    '''ORM mapping of the Note entity'''
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    modified_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    title = db.Column(db.String)
    content = db.Column(db.String)


@app.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)


@app.route('/note/new')
def note_new():
    note = Note()
    db.session.add(note)
    db.session.commit()
    return redirect('/note/%d' % note.id)


@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def note(note_id):
    note = Note.query.get_or_404(note_id)

    if request.method == 'POST':
        note.title = request.form.get('title')
        note.content = request.form.get('content')
        note.modified_at = dt.datetime.now()
        db.session.add(note)
        db.session.commit()

    return render_template('note.html', note=note)


if __name__ == '__main__':
    app.run()
