#!/usr/bin/env python3
from Crypto.Hash import SHA256
from mongoengine import connect
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

        for i in range(len(u)):
            u[i] = u[i].replace("\r", "")
            u[i] = u[i].replace("\n", "")

            # combines the first and last name as the username
            uname = u[i].replace(" ", "").lower()

            fname = u[i].split(" ")[0]
            lname = u[i].split(" ")[1]

            # print(uname)

            # generate hash
            pwd = SHA256.new(p[i].encode("utf8"))
            hex = pwd.hexdigest()

            #print(hex)

            email = "@".join((uname, (emails[random.randint(0, len(emails)-1)])))
            # email = "{}@{}".format(uname, (emails[random.randint(0, len(emails)-1)]))
            zip = random.randint(10001, 10314)

            # creates the Statistics document
            stats = models.Statistics(donated=0, received=0, delivered=0)

            # creates the Location document
            location = models.Location(state="NY", zip=zip)

            # print(email.replace(" ", ""))

            # creates the Users document
            user = models.Users(username=uname, fname=fname, lname=lname, email=email, volunteer=True, stats=stats, user_location=location)

            # print(user.email)
            user.save()


if __name__ == '__main__':
    initial = InitialUsers()
    initial.user_ins()
