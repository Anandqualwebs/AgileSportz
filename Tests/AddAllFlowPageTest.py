import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import os
from Pages.LoginPage import Loginpage
from Pages.LeagueAdminPage import LeagueAdminPage
sys.path.append(os.path.dirname(sys.path[0] + "\Pages"))
from Pages.LeaguePage import LeaguePage
from Pages.TeamPage import TeamPage
from Pages.UserPage import UserPage
from Pages.AnalystPage import AnalystPage
from Pages.TeamAdminPage import TeamAdminPage
from EnvSetup.EnvironSetup import EnvironmentSetup


###### This Will Add

# 1 leagues
# 3 Teams
# 3 League Admin  (1/1/1 Per Team)
# 3 Team Admins   (1/1/1 Per Team)
# 1 Analyst       (1 in Team 1)
# 1 Coach         (1 in Team 1)
# 3 player        (3 in Team 1)


###### After Adding

# League Admin = Will Ad
# d 2 Matches
# Team Admin = Will Add 1 Sprints with 2 matches
# Analyst = Will Assign Recommended Score to coach & player 1
# Coach = Will Plan his Score of Match 1
# Player 1 = Will Plan his Score of Match 1
# Team Admin = Will close Sprint & Give Actual Score to Coach & players 1


class AddAllFlowTest(EnvironmentSetup):
    league_name = "Agile League"
    league_location = "India"

########## Teams & Team Admins & League Admins ############################

    Team_1_name = "Agile Team One"
    Team_1_location = "India"

    team_1_team_admin_first_name = "Agile Team one"
    team_1_team_admin_last_name = "Team Admin"
    team_1_team_admin_email = "Agileleagueteam1teamadmin@gmail.com"
    team_1_team_admin_user_name = "Agileleagueteam1teamadmin"

    team_1_league_admin_first_name = "Agile Team one"
    team_1_league_admin_last_name = "league Admin"
    team_1_league_admin_email = "Agileteam1leagueadmin@gmail.com"
    team_1_league_admin_user_name = "Agileteam1leagueadmin"

    Team_2_name = "Agile Team two"
    Team_2_location = "India"

    team_2_team_admin_first_name = "Agile Team two"
    team_2_team_admin_last_name = "Team Admin"
    team_2_team_admin_email = "Agileleagueteam2teamadmin@gmail.com"
    team_2_team_admin_user_name = "Agileleagueteam2teamadmin"

    team_2_league_admin_first_name = "Agile Team two"
    team_2_league_admin_last_name = "league Admin"
    team_2_league_admin_email = "Agileteam2leagueadmin@gmail.com"
    team_2_league_admin_user_name = "Agileteam2leagueadmin"

    Team_3_name = "Agile Team three"
    Team_3_location = "India"

    team_3_team_admin_first_name = "Agile Team three"
    team_3_team_admin_last_name = "Team Admin"
    team_3_team_admin_email = "Agileleagueteam3teamadmin@gmail.com"
    team_3_team_admin_user_name = "Agileleagueteam3teamadmin"

    team_3_league_admin_first_name = "Agile Team three"
    team_3_league_admin_last_name = "league Admin"
    team_3_league_admin_email = "Agileteam3leagueadmin@gmail.com"
    team_3_league_admin_user_name = "Agileteam3leagueadmin"

    founded_year_index = 2
    sub_domain_1 = "Abc"
    sub_domain_2 = "def"
    sub_domain_3 = "igh"

    sprint_number = 1

############################ Team 1 users ################################

    Team_1_analyst_first_name = "Agile Team one"
    Team_1_analyst_last_name = "Analyst"
    Team_1_analyst_user_name = "AgileteamoneAnalyst"
    Team_1_analyst_email = "AgileteamoneAnalyst@gmail.com"

    Team_1_coach_first_name = "Agile Team one"
    Team_1_coach_last_name = "coach"
    Team_1_coach_user_name = "Agileteamonecoach"
    Team_1_coach_email = "Agileteamonecoach@gmail.com"

    Team_1_asst_coach_first_name = "Agile Team one"
    Team_1_asst_coach_last_name = "asst coach"
    Team_1_asst_coach_user_name = "Agileteamoneasstcoach"
    Team_1_asst_coach_email = "Agileteamoneasstcoach@gmail.com"

    Team_1_scout_first_name = "Agile Team one"
    Team_1_scout_last_name = "scout"
    Team_1_scout_user_name = "Agileteamonescout"
    Team_1_scout_email = "Agileteamonescout@gmail.com"

############################ Team 1 Players ################################

    Team_1_player_1_first_name = "Agile team one player"
    Team_1_player_1_last_name = "one"
    Team_1_player_1_user_name = "Agileoneplayer"
    Team_1_player_1_email = "Agileteamoneplayerone@gmail.com"

    Team_1_player_2_first_name = "Agile team one player"
    Team_1_player_2_last_name = "two"
    Team_1_player_2_user_name = "Agiletwoplayer"
    Team_1_player_2_email = "Agileteamoneplayertwo@gmail.com"

    Team_1_player_3_first_name = "Agile team one player"
    Team_1_player_3_last_name = "three"
    Team_1_player_3_user_name = "Agilethreeplayer"
    Team_1_player_3_email = "Agileteamoneplayerthree@gmail.com"

