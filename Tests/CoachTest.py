import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage
from Pages.AnalystPage import AnalystPage
from Pages.CoachPage import CoachPage
from Pages.LeaguePage import LeaguePage


class CoachTest(unittest.TestCase):

# Replace Your Login Credentials

    baseURL = "http://159.65.142.31/agile-sports/beta/"
    correct_email = "xyzteamonecoach@mailinator.com"
    correct_password = "123456"
    agilityURL = "http://159.65.142.31/agile-sports/beta/landing/agility-card"
    surveyURL = "http://159.65.142.31/agile-sports/beta/landing/post-game-survey"
    sprintstrategyURL = "http://159.65.142.31/agile-sports/beta/landing/sprint-strategy"
    meetingnoteURL = "http://159.65.142.31/agile-sports/beta/landing/meeting-notes"

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

    def test_1_assign_cards_plan(self):
        driver = self.driver
        card = AnalystPage(driver)
        time.sleep(1)
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 1
        card.click_game_1()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        # coach
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 2
        card.click_game_2()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        # coach
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
















