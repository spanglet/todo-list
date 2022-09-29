import functools
from uuid import uuid4

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from .db_models import db, User, List
from .schema import UserSchema
from .response import DataSchema, DataResponse

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    """Validate correct user registration data and insert user into db"""
    data = request.get_json()

    # Throws ValidationError if invalid request data for user
    UserSchema().load(data)

    user_id = uuid4().bytes

    # Create user via MySQL-Alchemy models
    new_user = User(
        id = user_id,
        username = data["username"],
        password = generate_password_hash(data["password"])
    )
    db.session.add(new_user)
    db.session.commit()
        
    # When user is successfully created, a main list is created for them
    main_list = List(
        name = "Main",
        description =  "Main list",
        userID = user_id
    )
    db.session.add(main_list)
    db.session.commit()

    return "User was successfully registered",200

@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':

        data = request.get_json()
        UserSchema().load(data)

        user = User.query.filter_by(username = data["username"]).first()

        if user is None:
            return {"OK": False}, 200

        if not check_password_hash(user.password, data["password"]):
            return {"OK": False}, 200

        session.clear()
        session['user_id'] = user.id

        return {"OK": True}, 200

    if request.method == 'GET':

        if g.user:
            return {"activeSession": True},200
        
        return {"activeSession": False}, 200
        

#Load user session if already logged in
@bp.before_app_request
def load_logged_in_user():

    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        #breakpoint()
        g.user = User.query.filter_by(id = user_id)

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return "login required", 400

        return view(**kwargs)

    return wrapped_view

# Remove user information from session
@login_required
@bp.route('/logout')
def logout():
    session.clear()
    return "Logout successful", 200