##########################################################################

    user_types_league_admin = "League Administrator"
    user_types_team_admin = "Team Administrator"
    user_types_analyst = "Analyst"
    user_types_coach = "Coach"
    user_types_player = "Players"
    user_types_scout = "Scout"
    user_types_asst_coach = "Assistant Coach"

#########################################################################

    common_password = "123456"
    opponent1 = 1
    opponent2 = 2
    opponent3 = 3
    match_location = "Usa"
    match_1_date = "8/25/2019"
    match_2_date = "8/26/2019"
    match_time = "03:00"

##########################################################################
    status_closed = "Closed"
    select_match_1 = 1
    select_match_2 = 2
    actual_score = 20

##########################################################################

    agilityURL = "http://159.65.142.31/agile-sports/beta/landing/agility-card"
    surveyURL = "http://159.65.142.31/agile-sports/beta/landing/post-game-survey"
    sprintstrategyURL = "http://159.65.142.31/agile-sports/beta/landing/sprint-strategy"
    meetingnoteURL = "http://159.65.142.31/agile-sports/beta/landing/meeting-notes"
    GameURL = "http://159.65.142.31/agile-sports/beta/landing/view-match"


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

    def test_i_add_player_1_2_3_and_select_team_1(self):
        driver = self.driver
        Player1 = LeaguePage(driver)
        login = Loginpage(self.driver)
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

        Player1.click_add_new_button()
        time.sleep(2)
        player.enter_user_first_name(self.Team_1_player_2_first_name)
        player.enter_user_last_name(self.Team_1_player_2_last_name)
        player.enter_user_email_xpath(self.Team_1_player_2_email)
        player.enter_user_username(self.Team_1_player_2_user_name)
        player.select_user_type(self.user_types_player)
        time.sleep(4)
        player.select_team(self.Team_1_name)
        time.sleep(2)
        Player1.click_add_submit_button()
        time.sleep(2)

        Player1.click_add_new_button()
        time.sleep(2)
        player.enter_user_first_name(self.Team_1_player_3_first_name)
        player.enter_user_last_name(self.Team_1_player_3_last_name)
        player.enter_user_email_xpath(self.Team_1_player_3_email)
        player.enter_user_username(self.Team_1_player_3_user_name)
        player.select_user_type(self.user_types_player)
        time.sleep(4)
        player.select_team(self.Team_1_name)
        time.sleep(2)
        Player1.click_add_submit_button()
        time.sleep(2)


