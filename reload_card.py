from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from landing_page import LandingPage
from very_simple_logger import VerySimpleLogger
import os
import json
import time
import keyring

config_file = "config.json"


def get_config():
    script_path = os.path.realpath(__file__)
    script_folder, script = os.path.split(script_path)
    config_path = os.path.join(script_folder, config_file)
    with open(config_path, 'r') as json_config:
        config = json.load(json_config)
        return config


def set_webdriver_options(headless_mode=False):
    my_options = Options()
    my_options.log.level = "error"
    my_options.headless = headless_mode  # Headless must be true if running from a cron task.
    return my_options


def set_webdriver_capabilities():
    my_capabilities = DesiredCapabilities().FIREFOX
    my_capabilities["marionette"] = True
    return my_capabilities


def set_webdriver_profile():
    my_profile = webdriver.FirefoxProfile()
    my_profile.set_preference("dom.webdriver.enabled", False)  # Site errors if it detects webdriver control.
    my_profile.set_preference('useAutomationExtension', False)
    my_profile.update_preferences()
    return my_profile


def get_password(config_dictionary):
    password = keyring.get_password(config_dictionary['application_name'], config_dictionary['user_name'])
    if password is None or len(password) <= 0:
        raise ValueError("Password for user is undefined or empty.")
    return password


def main():
    configuration_error = 1
    webdriver_error = 2
    config = None
    password = None

    try:
        config = get_config()
    except OSError as config_file_error:
        print(f"Error: Failed to read config file {config_file}: \n{config_file_error} \nExiting.")
        exit(configuration_error)

    logger = VerySimpleLogger(file_path=config['log_path'])

    try:
        password = get_password(config)
    except ValueError as value_error:
        logger.log_message(value_error)
        exit(configuration_error)

    logger.log_message("Preparing options, capabilities, and profile")
    driver_options = set_webdriver_options(headless_mode=config['headless_mode'])
    driver_capabilities = set_webdriver_capabilities()
    profile = set_webdriver_profile()
    logger.log_message("Instantiating webdriver")
    driver = None

    try:
        driver = webdriver.Firefox(firefox_profile=profile,
                                   capabilities=driver_capabilities,
                                   options=driver_options,
                                   firefox_binary=config['firefox_binary_path'],
                                   executable_path=config['gecko_driver_path']
                                   )
    except Exception as e:
        logger.log_message(f"Failed to instantiate webdriver: {e}")
        exit(webdriver_error)

    try:
        logger.log_message("Visiting landing page")
        landing_page = LandingPage(driver)

        logger.log_message("Visiting login page")
        login_page = landing_page.navigate_to_login_page()

        logger.log_message("Visiting offers page")
        offers_page = login_page.perform_login(config['user_name'], password)
        offers_page.load_offers()
        time.sleep(3)  # Wait until the points animation finishes counting.
        points_available = offers_page.get_accumulated_points()
        logger.log_message("Points available: " + points_available)
        offers_page.sign_out()
        logger.log_message("Signed out")
        time.sleep(2)
    except Exception as e:
        logger.log_message(f"Error while navigating pages: {e}")
    finally:
        driver.quit()
        logger.log_message("Quit driver")


if __name__ == "__main__":
    main()
