from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

import pytest

from TestData.LoginPageData import LoginPageData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestCases(BaseClass):
    def test_Cases(self, getData):
        log = self.logging()
        loginPage = LoginPage(self.driver)
        log.info("Entering username " + getData["Username"])
        loginPage.getUsername().send_keys(getData["Username"])
        log.info("Entering password " + getData["Password"])
        loginPage.getPassword().send_keys(getData["Password"])
        self.driver.implicitly_wait(5)
        log.info("clicking submit button")
        loginPage.getSubmitButton().click()
        act_title = self.driver.title
        exp_title = "OrangeHRM"
        if act_title == exp_title:
            print("Login Test Passed")
        else:
            print("Login Test Failed")
        loginPage.getProfile().click()
        self.driver.implicitly_wait(5)
        loginPage.getLog0ut().click()

        self.driver.refresh()

    @pytest.fixture(params=LoginPageData.foo())
    def getData(self, request):
        return request.param
