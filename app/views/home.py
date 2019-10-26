from flask import Blueprint, render_template
import app

blueprint = Blueprint("home", __name__)

# index route
@blueprint.route("/")
def index():
	return render_template("home/index.html")
