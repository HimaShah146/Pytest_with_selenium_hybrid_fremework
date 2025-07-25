import pytest
from selenium import webdriver
from utilities import ReadConfigurations

# @pytest.fixture(scope="class")
# def setup_class_browser(request):
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://demo.nopcommerce.com/")
#     request.cls.driver = driver
#     yield
#     driver.quit()

@pytest.fixture()
def setup_class_browser(request):
    browser = ReadConfigurations.read_configurations("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise Exception("❌ Please select a supported browser: chrome, firefox, or edge")
    driver.maximize_window()
    url = ReadConfigurations.read_configurations("basic info", "url")
    #app_url = "https://tutorialsninja.com/demo/"
    # if url == app_url:
    #     driver.get("https://tutorialsninja.com/demo/")
    # else:
    #     print("URL is not expected")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()