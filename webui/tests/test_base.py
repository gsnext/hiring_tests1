import unittest
from selenium import webdriver
from config import TestConfig
from webui.pages.base_page import LoginPage


class TestBase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(TestConfig.url)
        login_page = LoginPage(self.driver)
        login_page.login(TestConfig.username, TestConfig.password)

    @classmethod
    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
