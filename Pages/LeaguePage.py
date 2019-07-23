import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class LeaguePage():

    def __init__(self, driver):
        self.driver = driver

        self.league_tab_xpath = locators.league_tab_xpath
        self.add_new_button_xpath = locators.add_new_button_xpath
        self.league_name_input_xpath = locators.league_name_input_xpath
        self.league_location_input_xpath = locators.league_location_input_xpath
        self.new_add_submit_button_xpath = locators.new_add_submit_button_xpath
        self.table_league_names_xpath = locators.table_league_names_xpath
        self.table_league_admin_names_xpath = locators.table_league_admin_names_xpath
        self.table_league_team_number_xpath = locators.table_league_team_number_xpath
        self.table_league_number_of_games_xpath = locators.table_league_number_of_games_xpath


    def click_league_tab(self):
        self.driver.find_element_by_xpath(self.league_tab_xpath).click()

    def click_add_new_button(self):
        self.driver.find_element_by_xpath(self.add_new_button_xpath).click()

    def enter_league_name(self, text):
        self.driver.find_element_by_xpath(self.league_name_input_xpath).send_keys(text)

    def enter_league_location(self, text):
        self.driver.find_element_by_xpath(self.league_location_input_xpath).send_keys(text)

    def click_add_submit_button(self):
        self.driver.find_element_by_xpath(self.new_add_submit_button_xpath).click()




    def print_league_names(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_league_names_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_league_admin_names(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_league_admin_names_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_league_team_number(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_league_team_number_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_number_of_games(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_league_number_of_games_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def wait_element_present(self):
        try:
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'KambiBC-event-result__score-list'))
            WebDriverWait(self.driver, 4).until(element_present)
        except Exception:
            print ('Timed out waiting for page to load')



