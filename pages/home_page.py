from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_my_account_dropdown(self):
        self.driver.find_element(By.XPATH,"//ul[@class='list-inline']/li[2]/a").click()

    def click_login(self):
        self.driver.find_element(By.LINK_TEXT,"Login").click()

    def click_register(self):
        self.driver.find_element(By.LINK_TEXT,"Register").click()

    def navigate_to_register(self):
        self.click_my_account_dropdown()
        self.click_register()
        return RegisterPage(self.driver)

    def navigate_to_login(self):
        self.click_my_account_dropdown()
        self.click_login()
        return LoginPage(self.driver)