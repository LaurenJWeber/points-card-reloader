from page_object import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class OffersPage(BasePage):

    account_button_xpath = '/html/body/div/div/div/nav/section/ul[2]/li/button'
    sign_out_button_xpath = '/ html / body / div / div / div / nav / section / ul[2] / ul / li[5] / a'
    points_css_path = 'div.header-points__points-balance p strong span span'

    def __init__(self, driver):
        super().__init__(driver, 'https://www.pcoptimum.ca/offers')

    def load_offers(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.account_button_xpath)))
        self.scroll_to_bottom()
        self.scroll_to_top()

    def get_accumulated_points(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.points_css_path)))
        return self._points_display().text

    def sign_out(self):
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.account_button_xpath)))
        self._account_button().click()
        self.wait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.sign_out_button_xpath)))
        self._sign_out_button().click()

    def _account_button(self):
        return self.driver.find_element_by_xpath(self.account_button_xpath)

    def _sign_out_button(self):
        return self.driver.find_element_by_xpath(self.sign_out_button_xpath)

    def _points_display(self):
        return self.driver.find_element_by_css_selector(self.points_css_path)
