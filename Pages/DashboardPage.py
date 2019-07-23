import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DashboardPage():

    def __init__(self, driver):
        self.driver = driver

        self.logo_click_xpath = locators.logo_click_xpath
        self.dashboard_text_xpath = locators.dashboard_text_xpath
        self.chart_xpath = locators.chart_xpath
        self.electricity_xpath = locators.electricity_xpath
        self.water_xpath = locators.water_xpath
        self.heat_xpath = locators.heat_xpath
        self.portfolio_monthly_xpath = locators.portfolio_monthly_xpath
        self.notification_feed_xpath = locators.notification_feed_xpath
        self.notification_icon_xpath = locators.notification_icon_xpath
        self.notification_feed_close_xpath= locators.notification_feed_close_xpath
        self.expand_map_xpath = locators.expand_map_xpath
        self.collapse_map_xpath = locators.collapse_map_xpath
        self.google_zoomin_xpath = locators.google_zoomin_xpath
        self.google_zoomout_xpath = locators.google_zoomout_xpath
        self.google_fullscreen_max_min_xpath = locators.google_fullscreen_max_min_xpath
        self.portfolio_electricity_all_bars_value = locators.portfolio_electricity_all_bars_value
        self.portfolio_electricity_all_bars_height = locators.portfolio_electricity_all_bars_height
        self.portfolio_monthly_values_css = locators.portfolio_monthly_values_css

    def print_realtime_bars_values(self):
        consumptions = self.driver.find_elements_by_css_selector(self.portfolio_electricity_all_bars_value)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].get_attribute('textContent'):
                print("{}.{}".format(r + 1, consumptions[r].get_attribute('textContent')))
            else:
                pass

    def print_realtime_bars_heights(self):
        consumptions = self.driver.find_elements_by_css_selector(self.portfolio_electricity_all_bars_height)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].get_attribute('height'):
                print("{}.{}".format(r + 1, consumptions[r].get_attribute('height')))
            else:
                pass

    def compare_realtime_bars_heights(self):
        consumptions = self.driver.find_elements_by_css_selector(self.portfolio_electricity_all_bars_height)
        amount = len(consumptions)

        for r in range(0, amount):
            try:
                assert consumptions[r].get_attribute('height') != '0'
                print("{}.{}".format(r + 1, 'Height is Greater than 0'))
            except Exception as e:
                print("{}.{}".format(r + 1, 'Height is less than or equals 0'))


    def print_portfolio_values(self):
        consumptions = self.driver.find_elements_by_css_selector(self.portfolio_monthly_values_css)
        amount = len(consumptions)

        for r in range(0, amount):
            if consumptions[r].get_attribute('textContent'):
                print("{}.{}".format(r + 1, consumptions[r].get_attribute('textContent')))
            else:
                pass

    def compare_portfolio_values(self):
        consumptions = self.driver.find_elements_by_css_selector(self.portfolio_monthly_values_css)
        amount = len(consumptions)

        for r in range(0, amount):
            try:
                assert consumptions[r].get_attribute('textContent') != '0'
                print("{}.{}".format(r + 1, 'Monthly Value is Greater than 0'))
            except Exception as e:
                print("{}.{}".format(r + 1, 'Monthly Value is less than or equals 0'))

    def wait_logo_appear(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo_click_xpath)))
        except Exception as e:
            print("Element not Found")

    def click_logo(self):
        self.driver.find_element_by_xpath(self.logo_click_xpath).click()

    def logo_refer_check(self):
        element1 = self.driver.find_element_by_xpath(self.chart_xpath).is_displayed()
        print("Dashboard Is Displayed = ", element1)
        print("######################################")

    def chart_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.chart_xpath).is_displayed()
        print("chart Is Displayed = ", element1)

    def click_electricity(self):
        self.driver.find_element_by_xpath(self.electricity_xpath).click()
        print("Electricity Refers Electricity Graph")

    def electricity_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.electricity_xpath).is_displayed()
        print("Electricity Is Displayed = ", element1)

    def click_water(self):
        self.driver.find_element_by_xpath(self.water_xpath).click()
        print("Water Refers Water Graph")

    def water_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.water_xpath).is_displayed()
        print("Water Is Displayed = ", element1)

    def click_heat(self):
        self.driver.find_element_by_xpath(self.heat_xpath).click()
        print("Heat Refers Heat Graph")
        print("######################################")

    def heat_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.heat_xpath).is_displayed()
        print("Heat Is Displayed = ", element1)

    def portfolio_monthly_visible_check(self):
        element1 = self.driver.find_element_by_xpath(self.portfolio_monthly_xpath).is_displayed()
        print("Portfolio Monthly Is Displayed = ", element1)
        print("######################################")

    def click_bell_icon(self):
        self.driver.find_element_by_xpath(self.notification_icon_xpath).click()
        print("Side Notification open")

    def close_notifiaction(self):
        self.driver.find_element_by_xpath(self.notification_feed_close_xpath).click()
        print("Side Notification closed")
        print("######################################")

    def click_expand_dashboard_icon(self):
        self.driver.find_element_by_xpath(self.expand_map_xpath).click()
        print("Clicked Expand Map")

    def expand_portfolio_display_check(self):
        element1 = self.driver.find_element_by_xpath(self.portfolio_monthly_xpath).is_displayed()
        print("Portfolio monthly is Visible ? = ", element1)
        print("######################################")

    def click_collapse_dashboard_icon(self):
        self.driver.find_element_by_xpath(self.collapse_map_xpath).click()
        print("Clicked Collapse Map")

    def google_map_toogle_zoom(self):
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath(self.google_zoomin_xpath).click()
        self.driver.find_element_by_xpath(self.google_zoomout_xpath).click()
        print("Google zoom in - out working")

    def google_map_toogle_fullscreen(self):
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_xpath(self.google_fullscreen_max_min_xpath).click()
        self.driver.find_element_by_xpath(self.google_fullscreen_max_min_xpath).click()
        print("Google full screen toogle =  working")
        print("######################################")
