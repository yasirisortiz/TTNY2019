from flask import Blueprint, render_template
from ..models import models
import os

blueprint = Blueprint("home", __name__)

# index route
@blueprint.route("/")
def index():
	users = models.Users.objects.all()

	return render_template("home/index.html")

# home route
@blueprint.route("/home")
def home():
	return render_template("home/home.html")
