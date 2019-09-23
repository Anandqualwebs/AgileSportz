import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.select import Select

class TeamAdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.sprint_tab_xpath = locators.sprint_tab_xpath
        self.sprint_number_xpath = locators.sprint_number_xpath
        self.sprint_start_date_xpath = locators.sprint_start_date_xpath
        self.sprint_number_date_xpath = locators.sprint_number_date_xpath
        self.match_1_checkbox_css = locators.match_1_checkbox_css
        self.match_2_checkbox_css = locators.match_2_checkbox_css
        self.match_3_checkbox_css = locators.match_3_checkbox_css
        self.edit_sprint_xpath = locators.edit_sprint_xpath
        self.sprint_status_xpath = locators.sprint_status_xpath
        self.select_match_xpath = locators.select_match_xpath

        self.coach_card_input_1 = locators.coach_card_input_1
        self.coach_card_input_2 = locators.coach_card_input_2
        self.coach_card_input_3 = locators.coach_card_input_3
        self.coach_card_input_4 = locators.coach_card_input_4
        self.player_1_card_input_1 = locators.player_1_card_input_1
        self.player_1_card_input_2 = locators.player_1_card_input_2
        self.player_1_card_input_3 = locators.player_1_card_input_3
        self.player_1_card_input_4 = locators.player_1_card_input_4
        self.player_2_card_input_1 = locators.player_2_card_input_1
        self.player_2_card_input_2 = locators.player_2_card_input_2
        self.player_2_card_input_3 = locators.player_2_card_input_3
        self.player_2_card_input_4 = locators.player_2_card_input_4
        self.player_3_card_input_1 = locators.player_3_card_input_1
        self.player_3_card_input_2 = locators.player_3_card_input_2
        self.player_3_card_input_3 = locators.player_3_card_input_3
        self.player_3_card_input_4 = locators.player_3_card_input_4
        self.actual_save_edit_button_1_xpath = locators.actual_save_edit_button_1_xpath
        self.actual_save_edit_button_2_xpath = locators.actual_save_edit_button_2_xpath
        self.actual_save_edit_button_3_xpath = locators.actual_save_edit_button_3_xpath
        self.actual_save_edit_button_4_xpath = locators.actual_save_edit_button_4_xpath
        self.sprint_add_xpath = locators.sprint_add_xpath


    def click_sprint_tab(self):
        self.driver.find_element_by_xpath(self.sprint_tab_xpath).click()

    def click_match_1_checkbox(self):
        self.driver.find_element_by_css_selector(self.match_1_checkbox_css).click()

    def click_match_2_checkbox(self):
        self.driver.find_element_by_css_selector(self.match_2_checkbox_css).click()

    def enter_sprint_number(self, email):
        self.driver.find_element_by_xpath(self.sprint_number_xpath).send_keys(email)

    def enter_sprint_start_date(self, email):
        self.driver.find_element_by_xpath(self.sprint_start_date_xpath).send_keys(email)

    def enter_sprint_end_date(self, email):
        self.driver.find_element_by_xpath(self.sprint_number_date_xpath).send_keys(email)

    def click_save_sprint(self):
        self.driver.find_element_by_xpath(self.sprint_add_xpath).click()

    def click_edit_sprint(self):
        self.driver.find_element_by_xpath(self.edit_sprint_xpath).click()

    def select_sprint_status(self, usertype):
        Select(self.driver.find_element_by_xpath(self.sprint_status_xpath)).select_by_visible_text(usertype)

    def select_card_match(self, usertype):
        Select(self.driver.find_element_by_xpath(self.select_match_xpath)).select_by_index(usertype)


    def enter_coach_actual_input_1(self, email):
        self.driver.find_element_by_xpath(self.coach_card_input_1).send_keys(email)

    def enter_coach_actual_input_2(self, email):
        self.driver.find_element_by_xpath(self.coach_card_input_2).send_keys(email)

    def enter_coach_actual_input_3(self, email):
        self.driver.find_element_by_xpath(self.coach_card_input_3).send_keys(email)

    def enter_coach_actual_input_4(self, email):
        self.driver.find_element_by_xpath(self.coach_card_input_4).send_keys(email)


    def enter_player_1_actual_input_1(self, email):
        self.driver.find_element_by_xpath(self.player_1_card_input_1).send_keys(email)

    def enter_player_1_actual_input_2(self, email):
        self.driver.find_element_by_xpath(self.player_1_card_input_2).send_keys(email)

    def enter_player_1_actual_input_3(self, email):
        self.driver.find_element_by_xpath(self.player_1_card_input_3).send_keys(email)

    def enter_player_1_actual_input_4(self, email):
        self.driver.find_element_by_xpath(self.player_1_card_input_4).send_keys(email)



    def enter_player_2_actual_input_1(self, email):
        self.driver.find_element_by_xpath(self.player_2_card_input_1).send_keys(email)

    def enter_player_2_actual_input_2(self, email):
        self.driver.find_element_by_xpath(self.player_2_card_input_2).send_keys(email)

    def enter_player_2_actual_input_3(self, email):
        self.driver.find_element_by_xpath(self.player_2_card_input_3).send_keys(email)

    def enter_player_2_actual_input_4(self, email):
        self.driver.find_element_by_xpath(self.player_2_card_input_4).send_keys(email)



    def enter_player_3_actual_input_1(self, email):
        self.driver.find_element_by_xpath(self.player_3_card_input_1).send_keys(email)

    def enter_player_3_actual_input_2(self, email):
        self.driver.find_element_by_xpath(self.player_3_card_input_2).send_keys(email)

    def enter_player_3_actual_input_3(self, email):
        self.driver.find_element_by_xpath(self.player_3_card_input_3).send_keys(email)

    def enter_player_3_actual_input_4(self, email):
        self.driver.find_element_by_xpath(self.player_3_card_input_4).send_keys(email)



    def click_actual_edit_save_1(self):
        self.driver.find_element_by_xpath(self.actual_save_edit_button_1_xpath).click()

    def click_actual_edit_save_2(self):
        self.driver.find_element_by_xpath(self.actual_save_edit_button_2_xpath).click()

    def click_actual_edit_save_3(self):
        self.driver.find_element_by_xpath(self.actual_save_edit_button_3_xpath).click()

    def click_actual_edit_save_4(self):
        self.driver.find_element_by_xpath(self.actual_save_edit_button_4_xpath).click()


