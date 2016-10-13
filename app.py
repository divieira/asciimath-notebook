from flask import Flask, redirect, render_template, request
from flask_heroku import Heroku
from flask_sqlalchemy import SQLAlchemy
import datetime as dt
import logging

# Initialize Heroku app and database connection
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
heroku = Heroku(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Supress warning
db = SQLAlchemy(app)

app.debug = True


# SQLAlchemy Database entity for a note
# (each class corresponds to a database table and each instance to a table row)
class Note(db.Model):
    '''ORM mapping of the Note entity'''
    # Each attribute is a table column
    # These attributes are created automatically
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    modified_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)

    # These attributes should be set manually (default: None)
    title = db.Column(db.String)
    content = db.Column(db.String)


# Flask URL handlers
@app.route('/')
def index():
    '''Index page'''

    # Query all instances of Note from database
    notes = Note.query.all()

    # Render index page listing all notes
    return render_template('index.html', notes=notes)


@app.route('/note/new')
def note_new():
    '''Create a new note'''

    # Create a new instance from Note and add it to database
    note = Note()
    db.session.add(note)
    db.session.commit()

    # Redirect user to newly created note
    return redirect('/note/%d' % note.id)


@app.route('/note/<int:note_id>', methods=['GET', 'POST'])
def note(note_id):
    '''Open/update an existing note'''

    # Retrieve an existing instance from Note by id
    note = Note.query.get_or_404(note_id)

    if request.method == 'POST':
        # If responding to a POST, update fields from HTML form (if present)
        note.title = request.form.get('title', note.title)
        note.content = request.form.get('content', note.content)
        note.modified_at = dt.datetime.now()

        # And commit instance changes to database
        db.session.add(note)
        db.session.commit()

    # Render note page containing an HTML form with instance contents
    return render_template('note.html', note=note)


# Run app from command-line
if __name__ == '__main__':
    app.run()
