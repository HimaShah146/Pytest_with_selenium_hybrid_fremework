import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from pages import home_page
from tests.BaseTest import BaseTest
from utilities import excel_reader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestLogin(BaseTest):
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # Only log FATAL errors to terminal
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Define log file path
    service = Service(log_path="logs/chromedriver.log")  # Save ChromeDriver logs

    # Create driver
    driver = WebDriver.Chrome(service=service, options=chrome_options)
    # driver: WebDriver

    def test_empty_fields(self):
        time.sleep(20)
        self.driver.save_screenshot("screenshots/test_empty_fields.png")
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        login.login_application("","")
        # WebDriverWait(self.driver, 10).until(
        #     ec.visibility_of_element_located(
        #         (By.XPATH, "//div[contains(text(),'Warning: No match for E-Mail Address and/or Password.')]"))
        # )
        #
        # assert login.get_error_message_by_text("email_pass_error_mess") == \
        #        "Warning: No match for E-Mail Address and/or Password."
        time.sleep(1)
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.")

    @pytest.mark.parametrize("email,password",excel_reader.get_data_from_excel("Excel_Files/Login_Page_Pytest_Selenium.xlsx","Sheet1"))
    def test_invalid_email(self,email,password):
        home = home_page.HomePage(self.driver)
        self.driver.implicitly_wait(10)
        login = home.navigate_to_login()
        # login.login_application("abcalian365615@gmail.com","Abc@Alian123")
        login.login_application("email", "password")
        time.sleep(10)
        self.driver.save_screenshot("screenshots/test_invalid_email.png")
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.") or login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: Your account has exceeded allowed number of login attempts. Please try again in 1 hour.")

    def test_invalid_password(self):
        home = home_page.HomePage(self.driver)
        self.driver.implicitly_wait(10)
        login = home.navigate_to_login()
        login.login_application("abcalian@gmail.com","Abc@Alian123$%$%")
        self.driver.save_screenshot("screenshots/test_invalid_password.png")
        assert login.get_error_message_by_text("email_pass_error_mess").__eq__("Warning: No match for E-Mail Address and/or Password.")

    def test_valid_login(self):
        self.driver.implicitly_wait(10)
        home = home_page.HomePage(self.driver)
        login = home.navigate_to_login()
        account = login.login_application("abcalian@gmail.com","Abc@Alian123")
        time.sleep(1)
        assert account.success_login()