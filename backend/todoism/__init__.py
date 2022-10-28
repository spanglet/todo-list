import os
from flask import Flask
from flask_cors import CORS

from todoism.db_models import db
from todoism.request_handlers import register_request_handlers


def create_app(testing=False):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Enable CORS for frontend cross-origin requests
    # TODO transfer CORS to config file for switching between * URL and :::3000 (frontend)
    CORS(app, resources={r'/*': {
        'origins': 'http://127.0.0.1:3000',
        "supports_credentials": True
    }})

    # Config loaded from config.py in instance folder
    app.config.from_pyfile("config.py", silent=True)

    if testing:
        # Update configuration for testing purposes
        app.config.from_pyfile("test_config.py", silent=True)

    with app.app_context():
        db.init_app(app)
        if testing:
            db.drop_all()
        db.create_all()

    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Blueprints are registered to the app's root
    from . import auth, tasks, lists, error_handlers
    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)
    app.register_blueprint(lists.bp)
    app.register_blueprint(error_handlers.bp)

    register_request_handlers(app)

    """ Global 404 (Page not Found) error handler"""
    @app.errorhandler(404)
    def _handle_bad_request(e):
        return 'This page was not found.',404

    return app
