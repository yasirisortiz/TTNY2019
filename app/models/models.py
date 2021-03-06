# from app.extensions import mongo
from flask_mongoengine import MongoEngine

from mongoengine import Document, EmbeddedDocument, StringField, EmailField, ListField, BooleanField, EmbeddedDocumentField, ImageField, IntField, DateTimeField


db = MongoEngine()


DONATION_TYPE = ("Food Drive", "Clothing Drive", "Toiletree Drive", "School Supplies Drive", "Book Drive", "Other")
USER_TYPE = ("Volunteer", "Recipient", "Organization", "Guest")


class Organization(db.EmbeddedDocument):
    name = StringField(max_length=300)
    donation_type = StringField(choices=DONATION_TYPE, max_length=100)
    location = EmbeddedDocumentField("Location")
    phonenumber = IntField(max_length=10)
    

class Statistics(db.EmbeddedDocument):
    donated = IntField()
    received = IntField()
    delivered = IntField()


class Location(db.EmbeddedDocument):
    street = StringField(max_length=100)
    city = StringField(max_length=50)
    state = StringField(max_length=2)
    zip = IntField()


class Users(db.Document):
    username = StringField(max_length=50, required=True, unique=True)
    fname = StringField(max_length=30, required=True)
    lname = StringField(max_length=30, required=True)
    password = StringField(required=True)
    email = StringField(max_length=100, required=True, unique=True)
    user_type = StringField(choices=USER_TYPE, require=True)
    description = StringField(max_length=300)
    languages = ListField(StringField(), default=list)
    photo = ImageField()
    organization = EmbeddedDocumentField("Organization")
    stats = EmbeddedDocumentField("Statistics")
    user_location = EmbeddedDocumentField("Location")

    
class Events(db.Document):
    organization = EmbeddedDocumentField("Organization", required=True)
    type = StringField(choices=DONATION_TYPE, required=True)
    date = DateTimeField(required=True)
    description = StringField(required=True)
    flier = ImageField()


