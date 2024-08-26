from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import LoginPageLocators


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginPageLocators

    def wait_for_element(self, element):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(element)
        )

    def login(self, username, password):
        self.wait_for_element(self.locator.USERNAME)
        self.wait_for_element(self.locator.PASSWORD)
        self.wait_for_element(self.locator.SUBMIT)
        self.driver.find_element(*self.locator.USERNAME).send_keys(username)
        self.driver.find_element(*self.locator.PASSWORD).send_keys(password)
        self.driver.find_element(*self.locator.SUBMIT).click()

    def get_error_message_text(self):
        self.wait_for_element(self.locator.ERROR_MESSAGE)
        return self.driver.find_element(*self.locator.ERROR_MESSAGE).text