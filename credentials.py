import string
import secrets
import random
import pyperclip
class Credentials:
    '''
    CLASS THAT GENERATES A NEW INSTANCE OF A USER/
    CREATES A NEW ACCOUNT
    '''
    credential_list = []
    def __init__(self,app_name,account_name,account_password):
        '''
        initialises a new instance of a credential
        '''
        self.app_name = app_name
        self.account_name = account_name
        self.account_password= account_password
    def save_newcredential(self):
        Credentials.credential_list.append(self)
    def deletecredential(self):
        '''
        delete a credential from credential list
        '''
        Credentials.credential_list.remove(self)
    
    @classmethod
    def find_credentialbyappname(cls,name):
            '''Method that takes in appname and returns a credential
            that matches that appname.
            Args:
            appname TO SEARCH FOR 
            Returns :
            credentials of person that matches that appname.
            '''
            for credentials in cls.credential_list:
                if credentials.app_name == name:
                    return credentials
    @classmethod
    def credential_exist(cls,appname):
        '''
        method that checks if  a credential
         exists that uses appname and returns a boolean
         '''
        for Credentials in cls.credential_list:
            if Credentials.app_name == appname:
                return True
        return False
    @classmethod
    def display_allcredentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credential_list
    @classmethod

    # def generate_randompass():
    #     '''method to generate a random password
    #     which should have an uppercase letter,lowercase,digit 
    #     and punctuation mark
    #     password length=8 letters
    #     '''
    #     #password should contain a capital letter,small letter,digit and a punctuation
    #     characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    #     #length of the password
    #     passlength = random.randint(8,16)
    #     #randomly joins the characters
    #     pass_word = ''.join(secrets.choice(characters) for x in range(passlength))
    #     ##return or print the generated password
    #     return pass_word
