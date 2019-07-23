import sys
import os
sys.path.append(os.path.dirname(sys.path[0]+"\Locators"))
from Locators.Locators import  locators


class Loginpage():

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_xpath = locators.email_textbox_xpath
        self.password_textbox_xpath = locators.password_textbox_xpath
        self.login_button_xpath = locators.login_button_xpath
        self.Invalid_Credential_text_xpath = locators.Invalid_Credential_text_xpath
        self.valid_Credential_text_xpath = locators.valid_Credential_text_xpath

    def enter_email(self, email):
        self.driver.find_element_by_xpath(self.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.email_textbox_xpath).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def Invalid_Credential_text(self):
        element1 = self.driver.find_element_by_xpath(self.Invalid_Credential_text_xpath).is_displayed()
        print("Incorrect Credential popup visible = ", element1)

    def valid_Credential_text(self):
        try:
            assert "Dashboard" in self.driver.find_element_by_xpath(self.valid_Credential_text_xpath).text
            print("Logged in = Passed")
        except Exception as e:
            print("Logged in = Failed")









