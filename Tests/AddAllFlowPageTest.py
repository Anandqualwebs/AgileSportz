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


# This Will Add

# 1 leagues
# 3 Teams
# 3 League Admin  (1/1/1 Per Team)
# 3 Team Admins   (1/1/1 Per Team)
# 1 Analyst       (1 in Team 1)
# 1 Coach         (1 in Team 1)
# 1 Asst Coach    (1 in Team 1)
# 1 scout         (1 in Team 1)
# 3 player        (3 in Team 1)


class AddAllFlowTest(EnvironmentSetup):
    league_name = "jkl League"
    league_location = "India"

########## Teams & Team Admins & League Admins ############################

    Team_1_name = "jkl Team One"
    Team_1_location = "India"

    team_1_team_admin_first_name = "jkl Team one"
    team_1_team_admin_last_name = "Team Admin"
    team_1_team_admin_email = "jklleagueteam1teamadmin@mailinator.com"
    team_1_team_admin_user_name = "jklleagueteam1teamadmin"

    team_1_league_admin_first_name = "jkl Team one"
    team_1_league_admin_last_name = "league Admin"
    team_1_league_admin_email = "jklteam1leagueadmin@mailinator.com"
    team_1_league_admin_user_name = "jklteam1leagueadmin"

    Team_2_name = "jkl Team two"
    Team_2_location = "India"

    team_2_team_admin_first_name = "jkl Team two"
    team_2_team_admin_last_name = "Team Admin"
    team_2_team_admin_email = "jklleagueteam2teamadmin@mailinator.com"
    team_2_team_admin_user_name = "jklleagueteam2teamadmin"

    team_2_league_admin_first_name = "jkl Team two"
    team_2_league_admin_last_name = "league Admin"
    team_2_league_admin_email = "jklteam2leagueadmin@mailinator.com"
    team_2_league_admin_user_name = "jklteam2leagueadmin"

    Team_3_name = "jkl Team three"
    Team_3_location = "India"

    team_3_team_admin_first_name = "jkl Team three"
    team_3_team_admin_last_name = "Team Admin"
    team_3_team_admin_email = "jklleagueteam3teamadmin@mailinator.com"
    team_3_team_admin_user_name = "jklleagueteam3teamadmin"

    team_3_league_admin_first_name = "jkl Team three"
    team_3_league_admin_last_name = "league Admin"
    team_3_league_admin_email = "jklteam3leagueadmin@mailinator.com"
    team_3_league_admin_user_name = "jklteam3leagueadmin"

    founded_year_index = 2
    sub_domain_1 = "Abc"
    sub_domain_2 = "def"
    sub_domain_3 = "igh"

############################ Team 1 users ################################

    Team_1_analyst_first_name = "jkl Team one"
    Team_1_analyst_last_name = "Analyst"
    Team_1_analyst_user_name = "jklteamoneAnalyst"
    Team_1_analyst_email = "jklteamoneAnalyst@mailinator.com"

    Team_1_coach_first_name = "jkl Team one"
    Team_1_coach_last_name = "coach"
    Team_1_coach_user_name = "jklteamonecoach"
    Team_1_coach_email = "jklteamonecoach@mailinator.com"

    Team_1_asst_coach_first_name = "jkl Team one"
    Team_1_asst_coach_last_name = "asst coach"
    Team_1_asst_coach_user_name = "jklteamoneasstcoach"
    Team_1_asst_coach_email = "jklteamoneasstcoach@mailinator.com"

    Team_1_scout_first_name = "jkl Team one"
    Team_1_scout_last_name = "scout"
    Team_1_scout_user_name = "jklteamonescout"
    Team_1_scout_email = "jklteamonescout@mailinator.com"

############################ Team 1 Players ################################

    Team_1_player_1_first_name = "jkl team one player"
    Team_1_player_1_last_name = "one"
    Team_1_player_1_user_name = "jkloneplayer"
    Team_1_player_1_email = "jklteamoneplayerone@mailinator.com"

    Team_1_player_2_first_name = "jkl team one player"
    Team_1_player_2_last_name = "two"
    Team_1_player_2_user_name = "jkltwoplayer"
    Team_1_player_2_email = "jklteamoneplayertwo@mailinator.com"

    Team_1_player_3_first_name = "jkl team one player"
    Team_1_player_3_last_name = "three"
    Team_1_player_3_user_name = "jklthreeplayer"
    Team_1_player_3_email = "jklteamoneplayerthree@mailinator.com"


