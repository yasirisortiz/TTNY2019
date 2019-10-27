#!/usr/bin/env python3
from Crypto.Hash import SHA256
from mongoengine import connect
from datetime import datetime
import random
import imp


models = imp.load_source("models.py", "../models/models.py")
settings = imp.load_source("settings.py", "../settings.py")

connect(settings.MONGO_HOST, host=settings.MONGO_URI)


class InitialUsers():
    # def __init__(self):
    #     self.users = models.Users

    def user_ins(self):
        # passwords file
        p = open("random_passwords.txt", "r").readlines()
        # username file
        u = open("random_names.txt", "r").readlines()

        emails = ["gmail.com", "ymail.com", "outlook.com"]
        user_types = ["Volunteer", "Recipient"]

        for i in range(len(u)):
            u[i] = u[i].replace("\r", "")
            u[i] = u[i].replace("\n", "")

            # combines the first and last name as the username
            uname = u[i].replace(" ", "").lower()

            fname = u[i].split(" ")[0]
            lname = u[i].split(" ")[1]

            # generate hash
            pwd = SHA256.new(p[i].encode("utf8"))
            hex = pwd.hexdigest()

            email = "@".join((uname, (emails[random.randint(0, len(emails)-1)])))
            zip = random.randint(10001, 10314)

            type = user_types[random.randint(0, len(user_types)-1)]

            # creates the Statistics document
            stats = models.Statistics(donated=0, received=0, delivered=0)

            # creates the Location document
            location = models.Location(state="NY", zip=zip)

            # creates the Users document
            user = models.Users(username=uname, fname=fname, lname=lname, email=email, password=hex, user_type=type, stats=stats, user_location=location)

            user.save()


    def events_ins(self):
        # Sample Org #1
        location1 = models.Location(street="15 Grumman Road West Suite 1450", city="Bethpage", state="NY", zip=11714)

        org1 = models.Organization(name="Feeding America", donation_type="Food Drive", location=location1)

        event1 = models.Events(organization=org1, type="Food Drive", date=(datetime.strptime("11/03/2019 08:30", "%m/%d/%Y %H:%M")), description="We will be giving out canned goods starting at 8:30 AM.")

        # saves and send to db
        event1.save()

        # Sample Org #2
        location2 = models.Location(street="355 Food Center Dr.", city="New York", state="NY", zip=10474)

        org2 = models.Organization(name="Food Bank for New York City", donation_type="Food Drive", location=location1, phonenumber=7189914300)

        event2 = models.Events(organization=org2, type="Food Drive", date=(datetime.strptime("11/12/2019 10:00", "%m/%d/%Y %H:%M")), description="We will be be providing those in need with resources to survive another week.")

        # saves and send to db
        event2.save()



if __name__ == '__main__':
    initial = InitialUsers()

    ''' Calling for the initial insertions onto the Users document '''
    # initial.user_ins()
    ''' Calling for the initial insertions onto the Events document '''
    # initial.events_ins()
