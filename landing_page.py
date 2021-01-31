from page_object import BasePage
from login_page import LoginPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    sign_in_link_xpath = '/html/body/div[1]/div/div/nav/section/ul[2]/li[1]/a'

    def __init__(self, driver):
        super().__init__(driver, 'https://www.pcoptimum.ca/')

    def navigate_to_login_page(self):
        self.open()
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.sign_in_link_xpath)))
        self._sign_in_link().click()
        return LoginPage(self.driver)

    def _sign_in_link(self):
        return self.driver.find_element_by_xpath(self.sign_in_link_xpath)
