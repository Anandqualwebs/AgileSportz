import unittest
from selenium import webdriver
import time
import sys
import os

from Pages.AnalystPage import AnalystPage

sys.path.append(os.path.dirname(sys.path[0]+"\Pages"))
from Pages.LoginPage import Loginpage
from Pages.TeamAdminPage import TeamAdminPage
from Pages.LeaguePage import LeaguePage

class TeamAdminTest(unittest.TestCase):

# Replace Your Login Credentials

    baseURL = "http://159.65.142.31/agile-sports/beta/"
    agilityURL = "http://159.65.142.31/agile-sports/beta/landing/agility-card"
    correct_email = "xyzleagueteam1teamadmin@mailinator.com"
    correct_password = "123456"
    sprint_number = 1
    sprint_start_date = "8/25/2019"
    sprint_end_date = "8/26/2019"
    status_closed = "Closed"
    select_match_1 = 1
    select_match_2 = 2
    actual_score = 20

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

    # def test_1_add_sprint_1(self):
    #     driver = self.driver
    #     sprint = TeamAdminPage(driver)
    #     matchh = LeaguePage(driver)
    #     time.sleep(1)
    #     sprint.click_sprint_tab()
    #     time.sleep(1)
    #     matchh.click_add_new_button()
    #     time.sleep(1)
    #     sprint.enter_sprint_number(self.sprint_number)
    #     sprint.click_match_1_checkbox()
    #     sprint.click_match_2_checkbox()
    #     sprint.enter_sprint_start_date(self.sprint_start_date)
    #     sprint.enter_sprint_end_date(self.sprint_end_date)
    #     time.sleep(1)
    #     sprint.click_save_sprint()
    #     time.sleep(2)

#########################################################################


    def test_2_edit_sprint_1(self):
        driver = self.driver
        sprint = TeamAdminPage(driver)
        matchh = LeaguePage(driver)
        time.sleep(1)
        sprint.click_sprint_tab()
        time.sleep(1)
        sprint.click_edit_sprint()
        time.sleep(1)
        sprint.select_sprint_status(self.status_closed)
        time.sleep(1)
        matchh.click_add_submit_button()
        time.sleep(2)

    def test_3_card_assign_actual(self):
        driver = self.driver
        card = AnalystPage(driver)
        cardd = TeamAdminPage(driver)
        time.sleep(1)
        self.driver.get(self.agilityURL)
        #card.click_card_tab()
        time.sleep(1)
#Match 1
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
# Match 2
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
        time.sleep(6)


    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()





