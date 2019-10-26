from flask_pymongo import PyMongo
from . import settings

mongo =  PyMongo(uri=settings.MONGO_URI, retryWrites=False)
