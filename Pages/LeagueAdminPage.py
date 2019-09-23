import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.select import Select

class LeagueAdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.game_tab_xpath = locators.game_tab_xpath
        self.select_opponent_xpath = locators.select_opponent_xpath
        self.match_location_xpath = locators.match_location_xpath
        self.match_date_xpath = locators.match_date_xpath
        self.match_time_xpath = locators.match_time_xpath


    def click_game_tab(self):
        self.driver.find_element_by_xpath(self.game_tab_xpath).click()

    def select_match_opponent(self, year):
        Select(self.driver.find_element_by_xpath(self.select_opponent_xpath)).select_by_index(year)

    def enter_match_location(self, email):
        self.driver.find_element_by_xpath(self.match_location_xpath).send_keys(email)

    def enter_date_location(self, email):
        self.driver.find_element_by_xpath(self.match_date_xpath).send_keys(email)

    def enter_time_location(self, email):
        self.driver.find_element_by_xpath(self.match_time_xpath).send_keys(email)
