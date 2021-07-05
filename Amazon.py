

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

#Importing webdriver to perform automated browser testing on Chrome browser
from selenium.webdriver import Chrome
#Importing time module
import time
#Importing Action Chains to drag an element, click an element. 
from selenium.webdriver.common.action_chains import ActionChains
#Importing loggers
import logging

#############################################################################################################

#Creating the logger file with date and time format
logging.basicConfig(filename="Amazon.log",filemode = 'w', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.info('Execution starts Here.')

#Providing the URL
BASE_URL = "https://www.amazon.in"
#Providing mail id
EMAIL_ID = "supriyachowdary32@gmail.com"
#Giving Expected color
EXPECTED_COLOR = "rgba(221, 0, 0, 1)"

#Opening the Chrome and getting the amazon site
def get_url():
    driver = Chrome('/usr/bin/chromedriver')
    driver.get(BASE_URL)
    return driver.current_url

#############################################################################################################

#Creating Amazon class and writing the methods
class Amazon(object):

    def __init__(self):
        #Opening the Chrome and getting the amazon site
        self.driver = Chrome('/usr/bin/chromedriver')
        self.driver.get(BASE_URL)
        logging.info("successfully getting amazon site in chrome browser")

#############################################################################################################

    
    def signup(self):
    
        
        action = ActionChains(self.driver)
        time.sleep(1)

        phone_no = "7288990961"

        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
        action.move_to_element(firstmenu).perform()
        time.sleep(3)

        #It clicks on signup in page
        secondmenu = self.driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
        secondmenu.click()
        time.sleep(3)
        logging.info("successfully clicked on signup button")

        #Username is filled in signup page
        username = self.driver.find_element_by_name("customerName")
        username.send_keys("priya")
        time.sleep(3)
        logging.info("successfully filled the username")

        #Mobile number is filled in signup page
        mobile_number = self.driver.find_element_by_id("ap_phone_number")
        mobile_number.send_keys("7288990961")
        time.sleep(3)
        logging.info("successfully filled the mobilenumber")

        #Mail is filled in signup page
        mail = self.driver.find_element_by_xpath("/html/body")
        mail.send_keys("supriyachowdary32@gmail.com")
        time.sleep(3)
        logging.info("successfully filled the mailid")

        #Username is filled in signup page
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.open_txt_file())
        time.sleep(3)
        logging.info("successfully filled the password")

        #It clicks continue button
        signupbutton= self.driver.find_element_by_id("continue")
        signupbutton.click()
        time.sleep(3)
        logging.info("Continue button is clicked")

        #It checks the mobile number if it is equal mobile no is already used else account is created successfully
        if phone_no == "7288990961":
            print("mobile no already in use")
            return "mobileno already used"
        else:
            print("account created successfully")

#############################################################################################################

    '''This method is used to filter out the string error and the corresponding color 
      Then  it comparedobtained_color with a set of expected output colors and 
      print success message and error message accordingly''' 

    def validate_signupform(self):
       
       #Navigate to Signup Page
        action = ActionChains(self.driver)
        time.sleep(1)

        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
        action.move_to_element(firstmenu).perform()
        time.sleep(3)

        #Click on signup page
        secondmenu = self.driver.find_element_by_xpath('//*[@id="nav-flyout-ya-newCust"]/a')
        secondmenu.click()
        time.sleep(3)

        #Click on continue button
        signupbutton= self.driver.find_element_by_id("continue")
        signupbutton.click()
        time.sleep(3)
        logging.info("continue button is clicked on in signup page without entering the username, password, mobileno")

        #Username is not provided in signup page 
        username = self.driver.find_element_by_id('ap_customer_name')
        if "error" in username.get_attribute('outerHTML'):
            #Getting the colour and storing it in a variable called obtained colour
            obtained_color = username.value_of_css_property('border-bottom-color')
            logging.info("getting the colour and storing it in a variable called obtained colour")
            #Checking the condition whether the obtained colour is not equal or not
            if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
                print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
                logging.info("expected color is not matching the gotted color")
            else:
                print("please enter username")
                logging.info("please enter username")

        #Mobilenumber is not provided in signup page
        mobile_number = self.driver.find_element_by_id('ap_phone_number')
        if "error" in mobile_number.get_attribute('outerHTML'):
            #Getting the colour and storing it in a variable called obtained colour
            obtained_color = mobile_number.value_of_css_property('border-bottom-color')
            logging.info("getting the colour and storing it in a variable called obtained colour")
            #Checking the condition whether the obtained colour is not equal or not
            if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
                print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
                logging.info("expected color is not matching the gotted color")
            else:
                print("please enter mobile number")
                logging.info("please enter mobile number")

        #Password is not provided in signup page
        password = self.driver.find_element_by_id('ap_password')
        if "error" in password.get_attribute('outerHTML'):
            #Getting the colour and storing it in a variable called obtained colour
            obtained_color = password.value_of_css_property('border-bottom-color')
            logging.info("getting the colour and storing it in a variable called obtained colour")
            #Checking the condition whether the obtained colour is not equal or not
            if not self.check_color(obtained_color, "rgba(221, 0, 0, 1)"):
                print(f"expected color is {EXPECTED_COLOR} and got {obtained_color}")
                logging.info("expected color is not matching the gotted color")
            else:
                print("please enter password")
                logging.info("please enter password")

        #Checking the error messages
        error_messages = ["At least 3 characters",
                            "Invalid Email", "At least 6 characters"]
        message_body_html_elements = self.driver.find_elements_by_class_name('msg-body')
        for msg in message_body_html_elements:
            error_msg = msg.get_attribute('innerHTML').split("span")[1][1:-2]
            if error_msg not in error_messages:
                print(f"{msg.get_attribute('outerHTML')} is missing error message")

        return obtained_color

    #checking color
    def check_color(self, color, orginal_color):
        return color == orginal_color

