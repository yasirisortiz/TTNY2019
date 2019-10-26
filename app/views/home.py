from flask import Blueprint, render_template
from ..extensions import mongo
import os


blueprint = Blueprint("home", __name__)

# index route
@blueprint.route("/")
def index():
	print(mongo.db)
	user_collection = mongo.db.TTNY
	user_collection.insert_one({"name" : "Test Usersssssssssssssss"})
	user_collection.insert_one({"name" : "ERSGGS"})

	return render_template("home/index.html")
