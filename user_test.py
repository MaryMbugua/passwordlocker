import unittest ##import unittest module
from user import User ##import user class from user.py file

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test case
        '''
        self.new_user = User("pythonuser","lovepy") #create user object

    def test_init(self):
        '''
        to test if object is initialised properly
        '''
        self.assertEqual(self.new_user.user_name,"pythonuser")
        self.assertEqual(self.new_user.password,"lovepy")
    def test_savenewuser(self):
        #to test if user object is saved into users list
        self.new_user.savenewuser()
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()

    
