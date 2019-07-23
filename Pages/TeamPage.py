import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class TeamPage():

    def __init__(self, driver):
        self.driver = driver


        self.team_tab_xpath = locators.team_tab_xpath
        self.team_name_input_xpath = locators.team_name_input_xpath
        self.team_location_input_xpath = locators.team_location_input_xpath
        self.select_league_xpath = locators.select_league_xpath
        self.select_founded_year_xpath = locators.select_founded_year_xpath
        self.number_of_sprints_xpath = locators.number_of_sprints_xpath
        self.sub_domain_input_xpath = locators.sub_domain_input_xpath

        self.add_new_team_admin_checkbox = locators.add_new_team_admin_checkbox
        self.team_admin_first_name_css = locators.team_admin_first_name_css
        self.team_admin_last_name_css = locators.team_admin_last_name_css
        self.team_admin_email_css = locators.team_admin_email_css
        self.team_admin_user_name_css = locators.team_admin_user_name_css

        self.add_new_league_admin_checkbox = locators.add_new_league_admin_checkbox
        self.league_admin_first_name_css = locators.league_admin_first_name_css
        self.league_admin_last_name_css = locators.league_admin_last_name_css
        self.league_admin_email_css = locators.league_admin_email_css
        self.league_admin_user_name_css = locators.league_admin_user_name_css

        self.table_team_names_xpath = locators.table_team_names_xpath
        self.table_team_location_xpath = locators.table_team_location_xpath
        self.table_team_founded_year_xpath = locators.table_team_founded_year_xpath
        self.table_team_admin_name_xpath = locators.table_team_admin_name_xpath
        self.table_team_league_name_xpath = locators.table_team_league_name_xpath
        self.table_team_league_number_of_sprints_xpath = locators.table_team_league_number_of_sprints_xpath
        self.table_team_league_number_of_games_xpath = locators.table_team_league_number_of_games_xpath





    def click_team_tab(self):
        self.driver.find_element_by_xpath(self.team_tab_xpath).click()

    def enter_team_name(self, text):
        self.driver.find_element_by_xpath(self.team_name_input_xpath).send_keys(text)

    def enter_team_location(self, text):
        self.driver.find_element_by_xpath(self.team_location_input_xpath).send_keys(text)

    def select_league(self, league):
        Select(self.driver.find_element_by_xpath(self.select_league_xpath)).select_by_index(league)

    def select_founded_year(self, year):
        Select(self.driver.find_element_by_xpath(self.select_founded_year_xpath)).select_by_index(year)

    def enter_sub_domain(self, text):
        self.driver.find_element_by_xpath(self.sub_domain_input_xpath).send_keys(text)


    def click_add_new_team_admin_checkbox(self):
        self.driver.find_element_by_xpath(self.add_new_team_admin_checkbox).click()

    def enter_new_team_admin_first_name(self, text):
        self.driver.find_element_by_css_selector(self.team_admin_first_name_css).send_keys(text)

    def enter_new_team_admin_last_name(self, text):
        self.driver.find_element_by_css_selector(self.team_admin_last_name_css).send_keys(text)

    def enter_new_team_admin_email_xpath(self, text):
        self.driver.find_element_by_css_selector(self.team_admin_email_css).send_keys(text)

    def enter_new_team_admin_user_name(self, text):
        self.driver.find_element_by_css_selector(self.team_admin_user_name_css).send_keys(text)


    def click_add_new_league_admin_checkbox(self):
        self.driver.find_element_by_xpath(self.add_new_league_admin_checkbox).click()

    def enter_new_league_admin_first_name(self, text):
        self.driver.find_element_by_css_selector(self.league_admin_first_name_css).send_keys(text)

    def enter_new_league_admin_last_name(self, text):
        self.driver.find_element_by_css_selector(self.league_admin_last_name_css).send_keys(text)

    def enter_new_league_admin_email_xpath(self, text):
        self.driver.find_element_by_css_selector(self.league_admin_email_css).send_keys(text)

    def enter_new_league_admin_user_name(self, text):
        self.driver.find_element_by_css_selector(self.league_admin_user_name_css).send_keys(text)










    def print_team_names(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_names_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_locations(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_location_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_founded_year(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_founded_year_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_admin_names(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_admin_name_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_league_names(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_league_name_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_sprints(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_league_number_of_sprints_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass

    def print_team_number_of_games(self):
        consumptions = self.driver.find_elements_by_xpath(self.table_team_league_number_of_games_xpath)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].text:
                print("{}.{}".format(r + 1, consumptions[r].text))
            else:
                pass



