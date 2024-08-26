from email.mime.audio import MIMEAudio

from pages.base_test import BaseTest
from pages.login_page import LoginPage
from pages.main_page import MainPage
from utils.locators import MainPageLocators


class TestLogin(BaseTest):

    def test_successful_login(self):
        login_page = LoginPage(self.driver)
        main_page = MainPage(self.driver)
        login_page.login("administrator@testarena.pl", "sumXQQ72$L")
        assert main_page.get_username() is not None

    def test_invalid_login(self):
        login_page = LoginPage(self.driver)
        login_page.login("administrator@", "sumXQQ72$L")
        assert login_page.get_error_message_text() == "Nieprawidłowy format adresu e-mail. Wprowadź adres ponownie."
