import os

from flask import Flask, render_template
from . import settings, views, models
from flask_pymongo import PyMongo
from .extensions import mongo

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings)


    register_blueprints(app)
    register_errorhandlers(app)
    register_extensions(app)
    return app


def register_extensions(app):
    """Register Flask extensions."""
    mongo.init_app(app)
    mongo.retryWrites = False
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

app = create_app()
mongo =  PyMongo(app, uri=settings.MONGO_URI)
