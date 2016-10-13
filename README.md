# AsciiMath Notebook

Online notebook with [AsciiMath](http://asciimath.org/) syntax running on [Heroku](https://asciimath-notebook.herokuapp.com/)


## Reference

https://devcenter.heroku.com/articles/getting-started-with-python#introduction

> Notes:
>
>   1. You can follow these instructions, cloning this app instead of the 'python-getting-started' (and ignoring the Django stuff).
>   2. On the creation step, you can use `heroku create _yourappname_` instead of getting a random name.
>   3. After creating the app and provisioning the database, initialize SQLAlchemy (see "Initial setup" below).

## Local requirements

* Heroku toolbelt
* Python 2.7, pip, virtualenv (for developing)
* PostgreSQL (for running locally)
* Optional: virtualenvwrapper


## Initial setup

1. Create the virtual environment:

        $ virtualenv venv (virtualenv) or mkproject -f asciimath-notebook (virtualenvwrapper)

2. Activate the virtual environment:

        $ source venv/bin/activate (Unix) or venv\Scripts\activate (Windows) or workon navegatium-hrk (virtualenvwrapper)

3. Install the requirements:

        $ pip install -r requirements.txt

4. Create (or associate with) a Heroku app:

        $ heroku create _yourappname_

    _or_

        $ heroku git:remote -a _yourappname_

5.  Provision the database add-on

        $ heroku addons:create heroku-postgresql:hobby-dev

5. Deploy the code to the remote server (repeat after every change)

        $ git push heroku master

5. Initialize database on remote server (repeat after every new class)

        $ heroku run python
        >>> from app import db
        >>> db.create_all()

    > Note: If you change or delete a Model class, you may alter or drop the correponding table or `db.drop_all()` (which erases all data)

6. Optional: Initialize database locally (for local testing)

        $ python
        >>> from app import db
        >>> db.create_all()


## Common tasks

### Local testing

1. Activate the virtual environment:

        $ source venv/bin/activate (Unix) or venv\Scripts\activate (Windows) or workon navegatium-hrk (virtualenvwrapper)

2. Start the postgres database (Unix):

        $ postgres -D /usr/local/var/postgres/ & (Unix, if not running on startup)
        $ export DATABASE_URL=postgres:///$(whoami) (Unix) or set DATABASE_URL=%USERNAME% (Windows)

3. Run the app

        $ heroku local web (Unix) or python run.py (Windows)


### Access the database

* Remote:

        $ heroku pg:psql --app _yourappname_

* Local:

        $ psql
