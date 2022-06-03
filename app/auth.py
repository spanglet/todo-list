import functools
import mysql.connector
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from uuid import uuid4

from .db_models import db, User, List
#from .sql_util import connect_sql,insertRow


bp = Blueprint('auth', __name__, url_prefix='/auth')

host = "mysqldb"

#Returns a registration form to create an account
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
        
        # Password and Username are both required fields
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                user_id = uuid4().bytes,

                # Create user via MySQL-Alchemy models
                new_user = User(
                        id = user_id
                        username = username,
                        password = generate_password_hash(password))
                db.session.add(new_user)
                db.session.commit()
                    
                # When user is successfully created, a main list is created for them
                main_list = List(
                    name = "Main",
                    description =  "Main list",
                    userID = user_id)
                db.session.add(main_list)
                db.session.commit()

            except IntegrityError:
                return "Username already exists",200
        
            except SQLError as e:
                print ("SQL error when adding user:\n")
                print(e)
            else:
                return "User was successfully registered",200

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
