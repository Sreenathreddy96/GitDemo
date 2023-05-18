import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:/Users/Sreenath/Downloads/chromedriver_win32 (2).exe")

    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    driver.implicitly_wait(4)
    request.cls.driver = driver
    yield
    driver.close()
