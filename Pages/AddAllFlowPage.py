import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddAllFlowPage():

    def __init__(self, driver):
        self.driver = driver


    #     self.user_tab_xpath = locators.user_tab_xpath
    #     self.select_user_type_xpath = locators.select_user_type_xpath
    #     self.add_new_team_xpath = locators.add_new_team_xpath
    #     self.select_team_xpath = locators.select_team_xpath
    #     self.select_league_xpath = locators.select_league_xpath
    #
    #
    # def click_user_tab(self):
    #     self.driver.find_element_by_xpath(self.user_tab_xpath).click()
    #
    # def select_user_type(self, usertype):
    #     Select(self.driver.find_element_by_xpath(self.select_user_type_xpath)).select_by_visible_text(usertype)
    #
    # def select_team(self, team):
    #     Select(self.driver.find_element_by_xpath(self.select_team_xpath)).select_by_visible_text(team)
    #
    # def select_league(self, team):
    #     Select(self.driver.find_element_by_xpath(self.select_league_xpath)).select_by_visible_text(team)
    #
    #

