import unittest
from user import User

class TestClass(unittest.TestCase):
    def test_init(self):
        self.assertEqual(self.newuser.user_name,"fridah")
        self.assertEqual(self.newuser.password,"1234567")


    def setUp(self):
        self.newuser =User("fridah","1234567")



    def test_save_user(self):
        self.newuser.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials =Credentials("acc_name","fridah","1234567")


    def tearDown(self):
        Credentials.user_credentials =[]

    def test_details(self):
        self.assertEqual(self.new_credentials.acc_name,"facebook")
        self.assertEqual(self.new_credentials.user_name,"fridah")
        self.assertEqual(self.new_credentials.password,"1234567")


    def test_save_credentials(self):

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)


    def find_credentials(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("acc_name","user_name","password")
        test_credential.save_credentials() 

        the_credential =Credentials.find_acc_name("acc_name")
        self.assertEqual(the_credential.acc_name,test_credential.acc_name)


    def test_exist(self):
        self.new_credentials.save_credentials()
        test_credential =Credentials("acc_name","user_name","password")
        test_credential.save_credentials()

        search_credential =Credentials.credentialsuser_exist("acc_name")
        self.assertTrue(search_credential)

    def delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credential =credentials("acc_name","user_name","password")
        test_credential.save_credentials()


        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials),1) 


    def test_savemany_acc_name(self):
        self.new_credentials.save_credentials()
        test_credential =Credentials("acc_name","user_name","password")
        test_credential.save_credentials()

        self.assertEqual(len(Credentials.user_credentials),2)       

if __name__ == '__main__':
    unittest.main()
