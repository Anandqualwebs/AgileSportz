import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage
from Pages.LeagueAdminPage import LeagueAdminPage
from Pages.LeaguePage import LeaguePage

class LeagueAdminTest(unittest.TestCase):


    # Replace Your Login Credentials

    baseURL = "http://159.65.142.31/agile-sports/beta/"
    correct_email = "XYZteam1leagueadmin@mailinator.com	"
    correct_password = "123456"


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
        time.sleep(2)

    def test_1_add_match(self):
        driver = self.driver
        match = LeagueAdminPage(driver)
        matchh = LeaguePage(driver)
        time.sleep(2)
        match.click_match_tab()
        time.sleep(2)
        matchh.click_add_new_button()





    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()