import os
import config

from flask import Flask, render_template
from . import settings, views, models
from flask_pymongo import PyMongo
# from .extensions import mongo


project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    app.config["MONGO_URI"] = config.MONGO_URI
    # app.config['MONGO_DBNAME'] = config.MONGO_DBNAME
    mongo = PyMongo(app)
    db = mongo.db

    # register_extensions(app, mongo)
    register_blueprints(app)
    register_errorhandlers(app)
    return app

def register_extensions(app, mongo):
    """Register Flask extensions."""
    mongo.db.init_app(app)
    # client = PyMongo.MongoClient(confid.MONGO_URI)

    with app.app_context():
        mongo.db.create_all()
    return None

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(views.home.blueprint)
    app.register_blueprint(views.auth.blueprint)
    return None

def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return render_template('401.html')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html')

    return None
