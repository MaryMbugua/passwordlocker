#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

##creating a user
def create_user(fname,lname,uname,phone,email,passw):
    new_user = User(fname,lname,phone,email)
    return new_user
##save users
def save_user(user):
    user.save_user()
#displaying all users
def display_allusers():
    return User.display_allusers()
#generate a random password
def generate_randompass():
    return User.generate_randompass()
