import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from pages import home_page
from tests.BaseTest import BaseTest
from utilities import excel_reader


class TestRegister(BaseTest):
    driver: WebDriver

    @pytest.mark.parametrize("fname,lname,email,phone,password,con_pass,checkbox",excel_reader.get_data_by_scenario_register("Excel_Files/Login_Page_Pytest_Selenium.xlsx","register","empty"))
    def test_empty_form_register(self,fname,lname,email,phone,password,con_pass,checkbox):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        # register.register_application("","","","","","","")
        register.register_application(fname,lname,email,phone,password,con_pass,checkbox)
        time.sleep(1)
        assert register.get_error_message_by_text("first_name").__eq__("First Name must be between 1 and 32 characters!")
        assert register.get_error_message_by_text("last_name").__eq__("Last Name must be between 1 and 32 characters!")
        assert register.get_error_message_by_text("email").__eq__("E-Mail Address does not appear to be valid!")
        assert register.get_error_message_by_text("telephone").__eq__("Telephone must be between 3 and 32 characters!")
        assert register.get_error_message_by_text("password").__eq__("Password must be between 4 and 20 characters!")

    @pytest.mark.parametrize("fname,lname,email,phone,password,con_pass,checkbox",
                             excel_reader.get_data_by_scenario_register("Excel_Files/Login_Page_Pytest_Selenium.xlsx","register",
                                                                        "invalid_password"))
    def test_invalid_password(self,fname,lname,email,phone,password,con_pass,checkbox):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        # register.register_application("Abc","Alian","abcalian@gmail.com","1234567895","Abc@Alian123","Abc@Alian12345%^","Yes")
        register.register_application(fname, lname, email, phone, password, con_pass, checkbox)
        assert register.get_error_message_by_text("confirm_password").__eq__("Password confirmation does not match password!")

    @pytest.mark.parametrize("fname,lname,email,phone,password,con_pass,checkbox",
                             excel_reader.get_data_by_scenario_register("Excel_Files/Login_Page_Pytest_Selenium.xlsx",
                                                                        "register",
                                                                        "user_exist"))
    def test_user_exists(self,fname,lname,email,phone,password,con_pass,checkbox):
        home = home_page.HomePage(self.driver)
        register = home.navigate_to_register()
        # register.register_application("Abc", "Alian", "abcalian@gmail.com", "1234567891", "Abc@Alian123","Abc@Alian123","No")
        register.register_application(fname, lname, email, phone, password, con_pass, checkbox)
        assert register.get_error_message_by_text("user_exist").__eq__("Warning: E-Mail Address is already registered!")