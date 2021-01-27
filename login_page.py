from page_object import BasePage
from offers_page import OffersPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    email_input_id = 'email'
    password_input_id = 'password'
    sign_in_button_css = '#login > fieldset > button'

    def __init__(self, driver):
        super().__init__(driver, 'https://www.pcoptimum.ca/login')

    def perform_login(self, username: object, password: object):
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, self.email_input_id)))
        self._email_input().send_keys(username)
        self.wait.until(expected_conditions.element_to_be_clickable((By.ID, self.password_input_id)))
        self._password_input().send_keys(password)
        self.wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in_button_css)))
        self._sign_in_button().click()
        return OffersPage(self.driver)

    def _email_input(self):
        return self.driver.find_element_by_id(self.email_input_id)

    def _password_input(self):
        return self.driver.find_element_by_id(self.password_input_id)

    def _sign_in_button(self):
        return self.driver.find_element_by_css_selector(self.sign_in_button_css)
