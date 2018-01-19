class User:
    '''
    CLASS THAT GENERATES A NEW INSTANCE OF A USER/
    CREATES A NEW ACCOUNT
    '''
    user_list = []
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
        