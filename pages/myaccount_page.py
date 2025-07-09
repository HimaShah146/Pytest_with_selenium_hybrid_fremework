from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from pages.base_page import BasePage


class MyAccount(BasePage):
    def __init__(self,driver = WebDriver):
        super().__init__(driver)

    MY_ACCOUNT_TEXT = (By.XPATH,"//div[@id='content']/h2[1]")

    def success_login(self):
        return self.retrive_text(self.MY_ACCOUNT_TEXT)