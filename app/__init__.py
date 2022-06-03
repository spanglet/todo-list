import os
from flask import Flask
from flask_cors import CORS
from .db_models import db

REINIT_DB = True

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS for frontend cross-origin requests
    CORS(app, resources={r'/*': {'origins': '127.0.0.1:300'}})

    # Config loaded from config.py
    # TODO make env vars switch between testing and dev configs
    app.config.from_object('config.Config')

    try:
        db.init_app(app)
        if REINIT_DB:
            db.drop_all()
            db.create_all() 
    except Exception as e: 
        print("Exception when initializing database\n")
        print(e.message)
        return

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

    return app
