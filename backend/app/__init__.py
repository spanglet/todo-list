import os
from flask import Flask
from flask_cors import CORS

from .db_models import db

REINIT_DB = False

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS for frontend cross-origin requests
    # TODO transfer CORS to config file for switching between * URL and :::3000 (frontend)
    CORS(app, resources={r'/*': {'origins': 'http://127.0.0.1:3000',
        "supports_credentials": True}})

    # Config loaded from config.py
    # TODO make env vars switch between testing and dev configs
    app.config.from_pyfile("config.py")

    try:
        db.init_app(app)
        if REINIT_DB:
            db.drop_all(app=app)
            db.create_all(app=app) 
    except Exception as e: 
        print("Exception when initializing database\n")
        print(e)
        return

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints are registered to the app's root
    from . import auth
    app.register_blueprint(auth.bp)
    from . import tasks,lists
    app.register_blueprint(tasks.bp)
    app.register_blueprint(lists.bp)

    return app
