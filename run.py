#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

##creating a user
def create_user(fname,lname,uname,phone,email,passw):
    new_user = User(fname,lname,uname,phone,email,passw)
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
    print("Hello!Welcome to the PasswordLocker application.To proceed,Use these short codes :ca - create an account using your own password,ra - create an account using a randomly generated  password,ex - exit the application")
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
        p_number = input()
        
        print("Email ")
        e_address = input()
        
        print("Password ")
        p_word = input()

                    ##create and save a new account
        save_user(create_user(f_name,l_name,u_name,p_number,e_address,p_word))
        print('\n')
        print(f"New Account {u_name} created")
        print('\n')
        print("To login use the short code :lg - login into account ,ex - to exit the application")
        short_codetwo = input().lower()
        if short_codetwo == 'lg':
            print("-"*10)
            print("LogIn")
            print("-"*10)
            print("To log in, input your username and password")

            print("UserName")
            user_namein = input()
                 
            print("Password")
            pass_wordin = input()
            ###verifying the username and password
            if user_namein == u_name and pass_wordin == p_word:
                print("Correct username and password.To proceed use the following shortcodes:cc - create a new credential ,dc - display credentials ,fc - find a credential by inputtiing the appname ,ex - exit the application")

            
        # elif short_codetwo == 'ex':
        #     print("Bye Bye!")
        # break
        else:
            print("I really didn't get that.Please use the short codes")


    elif short_code == 'ra':
        print("Create an account using a randomly generated password")
        print("-"*10)

        print("First Name ")
        f_name = input()

        print("Last Name ")
        l_name = input()

        print("User Name ")
        u_name = input()

        print("Phone Number ")
        p_number = input()
        
        print("Email ")
        e_address = input()
    # elif short_code == "ex":
    #     print("Bye Bye!")
    # break
    else:
        print("I really didn't get that.Please use the short codes")
       
        

if __name__ == '__main__':

    main()





