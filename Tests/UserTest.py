import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os

sys.path.append(os.path.dirname(sys.path[0] + "\Pages"))
from Pages.LeaguePage import LeaguePage
from Pages.TeamPage import TeamPage
from Pages.UserPage import UserPage
from Pages.UserPage import UserPage
from EnvSetup.EnvironSetup import EnvironmentSetup


class UserTest(EnvironmentSetup):
    Team_1_name = "XYZ Team One"
    # Team_2_name = "qwe Team two"
    # Team_3_name = "qwe Team three"

    Team_1_analyst_first_name = "XYZ Team one"
    Team_1_analyst_last_name = "Analyst"
    Team_1_analyst_user_name = "XYZteamoneAnalyst"
    Team_1_analyst_email = "XYZteamoneAnalyst@mailinator.com"

    Team_1_coach_first_name = "XYZ Team one"
    Team_1_coach_last_name = "coach"
    Team_1_coach_user_name = "XYZteamonecoach"
    Team_1_coach_email = "XYZteamonecoach@mailinator.com"

    Team_1_asst_coach_first_name = "XYZ Team one"
    Team_1_asst_coach_last_name = "asst coach"
    Team_1_asst_coach_user_name = "XYZteamoneasstcoach"
    Team_1_asst_coach_email = "XYZteamoneasstcoach@gmail.com"

    Team_1_scout_first_name = "XYZ Team one"
    Team_1_scout_last_name = "scout"
    Team_1_scout_user_name = "XYZteamonescout"
    Team_1_scout_email = "XYZteamonescout@gmail.com"

    Team_1_player_1_first_name = "XYZ team one player"
    Team_1_player_1_last_name = "one"
    Team_1_player_1_user_name = "XYZoneplayer"
    Team_1_player_1_email = "XYZteamoneplayerone@mailinator.com"

    Team_1_player_2_first_name = "XYZ team one player"
    Team_1_player_2_last_name = "two"
    Team_1_player_2_user_name = "XYZtwoplayer"
    Team_1_player_2_email = "XYZteamoneplayertwo@mailinator.com"

    Team_1_player_3_first_name = "XYZ team one player"
    Team_1_player_3_last_name = "three"
    Team_1_player_3_user_name = "XYZthreeplayer"
    Team_1_player_3_email = "XYZteamoneplayerthree@mailinator.com"

###################################################################################

    user_types_league_admin = "League Administrator"
    user_types_team_admin = "Team Administrator"
    user_types_analyst = "Analyst"
    user_types_coach = "Coach"
    user_types_player = "Players"
    user_types_scout = "Scout"
    user_types_asst_coach = "Assistant Coach"

