from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class BasePage:
    def __init__(self, driver : WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_element(self, locator):
        """Wait for element to be present and return it."""
        return self.wait.until(ec.presence_of_element_located(locator))

    def click(self, locator):
        """Wait and click on an element."""
        self.get_element(locator).click()

    def send_keys(self, locator, text):
        """Clear and enter text into a field."""
        element = self.get_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def retrive_text(self,locator):
        self.get_element(locator).is_displayed()
        return self.get_element(locator).text

