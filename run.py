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

##Calling the Functions!!
def main():
    print("Hello!Welcome to the PasswordLocker application.To proceed,Use these short codes :ca - create an account using your own password,create an account using a randomly generated  password.")
    short_code = input().lower()
    if short_code == 'ca':
        print("Create an account using your own password")
        print("-"*10)

        print("First Name ")
        f_name = input()

        print("Last Name ")
        l_name = input()

        print("User Name ")
        u_name = input()

        print("Phone Number ")
        p_name = input()
        
        print("Email ")
        e_address = input()
        
        print("Password ")
        p_word = input()

if __name__ == '__main__':

    main()


