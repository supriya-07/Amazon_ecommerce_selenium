

#############################################################################################################

#Purpose of the script

#############################################################################################################

#1.This script has been designed to test the any Ecommerce Application(Amazon) by using selenium

#############################################################################################################

#Below points has been considered in the script:

#############################################################################################################

#1.Signup as a new user in paticular Ecommerce Application(Amazon).
#2.Then enter username, phoneno, password(it is readed from text file).
#3.After clicking on signup button. If username, password, phoneno has not been provided.
#4.Then filter out the string error and the corresponding color .
#5.Then compare obtained colors with a set of expected output colors and print success message and error message accordingly.
#6.Then sigin with valid emailid and valid password.
#7.Check system behavior when invalid email id and valid password is entered.
#8.Check system behavior when valid email id and invalid password is entered.
#9.Then check Forgot your password is working as expected or not.
#10.Check system behavior when "Keep me signed" is checked or not.
#11.Use loggers to print all the information on screen while executing and in log files

#############################################################################################################

#Importing Unittest and file
import unittest
import ecommerce_amazon
import logging

#############################################################################################################

#Instance of Amazon class is created
amazon_class = ecommerce_amazon.Amazon()

#############################################################################################################

#Create a class called TestAmazon that inherits from the TestCase class
class TestAmazon(unittest.TestCase):

    #Creating the logger
    logger = logging.getLogger(__name__)
    
    #Testing the get page by passing the URL
    def test_getpage(self):
        assert ecommerce_amazon.get_url() == "https://www.amazon.in/"
        self.logger.info("Test case passed successfully.Both URLS are same")
        
    #Testing the signup page    
    def test_signup(self):
        assert amazon_class.signup() == "mobileno already used", "account created successfully"
        self.logger.info("Already a user,testcase passed successfully")

    #Testing the corresponding color
    def test_validate_colour(self):
        assert amazon_class.validate_signupform() == "rgba(221, 0, 0, 1)"
        self.logger.info("Getting color and expected color both are same.Testcase passed successfully")

    #Testing signin by providing valid email and password
    def test_valid_email_passwrd(self):
        assert amazon_class.valid_email_password_signin() == "successfully signed"
        self.logger.info("successfully signed by providing valid email and password")

    #Testing signin by providing invalid emai id
    def test_invalid_email(self):
        assert amazon_class.invalid_email() == "We cannot find an account with that email address"
        self.logger.info("No account is found by passing invalid email id.Testcase passed successfully")

    #Testing singin by providing valid email id and invalid password
    def test_invalid_password(self):
        assert amazon_class.valid_mail_invalid_password() == "Your password is incorrect"
        self.logger.info("Password is incorrect by providing invalid password.Testcase passed successfully")
    
    #Testing Forgot password
    def test_forgot_password(self):
        assert amazon_class.forgot_password() == "priya123"
        self.logger.info("forgot password tested successfully")

    #Testing Keep me signed
    def test_keep_me_signed(self):
        assert amazon_class.keep_me_signed() == "keep me signed in successfully"
        self.logger.info("keep me signed successfully")

    #Closing the browser every testcase    
    def tearDown(self):
        amazon_class.close_driver()

#############################################################################################################

#Change the command-line entry point to call unittest.main()
if __name__ == '__main__':
    unittest.main()

logger.info("Execution ended here:")

############################### Script Details ##############################################################

# Script name               :       test_amazon.py
# Script version            :       1.0
# Prepared By               :       supriya.jakkamputi@infinite.com
# Create Date               :       15-JUNE-2021
# Last Modification Date    :       18-JUNE-2021

#############################################################################################################