##########################################################################

    # playerr_1_first_name = "player"
    # playerr_1_last_name = "one"
    # playerr_1_user_name = "qweoneplayerr"
    # playerr_1_email = "qweoneplayerr@mailinator.com"
    #
    # playerr_2_first_name = "player"
    # playerr_2_last_name = "two"
    # playerr_2_user_name = "qwetwoplayerr"
    # playerr_2_email = "qwetwoplayerr@mailinator.com"
    #
    # playerr_3_first_name = "player"
    # playerr_3_last_name = "three"
    # playerr_3_user_name = "qwethreeplayerr"
    # playerr_3_email = "qwethreeplayerr@mailinator.com"
    #
    # playerrr_1_first_name = "player"
    # playerrr_1_last_name = "one"
    # playerrr_1_user_name = "qweoneplayerrr"
    # playerrr_1_email = "qweoneplayerrr@mailinator.com"
    #
    # playerrr_2_first_name = "player"
    # playerrr_2_last_name = "two"
    # playerrr_2_user_name = "qwetwoplayerrr"
    # playerrr_2_email = "qwetwoplayerrr@mailinator.com"
    #
    # playerrr_3_first_name = "player"
    # playerrr_3_last_name = "three"
    # playerrr_3_user_name = "qwethreeplayerrr"
    # playerrr_3_email = "qwethreeplayerrr@mailinator.com"

    user_types_league_admin = "League Administrator"
    user_types_team_admin = "Team Administrator"
    user_types_analyst = "Analyst"
    user_types_coach = "Coach"
    user_types_player = "Players"
    user_types_scout = "Scout"
    user_types_asst_coach = "Assistant Coach"


    def test_a_add_league(self):
        driver = self.driver

        League = LeaguePage(driver)
        League.click_league_tab()
        time.sleep(2)
        League.click_add_new_button()
        League.enter_league_name(self.league_name)
        League.enter_league_location(self.league_location)
        League.click_add_submit_button()
        time.sleep(2)


    def test_b_add_Team_1_and_admin_league_admin(self):
        driver = self.driver

        Team = TeamPage(driver)
        Team1 = LeaguePage(driver)
        Team11 = UserPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team1.click_add_new_button()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        Team11.select_league(self.league_name)
        Team.enter_team_name(self.Team_1_name)
        Team.enter_team_location(self.Team_1_location)
        Team.select_founded_year(self.founded_year_index)
        Team.enter_sub_domain(self.sub_domain_1)
        Team.click_add_new_team_admin_checkbox()
        time.sleep(2)
        Team.enter_new_team_admin_first_name(self.team_1_team_admin_first_name)
        Team.enter_new_team_admin_last_name(self.team_1_team_admin_last_name)
        Team.enter_new_team_admin_email_xpath(self.team_1_team_admin_email)
        Team.enter_new_team_admin_user_name(self.team_1_team_admin_user_name)
        Team.click_add_new_league_admin_checkbox()
        time.sleep(2)
        Team.enter_new_league_admin_first_name(self.team_1_league_admin_first_name)
        Team.enter_new_league_admin_last_name(self.team_1_league_admin_last_name)
        Team.enter_new_league_admin_email_xpath(self.team_1_league_admin_email)
        Team.enter_new_league_admin_user_name(self.team_1_league_admin_user_name)
        Team1.click_add_submit_button()
        time.sleep(2)

    def test_c_add_Team_2_and_admin_league_admin(self):
        driver = self.driver

        Team = TeamPage(driver)
        Team1 = LeaguePage(driver)
        Team11 = UserPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team1.click_add_new_button()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        Team11.select_league(self.league_name)
        Team.enter_team_name(self.Team_2_name)
        Team.enter_team_location(self.Team_2_location)
        Team.select_founded_year(self.founded_year_index)
        Team.enter_sub_domain(self.sub_domain_2)
        Team.click_add_new_team_admin_checkbox()
        time.sleep(2)
        Team.enter_new_team_admin_first_name(self.team_2_team_admin_first_name)
        Team.enter_new_team_admin_last_name(self.team_2_team_admin_last_name)
        Team.enter_new_team_admin_email_xpath(self.team_2_team_admin_email)
        Team.enter_new_team_admin_user_name(self.team_2_team_admin_user_name)
        Team.click_add_new_league_admin_checkbox()
        time.sleep(2)
        Team.enter_new_league_admin_first_name(self.team_2_league_admin_first_name)
        Team.enter_new_league_admin_last_name(self.team_2_league_admin_last_name)
        Team.enter_new_league_admin_email_xpath(self.team_2_league_admin_email)
        Team.enter_new_league_admin_user_name(self.team_2_league_admin_user_name)
        Team1.click_add_submit_button()
        time.sleep(2)

    def test_d_add_Team_3_and_admin_league_admin(self):
        driver = self.driver

        Team = TeamPage(driver)
        Team1 = LeaguePage(driver)
        Team11 = UserPage(driver)
        Team.click_team_tab()
        time.sleep(2)
        Team1.click_add_new_button()
        time.sleep(1)
        driver.refresh()
        time.sleep(2)
        Team11.select_league(self.league_name)
        Team.enter_team_name(self.Team_3_name)
        Team.enter_team_location(self.Team_3_location)
        Team.select_founded_year(self.founded_year_index)
        Team.enter_sub_domain(self.sub_domain_3)
        Team.click_add_new_team_admin_checkbox()
        time.sleep(2)
        Team.enter_new_team_admin_first_name(self.team_3_team_admin_first_name)
        Team.enter_new_team_admin_last_name(self.team_3_team_admin_last_name)
        Team.enter_new_team_admin_email_xpath(self.team_3_team_admin_email)
        Team.enter_new_team_admin_user_name(self.team_3_team_admin_user_name)
        Team.click_add_new_league_admin_checkbox()
        time.sleep(2)
        Team.enter_new_league_admin_first_name(self.team_3_league_admin_first_name)
        Team.enter_new_league_admin_last_name(self.team_3_league_admin_last_name)
        Team.enter_new_league_admin_email_xpath(self.team_3_league_admin_email)
        Team.enter_new_league_admin_user_name(self.team_3_league_admin_user_name)
        Team1.click_add_submit_button()
        time.sleep(2)

    def test_e_add_analyst_1_and_select_team_1(self):
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

    def test_f_add_coach_and_select_team_1(self):
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

    def test_g_add_asst_coach_and_select_team_1(self):
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

    def test_h_add_scout_and_select_team_1(self):
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

    def test_i_add_player_1_and_select_team_1(self):
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

    def test_j_add_player_2_and_select_team_1(self):
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

    def test_k_add_player_3_and_select_team_1(self):
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
