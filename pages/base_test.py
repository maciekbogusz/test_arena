import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://demo.testarena.pl/zaloguj")

    def tearDown(self):
        self.driver.close()
