import time
import pytest
from selenium.webdriver.chrome import webdriver
from pages import home_page
from tests.BaseTest import BaseTest
from utilities import excel_reader

class TestLogin(BaseTest):
    driver: webdriver

    @pytest.mark.parametrize("email,password",
                             excel_reader.get_data_by_scenario_login("Excel_Files/Login_Page_Pytest_Selenium.xlsx", "login",
                                                               "empty_email_password"))
    def test_empty_fields(self,email,password):
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        login.login_application(email,password)
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.")

    @pytest.mark.parametrize("email,password",
                             excel_reader.get_data_by_scenario_login("Excel_Files/Login_Page_Pytest_Selenium.xlsx", "login",
                                                               "invalid_email"))
    def test_invalid_email(self,email,password):
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        # login.login_application("abcalian365615@gmail.com","Abc@Alian123")
        login.login_application(email,password)
        self.driver.save_screenshot("screenshots/test_invalid_email.png")
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.") or login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.")

    @pytest.mark.parametrize("email,password",
                             excel_reader.get_data_by_scenario_login("Excel_Files/Login_Page_Pytest_Selenium.xlsx", "login",
                                                               "invalid_password"))
    def test_invalid_password(self,email,password):
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        # login.login_application("abcalian@gmail.com","Abc@Alian123$%$%")
        login.login_application(email,password)
        self.driver.save_screenshot("screenshots/test_invalid_password.png")
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.")

    @pytest.mark.parametrize("email,password",excel_reader.get_data_by_scenario_login("Excel_Files/Login_Page_Pytest_Selenium.xlsx","login","valid_login"))
    def test_valid_login(self,email,password):
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        # account = login.login_application("abcalian@gmail.com","Abc@Alian123")
        account = login.login_application(email,password)
        time.sleep(1)
        assert account.success_login()