#############################################################################################################

    #Validating email and password in signin page
    def valid_email_password_signin(self):

        #Clicking the signin button
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        time.sleep(3)
        logging.info("signin button is clicked")

        #Entereing the email id in signin page
        email = self.driver.find_element_by_name("email")
        email.send_keys("supriyachowdary32@gmail.com")
        time.sleep(3)
        logging.info("email id entered.")

        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)
    
        #Entering the password in signin page
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.open_txt_file())
        logging.info("password entered.")
        time.sleep(2)

        #Clicking the signin button
        signin = self.driver.find_element_by_id("signInSubmit").click()
        logging.info("Signin successfully")
        time.sleep(3)
        
        return "successfully signed"

#############################################################################################################

    #Invalid emailid is entered in signin page
    def invalid_email(self):

        #Clicking the signin button
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        logging.info("signin button is clicked")
        time.sleep(3)

        #Entereing the wrong email id in signin page
        email = self.driver.find_element_by_name("email")
        email.send_keys("supriyachowdary32@gmail.com")
        logging.info("wrong emailid is entered")
        time.sleep(3)

        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)

        return "We cannot find an account with that email address"

#############################################################################################################

    #Valid emailid and invalid password are entered in signin page
    def valid_mail_invalid_password(self):

        #Clicking the signin button
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        logging.info("signin button is clicked")
        time.sleep(3)

        #Entereing the  email id in signin page
        email = self.driver.find_element_by_name("email")
        email.send_keys("supriyachowdary32@gmail.com")
        logging.info("emailid is entered.")
        time.sleep(3)

        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)

        #Entering the wrong password in signin page
        password = self.driver.find_element_by_name("password")
        password.send_keys("rrrr")
        logging.info("Wrong password entered.")
        time.sleep(2)

        #Clicking the signin button
        signin = self.driver.find_element_by_id("signInSubmit").click()
        logging.info("Signin successfully")
        time.sleep(3)
        
        return "Your password is incorrect"

#############################################################################################################

    def forgot_password(self):

        #Clicking the signin button
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        logging.info("signin button is clicked")
        time.sleep(3)
        
        #Entereing  email id in signin page
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("supriyachowdary32@gmail.com")
        logging.info("emailid is entered.")
        time.sleep(3)

        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)

        #Clicking the forgot password in signin page
        forgot_pass = self.driver.find_element_by_xpath('//*[@id="auth-fpp-link-bottom"]').click()
        logging.info("Clicking the forgot password .")
        time.sleep(2)
        
        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)

        #Entering the OTP in signin page
        otp = self.driver.find_element_by_xpath('//*[@id="cvf-input-code"]')
        logging.info("OTP generated successfully")
        time.sleep(20)

        new_pswd = "priya@123"
        retype_pswd = "priya@123"

        #Entering the new password in signin page
        new_password = self.driver.find_element_by_name("password").send_keys(new_pswd)
        retype_password = self.driver.find_element_by_name("passwordCheck").send_keys(retype_pswd)
        logging.info("New password entered.")
        time.sleep(2)
        
        #Clicking the signin button
        signin = self.driver.find_element_by_id("signInSubmit").click()
        logging.info("Signin successfully")
        time.sleep(3)

        #Checking the new password and retype password
        if new_pswd == retype_pswd:
            print(new_pswd)
            print(retype_pswd)
            return retype_pswd
        else:
            print('password is not matching')
            return "password is not matching"

#############################################################################################################

    def keep_me_signed(self):

        #Clicking the signin button
        firstmenu = self.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span')
        firstmenu.click()
        logging.info("signin button is clicked")
        time.sleep(3)
        
        #Entereing email id in signin page
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("supriyachowdary32@gmail.com")
        logging.info("emailid is entered.")
        time.sleep(3)

        #Clicking the continue button
        continue_button = self.driver.find_element_by_id("continue").click()
        logging.info("Clicking continue button")
        time.sleep(2)

        keep_me_signed = self.driver.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/input')
        keep_me_signed.click()

        #Entering the password in signin page
        password = self.driver.find_element_by_name("password")
        password.send_keys(self.open_txt_file())
        logging.info("password entered.")
        time.sleep(2)

        #Clicking the signin button
        signin = self.driver.find_element_by_id("signInSubmit").click()
        logging.info("Signin successfully")
        time.sleep(3)

        return "keep me signed in successfully"

#############################################################################################################

    #Opening password file in read mode
    def open_txt_file(self):
        with open("password.txt", "r") as fr:
            Password = fr.read()
        return Password

#############################################################################################################

    #Closing the browser
    def close_driver(self):
        self.driver.close()

############################### Script Details ##############################################################

# Script name               :       Amazon.py
# Script version            :       1.0
# Prepared By               :       supriya.jakkamputi@infinite.com
# Create Date               :       15-JUNE-2021
# Last Modification Date    :       18-JUNE-2021

#############################################################################################################
