import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.select import Select


class CoachPage():

    def __init__(self, driver):
        self.driver = driver

        self.card_tab_xpath = locators.card_tab_xpath


    def click_card_tab(self):
        self.driver.find_element_by_xpath(self.card_tab_xpath).click()




