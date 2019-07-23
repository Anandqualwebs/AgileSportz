import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators


class LeagueAdminPage():

    def __init__(self, driver):
        self.driver = driver

        self.match_tab_xpath = locators.match_tab_xpath




    def click_match_tab(self):
        self.driver.find_element_by_xpath(self.match_tab_xpath).click()





    # def enter_email(self, email):
    #     self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
    #     self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

