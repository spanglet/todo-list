import os
from flask import Flask
from flask_cors import CORS

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #enable CORS for communcation to separated front-end
    CORS(app, resources={r'/*': {'origins': '*'}})


    # Debugging enabled for dev setting
    app.debug = True

    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    from . import auth,tasks
    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)

    from . import db
    db.db_init()
    

    return app
