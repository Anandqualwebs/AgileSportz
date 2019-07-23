import sys
import os
sys.path.append(os.path.dirname(sys.path[0] + "\Locators"))
from Locators.Locators import locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class buildingpage():

    def __init__(self, driver):
        self.driver = driver

        self.building_tab_linktext = locators.building_tab_linktext
        self.building_overview_css = locators.building_overview_css
        self.overview_page_xpath = locators.overview_page_xpath

        self.building_temp_out_css = locators.building_temp_out_css
        self.building_temp_building_css = locators.building_temp_building_css
        self.building_grade_css = locators.building_grade_css

        self.building_name_css = locators.building_name_css
        self.building_address_css = locators.building_address_css
        self.building_stats_css = locators.building_stats_css


    def building_click(self):
            self.driver.find_element_by_link_text(self.building_tab_linktext).click()

    def building_click_overview(self):
            self.driver.find_element_by_css_selector(self.building_overview_css).click()

    def overview_refers_overview_page_check(self):
        element1 = self.driver.find_element_by_xpath(self.overview_page_xpath).is_displayed()
        print("Overview Refers Overview Page = ", element1)

    def building_grade_visible_check(self):
        element1 = self.driver.find_element_by_css_selector(self.building_grade_css).is_displayed()
        print("Building Grade Are Displayed = ", element1)

    def building_temp_out_visible_check(self):
        element1 = self.driver.find_element_by_css_selector(self.building_temp_out_css).is_displayed()
        print("Buildings Temp Outside Are Displayed = ", element1)

    def building_temp_visible_check(self):
        element1 = self.driver.find_element_by_css_selector(self.building_temp_building_css).is_displayed()
        print("Buildings Temp Are Displayed = ", element1)

    def print_buildings_name(self):
        names = self.driver.find_elements_by_css_selector(self.building_name_css)
        amount = len(names)

        for r in range(0, amount):
            if names[r].text:
                print("{}.{}".format(r + 1, names[r].text))
            else:
                pass

    def print_buildings_address(self):
        addresses = self.driver.find_elements_by_css_selector(self.building_address_css)
        amount = len(addresses)

        for r in range(0, amount):
            if addresses[r].text:
                print("{}.{}".format(r + 1, addresses[r].text))
            else:
                pass

    def print_buildings_stats(self):
        addresses = self.driver.find_elements_by_css_selector(self.building_stats_css)
        amount = len(addresses)

        for r in range(0, amount):
            if addresses[r].text:
                print("{}.{}".format(r + 1, addresses[r].text))
            else:
                pass

    def compare_buildings_stats(self):
        consumptions = self.driver.find_elements_by_css_selector(self.building_stats_css)
        amount = len(consumptions)

        for r in range(0, amount):
            try:
                assert consumptions[r].get_attribute('textContent') != '-'
                print("{}.{}".format(r + 1, 'This Stat is Having Some Values'))
            except Exception as e:
                print("{}.{}".format(r + 1, 'This Stat Having no Values "-"'))