###################################################################################

    def test_a_add_analyst_1_and_select_team_1(self):
        driver = self.driver

        Analyst1 = LeaguePage(driver)
        Analyst = UserPage(driver)
        Analyst.click_user_tab()
        time.sleep(2)
        Analyst1.click_add_new_button()
        time.sleep(2)
        Analyst.enter_user_first_name(self.Team_1_analyst_first_name)
        Analyst.enter_user_last_name(self.Team_1_analyst_last_name)
        Analyst.enter_user_email_xpath(self.Team_1_analyst_email)
        Analyst.enter_user_username(self.Team_1_analyst_user_name)
        Analyst.select_user_type(self.user_types_analyst)
        time.sleep(4)
        Analyst.select_team(self.Team_1_name)
        time.sleep(2)
        Analyst1.click_add_submit_button()
        time.sleep(2)

    def test_b_add_coach_and_select_team_1(self):
        driver = self.driver

        Coach1 = LeaguePage(driver)
        Coach = UserPage(driver)
        Coach.click_user_tab()
        time.sleep(2)
        Coach1.click_add_new_button()
        time.sleep(2)
        Coach.enter_user_first_name(self.Team_1_coach_first_name)
        Coach.enter_user_last_name(self.Team_1_coach_last_name)
        Coach.enter_user_email_xpath(self.Team_1_coach_email)
        Coach.enter_user_username(self.Team_1_coach_user_name)
        Coach.select_user_type(self.user_types_coach)
        time.sleep(4)
        Coach.select_team(self.Team_1_name)
        time.sleep(2)
        Coach1.click_add_submit_button()
        time.sleep(2)

    def test_c_add_asst_coach_and_select_team_1(self):
        driver = self.driver

        Coach1 = LeaguePage(driver)
        Coach = UserPage(driver)
        Coach.click_user_tab()
        time.sleep(2)
        Coach1.click_add_new_button()
        time.sleep(2)
        Coach.enter_user_first_name(self.Team_1_asst_coach_first_name)
        Coach.enter_user_last_name(self.Team_1_asst_coach_last_name)
        Coach.enter_user_email_xpath(self.Team_1_asst_coach_email)
        Coach.enter_user_username(self.Team_1_asst_coach_user_name)
        Coach.select_user_type(self.user_types_asst_coach)
        time.sleep(4)
        Coach.select_team(self.Team_1_name)
        time.sleep(2)
        Coach1.click_add_submit_button()
        time.sleep(2)

    def test_d_add_scout_and_select_team_1(self):
        driver = self.driver
        Coach1 = LeaguePage(driver)
        Coach = UserPage(driver)
        Coach.click_user_tab()
        time.sleep(2)
        Coach1.click_add_new_button()
        time.sleep(2)
        Coach.enter_user_first_name(self.Team_1_scout_first_name)
        Coach.enter_user_last_name(self.Team_1_scout_last_name)
        Coach.enter_user_email_xpath(self.Team_1_scout_email)
        Coach.enter_user_username(self.Team_1_scout_user_name)
        Coach.select_user_type(self.user_types_scout)
        time.sleep(4)
        Coach.select_team(self.Team_1_name)
        time.sleep(2)
        Coach1.click_add_submit_button()
        time.sleep(2)


    def test_e_add_player_1_and_select_team_1(self):
        driver = self.driver

        Player1 = LeaguePage(driver)
        player = UserPage(driver)
        player.click_user_tab()
        time.sleep(2)
        Player1.click_add_new_button()
        time.sleep(2)
        player.enter_user_first_name(self.Team_1_player_1_first_name)
        player.enter_user_last_name(self.Team_1_player_1_last_name)
        player.enter_user_email_xpath(self.Team_1_player_1_email)
        player.enter_user_username(self.Team_1_player_1_user_name)
        player.select_user_type(self.user_types_player)
        time.sleep(4)
        player.select_team(self.Team_1_name)
        time.sleep(2)
        Player1.click_add_submit_button()
        time.sleep(2)

    def test_f_add_player_2_and_select_team_1(self):
        driver = self.driver

        Player2 = LeaguePage(driver)
        player = UserPage(driver)
        player.click_user_tab()
        time.sleep(2)
        Player2.click_add_new_button()
        time.sleep(2)
        player.enter_user_first_name(self.Team_1_player_2_first_name)
        player.enter_user_last_name(self.Team_1_player_2_last_name)
        player.enter_user_email_xpath(self.Team_1_player_2_email)
        player.enter_user_username(self.Team_1_player_2_user_name)
        player.select_user_type(self.user_types_player)
        time.sleep(4)
        player.select_team(self.Team_1_name)
        time.sleep(2)
        Player2.click_add_submit_button()
        time.sleep(2)

    def test_g_add_player_3_and_select_team_1(self):
        driver = self.driver

        Player3 = LeaguePage(driver)
        player = UserPage(driver)
        player.click_user_tab()
        time.sleep(2)
        Player3.click_add_new_button()
        time.sleep(2)
        player.enter_user_first_name(self.Team_1_player_3_first_name)
        player.enter_user_last_name(self.Team_1_player_3_last_name)
        player.enter_user_email_xpath(self.Team_1_player_3_email)
        player.enter_user_username(self.Team_1_player_3_user_name)
        player.select_user_type(self.user_types_player)
        time.sleep(4)
        player.select_team(self.Team_1_name)
        time.sleep(2)
        Player3.click_add_submit_button()
        time.sleep(2)




