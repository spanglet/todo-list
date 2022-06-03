import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #enable CORS for communcation to separated front-end
    # Limit CORS to specific devices for production
    CORS(app, resources={r'/*': {'origins': ''}})

    # Debugging enabled for dev setting
    #app.debug = True

    try:
        db = SQLAlchemy(app)

    
    except Exception as e: 
        print("Exception when trying to connect to the MySQL database\n")
        print(e.message)

    

    #app.config.from_mapping(
    #    SECRET_KEY='dev'
    #)

    """if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)"""

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints are registered to the app's root
    from . import auth,tasks,lists
    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)
    app.register_blueprint(lists.bp)

    # Initialize MySQL database
    from . import db
    db.db_init(reinit=False)

    return app
