import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage

class LoginTest(unittest.TestCase):

    # Replace Your Login Credentials
    baseURL = "http://159.65.142.31/agile-sports/beta/"
    correct_email = "superadmin@agile.com"
    correct_password = "Hi@agile"
    incorrect_email = "ssuperadmin@agile.com"
    incorrect_password = "Hi@agilee"

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get(inst.baseURL)
        time.sleep(1)

    # def test_1_Login_incorrect_password(self):
    #     driver = self.driver
    #     login = Loginpage(driver)
    #     login.enter_email(self.correct_email)
    #     login.enter_password(self.incorrect_password)
    #     time.sleep(3)
    #     login.click_login()
    #     login.Invalid_Credential_text()
    #
    # def test_2_Login_incorrect_email(self):
    #     driver = self.driver
    #     login = Loginpage(driver)
    #     time.sleep(1)
    #     login.enter_email(self.incorrect_email)
    #     login.enter_password(self.correct_password)
    #     time.sleep(3)
    #     login.click_login()
    #     login.Invalid_Credential_text()

    def test_3_Login_correct(self):
        driver = self.driver
        login = Loginpage(driver)
        time.sleep(1)
        login.enter_email(self.correct_email)
        login.enter_password(self.correct_password)
        login.click_login()
        time.sleep(1)
        login.valid_Credential_text()


    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()



