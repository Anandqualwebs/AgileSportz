import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.select import Select


class AnalystPage():

    def __init__(self, driver):
        self.driver = driver

        self.card_tab_xpath = locators.card_tab_xpath
        self.game_1_link_text = locators.game_1_link_text
        self.game_2_link_text = locators.game_2_link_text
        self.coach_assign_css = locators.coach_assign_css

        self.player_1_assign_css = locators.player_1_assign_css
        self.player_2_assign_css = locators.player_2_assign_css
        self.player_3_assign_css = locators.player_3_assign_css

        self.matrics_1_xpath = locators.matrics_1_xpath
        self.matrics_2_xpath = locators.matrics_2_xpath
        self.matrics_3_xpath = locators.matrics_3_xpath
        self.matrics_4_xpath = locators.matrics_4_xpath
        self.matrics_5_xpath = locators.matrics_5_xpath

        self.assign_submit_button_xpath = locators.assign_submit_button_xpath

        self.plan_tab_xpath = locators.plan_tab_xpath

        self.survey_tab_xpath = locators.survey_tab_xpath
        self.survey_match_1_submit_xpath = locators.survey_match_1_submit_xpath
        self.survey_match_2_submit_xpath = locators.survey_match_2_submit_xpath
        self.survey_question_1_checkbox_xpath = locators.survey_question_1_checkbox_xpath
        self.survey_question_2_checkbox_xpath = locators.survey_question_2_checkbox_xpath
        self.survey_question_3_checkbox_xpath = locators.survey_question_3_checkbox_xpath
        self.survey_question_4_checkbox_xpath = locators.survey_question_4_checkbox_xpath
        self.survey_question_5_checkbox_xpath = locators.survey_question_5_checkbox_xpath
        self.survey_common_submit_xpath = locators.survey_common_submit_xpath


    def click_card_tab(self):
        self.driver.find_element_by_xpath(self.card_tab_xpath).click()

    def click_game_1(self):
        self.driver.find_element_by_link_text(self.game_1_link_text).click()

    def click_game_2(self):
        self.driver.find_element_by_link_text(self.game_2_link_text).click()

    def click_coach_assign(self):
        self.driver.find_element_by_css_selector(self.coach_assign_css).click()

    def click_player_1_assign(self):
        self.driver.find_element_by_css_selector(self.player_1_assign_css).click()

    def click_player_2_assign(self):
        self.driver.find_element_by_css_selector(self.player_2_assign_css).click()

    def click_player_3_assign(self):
        self.driver.find_element_by_css_selector(self.player_3_assign_css).click()

    def click_matrics_1(self):
        self.driver.find_element_by_xpath(self.matrics_1_xpath).click()

    def click_matrics_2(self):
        self.driver.find_element_by_xpath(self.matrics_2_xpath).click()

    def click_matrics_3(self):
        self.driver.find_element_by_xpath(self.matrics_3_xpath).click()

    def click_matrics_4(self):
        self.driver.find_element_by_xpath(self.matrics_4_xpath).click()

    def click_matrics_5(self):
        self.driver.find_element_by_xpath(self.matrics_5_xpath).click()

    def click_assign_submit_button(self):
        self.driver.find_element_by_xpath(self.assign_submit_button_xpath).click()



    def click_survey_tab(self):
        self.driver.find_element_by_xpath(self.survey_tab_xpath).click()

    def click_survey_match_1_submit(self):
        self.driver.find_element_by_xpath(self.survey_match_1_submit_xpath).click()

    def click_survey_match_2_submit(self):
        self.driver.find_element_by_xpath(self.survey_match_2_submit_xpath).click()

    def click_survey_question_1_checkbox(self):
        self.driver.find_element_by_xpath(self.survey_question_1_checkbox_xpath).click()

    def click_survey_question_2_checkbox(self):
        self.driver.find_element_by_xpath(self.survey_question_2_checkbox_xpath).click()

    def click_survey_question_3_checkbox(self):
        self.driver.find_element_by_xpath(self.survey_question_3_checkbox_xpath).click()

    def click_survey_question_4_checkbox(self):
        self.driver.find_element_by_xpath(self.survey_question_4_checkbox_xpath).click()

    def click_survey_question_5_checkbox(self):
        self.driver.find_element_by_xpath(self.survey_question_5_checkbox_xpath).click()

    def click_survey_common_submit(self):
        self.driver.find_element_by_xpath(self.survey_common_submit_xpath).click()

    def click_plan_tab(self):
        self.driver.find_element_by_xpath(self.plan_tab_xpath).click()









