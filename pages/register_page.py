from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self,driver = WebDriver):
        super().__init__(driver)

    FIRST_NAME_FIELD = (By.ID, "input-firstname")
    LAST_NAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    PASSWORD_FIELD = (By.ID, "input-password")
    CONFIRM_PASSWORD_FIELD = (By.ID, "input-confirm")
    PRIVACY_POLICY_CHECKBOX = (By.NAME, "agree")
    NEWSLETTER_RADIOBUTTON = (By.CSS_SELECTOR,"input[value='1'][name='newsletter']")
    REGISTER_BUTTON = (By.XPATH,"//div[@class='pull-right']/input[2]")

    ERROR_MESSAGES = {
        "first_name": (By.XPATH,"//div[contains(text(),'First Name must be between 1 and 32 characters!')]"),
        "last_name" : (By.XPATH,"//div[contains(text(),'Last Name must be between 1 and 32 characters!')]"),
        "email": (By.XPATH,"//div[contains(text(),'E-Mail Address does not appear to be valid!')]"),
        "password": (By.XPATH,"//div[contains(text(),'Password must be between 4 and 20 characters!')]"),
        "telephone": (By.XPATH,"//div[contains(text(),'Telephone must be between 3 and 32 characters!')]"),
        "confirm_password": (By.XPATH,"//div[contains(text(),'Password confirmation does not match password!')]"),
        "user_exist":(By.XPATH,"//div[@id='account-register']/div[1]")
    }

    def register_application(self,first,last,email,phone,password,confirm_password,yes):
        self.send_keys(self.FIRST_NAME_FIELD, first)
        self.send_keys(self.LAST_NAME_FIELD, last)
        self.send_keys(self.EMAIL_FIELD, email)
        self.send_keys(self.TELEPHONE_FIELD, phone)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.send_keys(self.CONFIRM_PASSWORD_FIELD, confirm_password)
        if yes == "Yes":
            self.click(self.NEWSLETTER_RADIOBUTTON)
        self.click(self.PRIVACY_POLICY_CHECKBOX)
        return self.click(self.REGISTER_BUTTON)

    def get_error_message_by_text(self, key):
        locator = self.ERROR_MESSAGES.get(key)
        if locator:
            return self.get_element(locator).text
        return None
