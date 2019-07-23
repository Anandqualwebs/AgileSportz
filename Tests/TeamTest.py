import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.TeamPage import TeamPage
from Pages.LeaguePage import LeaguePage
from Pages.UserPage import UserPage
from EnvSetup.EnvironSetup import EnvironmentSetup


class TestTeam(EnvironmentSetup):
    league_name = "XYZ League"

    Team_1_name = "XYZ Team One"
    Team_1_location = "India"

    team_1_team_admin_first_name = "XYZ Team one"
    team_1_team_admin_last_name = "Team Admin"
    team_1_team_admin_email = "XYZleagueteam1teamadmin@mailinator.com"
    team_1_team_admin_user_name = "XYZleagueteam1teamadmin"

    team_1_league_admin_first_name = "XYZ Team one"
    team_1_league_admin_last_name = "league Admin"
    team_1_league_admin_email = "XYZteam1leagueadmin@mailinator.com"
    team_1_league_admin_user_name = "XYZteam1leagueadmin"

    Team_2_name = "XYZ Team two"
    Team_2_location = "India"

    team_2_team_admin_first_name = "XYZ Team two"
    team_2_team_admin_last_name = "Team Admin"
    team_2_team_admin_email = "XYZleagueteam2teamadmin@mailinator.com"
    team_2_team_admin_user_name = "XYZleagueteam2teamadmin"

    team_2_league_admin_first_name = "XYZ Team two"
    team_2_league_admin_last_name = "league Admin"
    team_2_league_admin_email = "XYZteam2leagueadmin@mailinator.com"
    team_2_league_admin_user_name = "XYZteam2leagueadmin"

    Team_3_name = "XYZ Team three"
    Team_3_location = "India"

    team_3_team_admin_first_name = "XYZ Team three"
    team_3_team_admin_last_name = "Team Admin"
    team_3_team_admin_email = "XYZleagueteam3teamadmin@mailinator.com"
    team_3_team_admin_user_name = "XYZleagueteam3teamadmin"

    team_3_league_admin_first_name = "XYZ Team three"
    team_3_league_admin_last_name = "league Admin"
    team_3_league_admin_email = "XYZteam3leagueadmin@mailinator.com"
    team_3_league_admin_user_name = "XYZteam3leagueadmin"

    founded_year_index = 2
    sub_domain_1 = "Abc"
    sub_domain_2 = "def"
    sub_domain_3 = "igh"

    #
    # def test_1_add_Team_1_and_admin_league_admin(self):
    #     driver = self.driver
    #
    #     Team = TeamPage(driver)
    #     Team1 = LeaguePage(driver)
    #     Team11 = UserPage(driver)
    #     Team.click_team_tab()
    #     time.sleep(2)
    #     Team1.click_add_new_button()
    #     time.sleep(2)
    #     Team11.select_league(self.league_name)
    #     Team.enter_team_name(self.Team_1_name)
    #     Team.enter_team_location(self.Team_1_location)
    #     Team.select_founded_year(self.founded_year_index)
    #     Team.enter_sub_domain(self.sub_domain_1)
    #     Team.click_add_new_team_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_team_admin_first_name(self.team_1_team_admin_first_name)
    #     Team.enter_new_team_admin_last_name(self.team_1_team_admin_last_name)
    #     Team.enter_new_team_admin_email_xpath(self.team_1_team_admin_email)
    #     Team.enter_new_team_admin_user_name(self.team_1_team_admin_user_name)
    #     Team.click_add_new_league_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_league_admin_first_name(self.team_1_league_admin_first_name)
    #     Team.enter_new_league_admin_last_name(self.team_1_league_admin_last_name)
    #     Team.enter_new_league_admin_email_xpath(self.team_1_league_admin_email)
    #     Team.enter_new_league_admin_user_name(self.team_1_league_admin_user_name)
    #     Team1.click_add_submit_button()
    #     time.sleep(2)
    #
    # def test_2_add_Team_2_and_admin_league_admin(self):
    #     driver = self.driver
    #
    #     Team = TeamPage(driver)
    #     Team1 = LeaguePage(driver)
    #     Team11 = UserPage(driver)
    #     Team.click_team_tab()
    #     time.sleep(2)
    #     Team1.click_add_new_button()
    #     time.sleep(1)
    #     driver.refresh()
    #     time.sleep(2)
    #     Team11.select_league(self.league_name)
    #     Team.enter_team_name(self.Team_2_name)
    #     Team.enter_team_location(self.Team_2_location)
    #     Team.select_founded_year(self.founded_year_index)
    #     Team.enter_sub_domain(self.sub_domain_2)
    #     Team.click_add_new_team_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_team_admin_first_name(self.team_2_team_admin_first_name)
    #     Team.enter_new_team_admin_last_name(self.team_2_team_admin_last_name)
    #     Team.enter_new_team_admin_email_xpath(self.team_2_team_admin_email)
    #     Team.enter_new_team_admin_user_name(self.team_2_team_admin_user_name)
    #     Team.click_add_new_league_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_league_admin_first_name(self.team_2_league_admin_first_name)
    #     Team.enter_new_league_admin_last_name(self.team_2_league_admin_last_name)
    #     Team.enter_new_league_admin_email_xpath(self.team_2_league_admin_email)
    #     Team.enter_new_league_admin_user_name(self.team_2_league_admin_user_name)
    #     Team1.click_add_submit_button()
    #     time.sleep(2)
    #
    # def test_3_add_Team_3_and_admin_league_admin(self):
    #     driver = self.driver
    #
    #     Team = TeamPage(driver)
    #     Team1 = LeaguePage(driver)
    #     Team11 = UserPage(driver)
    #     Team.click_team_tab()
    #     time.sleep(2)
    #     Team1.click_add_new_button()
    #     time.sleep(1)
    #     driver.refresh()
    #     time.sleep(2)
    #     Team11.select_league(self.league_name)
    #     Team.enter_team_name(self.Team_3_name)
    #     Team.enter_team_location(self.Team_3_location)
    #     Team.select_founded_year(self.founded_year_index)
    #     Team.enter_sub_domain(self.sub_domain_3)
    #     Team.click_add_new_team_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_team_admin_first_name(self.team_3_team_admin_first_name)
    #     Team.enter_new_team_admin_last_name(self.team_3_team_admin_last_name)
    #     Team.enter_new_team_admin_email_xpath(self.team_3_team_admin_email)
    #     Team.enter_new_team_admin_user_name(self.team_3_team_admin_user_name)
    #     Team.click_add_new_league_admin_checkbox()
    #     time.sleep(2)
    #     Team.enter_new_league_admin_first_name(self.team_3_league_admin_first_name)
    #     Team.enter_new_league_admin_last_name(self.team_3_league_admin_last_name)
    #     Team.enter_new_league_admin_email_xpath(self.team_3_league_admin_email)
    #     Team.enter_new_league_admin_user_name(self.team_3_league_admin_user_name)
    #     Team1.click_add_submit_button()
    #     time.sleep(2)









    def test_2_print_team_names(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_names()

    def test_4_print_team_admin_names(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_admin_names()

    def test_5_print_team_founded_year(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_founded_year()

    def test_6_print_team_league_names(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_league_names()

    def test_7_print_team_locations(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_locations()

    def test_8_print_team_number_of_games(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_number_of_games()

    def test_9_print_team_sprints(self):
        driver = self.driver
        Team = TeamPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team.print_team_sprints()
