from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, selenium_driver, url):
        self.driver = selenium_driver
        self.url = url
        self.implicit_wait_time_seconds = 5
        self.driver.implicitly_wait(self.implicit_wait_time_seconds)
        self.explicit_wait_time_seconds = 10
        self.polling_interval_seconds = 1.0
        self.wait = WebDriverWait(self.driver, self.explicit_wait_time_seconds, self.polling_interval_seconds)

    def open(self):
        self.driver.get(self.url)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
