from flask_pymongo import PyMongo
from . import app

mongo = PyMongo(app)
