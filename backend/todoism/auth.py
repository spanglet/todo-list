import functools

from flask import (
    Blueprint, abort, flash, g, redirect,
    render_template, request, session, url_for,
)  
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash

from todoism.db_models import db, User, List
from todoism.schema import UserSchema
from todoism.exceptions import APIError, LoginError


bp = Blueprint('auth', __name__, url_prefix='/auth')

# Initialize imported marshmallow schemas for validation
user_schema = UserSchema()

@bp.route('/register', methods=['POST', 'GET'])
def register():
    """Validate correct user registration data and insert user into db"""
    if request.method == 'GET':
        return {}, 200

    data = request.get_json()

    # Raises ValidationError if invalid request data for user
    new_user = user_schema.load(data)

    try:
        db.session.add(new_user)
        db.session.commit()

    except IntegrityError:
        raise APIError("Username is already taken")
        
    # Default 'Today' list is created for the new user
    main_list = List(
        name = "Today",
        description =  "Today's running tasks",
        userID = new_user.id
    )

    db.session.add(main_list)
    db.session.commit()

    return {"ok": True}, 200

@bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
       
        data = request.get_json()

        query = db.select(User).filter_by(username = data.get('username'))
        user = db.session.scalars(query).first()

        if (not user or 
                not check_password_hash(user.password, data.get('password'))):
            # Raised exception sent to errorhandler for post-request processing
            raise LoginError

        session.clear()
        session['user_id'] = user.id

        return {"ok": True}, 200

    else:

        session_active = True
        if g.user is None:
            session_active = False
        
        return {"sessionActive": session_active}, 200
        

@bp.before_app_request
def load_logged_in_user():
    '''Load user session if already logged in'''
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        query = db.select(User).filter_by(id = user_id)
        g.user = db.session.scalars(query).first()


def login_required(view):
    """Raise a 401 Authentication error if no user is logged in"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            abort(401)

        return view(**kwargs)

    return wrapped_view

@login_required
@bp.route('/logout')
def logout():
    """Remove user information from session"""
    session.clear()
    return {"ok": True}, 200
