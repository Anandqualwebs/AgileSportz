import unittest
from selenium import webdriver
import time
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage
from Pages.AnalystPage import AnalystPage
from Pages.LeaguePage import LeaguePage


class AnalystTest(unittest.TestCase):

# Replace Your Login Credentials

    baseURL = "http://159.65.142.31/agile-sports/beta/"
    correct_email = "xyzteamoneAnalyst@mailinator.com"
    correct_password = "123456"
    agilityURL = "http://159.65.142.31/agile-sports/beta/landing/agility-card"
    surveyURL = "http://159.65.142.31/agile-sports/beta/landing/post-game-survey"

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

    def test_1_assign_cards(self):
        driver = self.driver
        card = AnalystPage(driver)
        time.sleep(6)
        card.click_card_tab()
        self.driver.get(self.agilityURL)
        time.sleep(2)
#Match 1
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
#player1
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
#coach
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
#player1
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

#     def test_2_submit_survey(self):
#         driver = self.driver
#         survey = AnalystPage(driver)
#         time.sleep(2)
# #       survey.click_survey_tab()
#         self.driver.get(self.surveyURL)
#         time.sleep(2)
#         survey.click_survey_match_1_submit()
#         time.sleep(2)
#         survey.click_survey_question_1_checkbox()
#         survey.click_survey_question_1_checkbox()
#         survey.click_survey_question_1_checkbox()
#         survey.click_survey_question_1_checkbox()
#         survey.click_survey_question_1_checkbox()
#         survey.click_survey_common_submit()
#         time.sleep(5)

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


