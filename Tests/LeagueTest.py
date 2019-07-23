import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LeaguePage import LeaguePage
from EnvSetup.EnvironSetup import EnvironmentSetup


class LeagueTest(EnvironmentSetup):
    league_name = "XYZ League"
    league_location = "India"



    def test_1_add_league(self):
        driver = self.driver

        League = LeaguePage(driver)
        League.click_league_tab()
        time.sleep(2)
        League.click_add_new_button()
        League.enter_league_name(self.league_name)
        League.enter_league_location(self.league_location)
        League.click_add_submit_button()
        time.sleep(2)

    # def test_2_print_league_names(self):
    #     driver = self.driver
    #     League = LeaguePage(driver)
    #     League.click_league_tab()
    #     time.sleep(2)
    #     League.print_league_names()
    #
    # def test_3_print_league_admin_names(self):
    #     driver = self.driver
    #     League = LeaguePage(driver)
    #     League.click_league_tab()
    #     time.sleep(2)
    #     League.print_league_admin_names()
    #
    # def test_4_print_league_team_number(self):
    #     driver = self.driver
    #     League = LeaguePage(driver)
    #     League.click_league_tab()
    #     time.sleep(2)
    #     League.print_league_team_number()
    #
    # def test_5_print_league_number_of_games(self):
    #     driver = self.driver
    #     League = LeaguePage(driver)
    #     League.click_league_tab()
    #     time.sleep(2)
    #     League.print_number_of_games()






