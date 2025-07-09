from pycparser.c_ast import Return
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.myaccount_page import MyAccount


class LoginPage(BasePage):

    def __init__(self,driver:WebDriver):
        super().__init__(driver)

    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Login']")
    ERROR_MESSAGES ={
        "email_pass_error_mess" : (By.CSS_SELECTOR,".alert.alert-danger.alert-dismissible")
    }

    def login_application(self, email, password):
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
        return MyAccount(self.driver)

    def get_error_message_by_text(self, key):
        locator = self.ERROR_MESSAGES.get(key)
        if locator:
            return self.get_element(locator).text
        return None
