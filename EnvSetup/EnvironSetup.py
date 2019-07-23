import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage

class EnvironmentSetup(unittest.TestCase):

    #Replace Your Login Credentials
    baseURL = "http://159.65.142.31/agile-sports/beta/"
    correct_email = "superadmin@agile.com"
    correct_password = "Hi@agile"

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(10)
        inst.driver.maximize_window()
        inst.driver.delete_all_cookies()
        inst.driver.get(inst.baseURL)
        time.sleep(1)
        login = Loginpage(inst.driver)
        login.enter_email(inst.correct_email)
        login.enter_password(inst.correct_password)
        login.click_login()
        time.sleep(1)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == "__main__":
    unittest.main()