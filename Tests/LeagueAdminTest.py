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
    GameURL = "http://159.65.142.31/agile-sports/beta/landing/view-match"
    correct_email = "XYZleagueteam1teamadmin@mailinator.com"
    correct_password = "123456"
    opponent1 = 1
    opponent2 = 2
    opponent3 = 3
    match_location = "Usa"
    match_1_date = "8/25/2019"
    match_2_date = "8/26/2019"
    match_time = "03:00"

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


    def test_1_add_match_1(self):
        driver = self.driver
        match = LeagueAdminPage(driver)
        matchh = LeaguePage(driver)
        time.sleep(2)
        self.driver.get(self.GameURL)
        #match.click_game_tab()
        time.sleep(2)
        matchh.click_add_new_button()
        time.sleep(2)
        match.select_match_opponent(self.opponent1)
        match.enter_match_location(self.match_location)
        match.enter_date_location(self.match_1_date)
        match.enter_time_location(self.match_time)
        matchh.click_add_submit_button()
        time.sleep(2)

    def test_1_add_match_2(self):
        driver = self.driver
        match = LeagueAdminPage(driver)
        matchh = LeaguePage(driver)
        time.sleep(2)
        self.driver.get(self.GameURL)
#        match.click_game_tab()
        time.sleep(2)
        matchh.click_add_new_button()
        time.sleep(2)
        match.select_match_opponent(self.opponent2)
        match.enter_match_location(self.match_location)
        match.enter_date_location(self.match_2_date)
        match.enter_time_location(self.match_time)
        matchh.click_add_submit_button()
        time.sleep(2)



    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()