import functools

import mysql.connector
from .sql_util import connect_sql,insertRow

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')

host = "mysqldb"

#Returns a registration form to create an account
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Connect to docker container running mysql db
        db = connect_sql(host, "flax")
        cursor = db.cursor()

        # Password and Username are both required fields
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                cursor.execute(
                    "INSERT INTO users (username, password) VALUES (%s, %s)",
                    (username, generate_password_hash(password)),
                )
                    
                # When user is successfully created, a main list is created for them
                listData = {
                    "name": "Main",
                    "description": "Main task list"
                }
                insertRow(db, "lists", listData)
        
                db.commit()
            except mysql.connector.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        db = connect_sql(host, "flax")
        cursor = db.cursor(dictionary=True)

        cursor.execute(
            'SELECT * FROM users WHERE username = %s', (username,)
        )

        user = cursor.fetchone()

        error = None
        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return "log in successful",200

        flash(error)

    return render_template('auth/login.html')

#Load user session if already logged in
@bp.before_app_request
def load_logged_in_user():

    session.clear()

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = connect_sql(host, "flax")
        cursor = db.cursor(dictionary=True)
        g.user = cursor.execute(
            'SELECT * FROM users WHERE id = %s', (user_id,)
        ).fetchone()


# Remove user information from session
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
