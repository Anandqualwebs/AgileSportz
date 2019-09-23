import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage
from Pages.AnalystPage import AnalystPage
from Pages.PlayerPage import PlayerPage
from Pages.LeaguePage import LeaguePage


class PlayerTest(unittest.TestCase):

# Replace Your Login Credentials

    baseURL = "http://159.65.142.31/agile-sports/beta/"
    agilityURL = "http://159.65.142.31/agile-sports/beta/landing/agility-card"
    player_1_email = "xyzteamoneplayerone@mailinator.com"
    player_2_email = "xyzteamoneplayertwo@mailinator.com"
    player_3_email = "xyzteamoneplayerthree@mailinator.com"
    correct_password = "123456"

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(10)
        inst.driver.maximize_window()
        inst.driver.delete_all_cookies()
        inst.driver.get(inst.baseURL)
        time.sleep(1)


    def test_1_player_1_assign_cards_plan(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.player_1_email)
        login.enter_password(self.correct_password)
        login.click_login()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 1
        card.click_game_1()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 2
        card.click_game_2()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)

# Logout
        time.sleep(5)
        login.click_profile_icon()
        login.click_profile_icon()
        time.sleep(2)
        login.click_logout()
        time.sleep(2)
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)

    def test_1_player_2_assign_cards_plan(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.player_2_email)
        login.enter_password(self.correct_password)
        login.click_login()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 1
        card.click_game_1()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 2
        card.click_game_2()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)

# Logout
        time.sleep(5)
        login.click_profile_icon()
        login.click_profile_icon()
        time.sleep(2)
        login.click_logout()
        time.sleep(2)
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)

    def test_1_player_3_assign_cards_plan(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.player_3_email)
        login.enter_password(self.correct_password)
        login.click_login()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 1
        card.click_game_1()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
        # card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
# Match 2
        card.click_game_2()
        time.sleep(1)
        card.click_plan_tab()
        time.sleep(1)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)

# Logout
        time.sleep(5)
        login.click_profile_icon()
        login.click_profile_icon()
        time.sleep(2)
        login.click_logout()
        time.sleep(2)
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()
















