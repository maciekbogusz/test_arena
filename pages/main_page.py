from utils.locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = MainPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def get_username(self):
        self.wait_for_element(self.locator.USER_INFO)
        return self.driver.find_element(*self.locator.USER_INFO).text