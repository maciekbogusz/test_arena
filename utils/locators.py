
from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    SUBMIT = (By.ID, 'login')
    ERROR_MESSAGE =  (By.CLASS_NAME, "login_form_error")

class MainPageLocators(object):
    USER_INFO = (By.CLASS_NAME, 'user-info')
