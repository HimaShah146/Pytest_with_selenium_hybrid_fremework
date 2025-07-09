import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages import home_page
from tests.BaseTest import BaseTest

class TestRegister(BaseTest):
    driver: WebDriver
    def test_empty_form_register(self):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        register.register_application("","","","","","","")
        time.sleep(1)
        assert register.get_error_message_by_text("first_name").__eq__("First Name must be between 1 and 32 characters!")
        assert register.get_error_message_by_text("last_name").__eq__("Last Name must be between 1 and 32 characters!")
        assert register.get_error_message_by_text("email").__eq__("E-Mail Address does not appear to be valid!")
        assert register.get_error_message_by_text("telephone").__eq__("Telephone must be between 3 and 32 characters!")
        assert register.get_error_message_by_text("password").__eq__("Password must be between 4 and 20 characters!")

    def test_invalid_password(self):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        register.register_application("Abc","Alian","abcalian@gmail.com","1234567895","Abc@Alian123","Abc@Alian12345%^","Yes")
        assert register.get_error_message_by_text("confirm_password").__eq__("Password confirmation does not match password!")

    def test_user_exists(self):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        register.register_application("Abc", "Alian", "abcalian@gmail.com", "1234567891", "Abc@Alian123","Abc@Alian123","No")
        assert register.get_error_message_by_text("user_exist").__eq__("Warning: E-Mail Address is already registered!")