# Logout
        time.sleep(5)
        login.click_profile_icon()
        login.click_profile_icon()
        time.sleep(1)
        login.click_logout()
        time.sleep(2)
        driver.delete_all_cookies()
        driver.refresh()
        time.sleep(2)


    def test_l_league_admin_add_match_1(self):
        driver = self.driver
        match = LeagueAdminPage(driver)
        matchh = LeaguePage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.team_1_league_admin_email)
        login.enter_password(self.common_password)
        login.click_login()
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

    def test_m_league_admin_add_match_2(self):
        driver = self.driver
        match = LeagueAdminPage(driver)
        matchh = LeaguePage(driver)
        login = Loginpage(driver)
        time.sleep(2)
        self.driver.get(self.GameURL)
        #match.click_game_tab()
        time.sleep(2)
        matchh.click_add_new_button()
        time.sleep(2)
        match.select_match_opponent(self.opponent2)
        match.enter_match_location(self.match_location)
        match.enter_date_location(self.match_2_date)
        match.enter_time_location(self.match_time)
        matchh.click_add_submit_button()
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

    def test_n_team_admin_add_sprint_1(self):
        driver = self.driver
        sprint = TeamAdminPage(driver)
        login = Loginpage(driver)
        time.sleep(2)
        login.enter_email(self.team_1_team_admin_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        matchh = LeaguePage(driver)
        time.sleep(1)
        sprint.click_sprint_tab()
        time.sleep(1)
        matchh.click_add_new_button()
        time.sleep(1)
        sprint.enter_sprint_number(self.sprint_number)
        sprint.click_match_1_checkbox()
        sprint.click_match_2_checkbox()
        sprint.enter_sprint_start_date(self.match_1_date)
        sprint.enter_sprint_end_date(self.match_2_date)
        time.sleep(1)
        sprint.click_save_sprint()
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

    def test_o_analyst_recommend_score_to_coach_and_players(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(driver)
        time.sleep(2)
        login.enter_email(self.Team_1_analyst_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        self.driver.get(self.agilityURL)
        time.sleep(2)
# Match 1
        card.click_game_1()
        time.sleep(1)
# coach
        card.click_coach_assign()
        time.sleep(2)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
# player1
        card.click_player_1_assign()
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)

#player2
        card.click_player_2_assign()
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
#player 3
        card.click_player_3_assign()
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
        self.driver.get(self.agilityURL)
        #card.click_card_tab()
        time.sleep(1)
#Match 2
        card.click_game_2()
        time.sleep(1)
# coach
        card.click_coach_assign()
        time.sleep(2)
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()

        time.sleep(2)
# player1
        card.click_player_1_assign()
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
#player2
        card.click_player_2_assign()
        card.click_matrics_1()
        card.click_matrics_2()
        card.click_matrics_3()
        card.click_matrics_4()
        card.click_matrics_5()
        time.sleep(1)
        card.click_assign_submit_button()
        time.sleep(2)
#player3
        card.click_player_3_assign()
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

    def test_p_coach_plan_score(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(driver)
        time.sleep(2)
        login.enter_email(self.Team_1_coach_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        self.driver.get(self.agilityURL)
        time.sleep(2)
#Match 1
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
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 2
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

    def test_q_player_1_plan_score(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.Team_1_player_1_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        time.sleep(1)
        self.driver.get(self.agilityURL)
        time.sleep(2)
#Match 1
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
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 2
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


    def test_r_player_plan_score(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.Team_1_player_2_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        time.sleep(1)
        self.driver.get(self.agilityURL)
        time.sleep(2)
#Match 1
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
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 2
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

    def test_s_player_3_plan_score(self):
        driver = self.driver
        card = AnalystPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.Team_1_player_3_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
        time.sleep(1)
        self.driver.get(self.agilityURL)
        time.sleep(2)
#Match 1
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
        #card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(1)
#Match 2
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


    def test_t_sprint_close_and_give_actual(self):
        driver = self.driver
        sprint = TeamAdminPage(driver)
        matchh = LeaguePage(driver)
        card = AnalystPage(driver)
        cardd = TeamAdminPage(driver)
        login = Loginpage(self.driver)
        login.enter_email(self.team_1_team_admin_email)
        login.enter_password(self.common_password)
        login.click_login()
        time.sleep(2)
#sprint
        sprint.click_sprint_tab()
        time.sleep(1)
        sprint.click_edit_sprint()
        time.sleep(1)
        sprint.select_sprint_status(self.status_closed)
        time.sleep(1)
        matchh.click_add_submit_button()
        time.sleep(2)
#card
        self.driver.get(self.agilityURL)
        #card.click_card_tab()
        time.sleep(1)

#match 1
        cardd.select_card_match(self.select_match_1)
        time.sleep(1)
        cardd.enter_coach_actual_input_1(self.actual_score)
        cardd.enter_coach_actual_input_2(self.actual_score)
        cardd.enter_coach_actual_input_3(self.actual_score)
        cardd.enter_coach_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_1()
        time.sleep(2)
        cardd.enter_player_1_actual_input_1(self.actual_score)
        cardd.enter_player_1_actual_input_2(self.actual_score)
        cardd.enter_player_1_actual_input_3(self.actual_score)
        cardd.enter_player_1_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_2()
        time.sleep(2)
        cardd.enter_player_2_actual_input_1(self.actual_score)
        cardd.enter_player_2_actual_input_2(self.actual_score)
        cardd.enter_player_2_actual_input_3(self.actual_score)
        cardd.enter_player_2_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_3()
        time.sleep(2)
        cardd.enter_player_3_actual_input_1(self.actual_score)
        cardd.enter_player_3_actual_input_2(self.actual_score)
        cardd.enter_player_3_actual_input_3(self.actual_score)
        cardd.enter_player_3_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_4()

# match 2
        cardd.select_card_match(self.select_match_2)
        time.sleep(1)
        cardd.enter_coach_actual_input_1(self.actual_score)
        cardd.enter_coach_actual_input_2(self.actual_score)
        cardd.enter_coach_actual_input_3(self.actual_score)
        cardd.enter_coach_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_1()
        time.sleep(2)
        cardd.enter_player_1_actual_input_1(self.actual_score)
        cardd.enter_player_1_actual_input_2(self.actual_score)
        cardd.enter_player_1_actual_input_3(self.actual_score)
        cardd.enter_player_1_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_2()
        time.sleep(2)
        cardd.enter_player_2_actual_input_1(self.actual_score)
        cardd.enter_player_2_actual_input_2(self.actual_score)
        cardd.enter_player_2_actual_input_3(self.actual_score)
        cardd.enter_player_2_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_3()
        time.sleep(2)
        cardd.enter_player_3_actual_input_1(self.actual_score)
        cardd.enter_player_3_actual_input_2(self.actual_score)
        cardd.enter_player_3_actual_input_3(self.actual_score)
        cardd.enter_player_3_actual_input_4(self.actual_score)
        cardd.click_actual_edit_save_4()

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

