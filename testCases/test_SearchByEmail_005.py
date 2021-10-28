import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.Login_PageObjects import LoginPage
from pageObjects.AddCustomer_PageObjects import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger
from pageObjects.SearchCustomer_PageObjects import SearchCustomer
import string
import random

class Test_SearchByEmail_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    pwd = ReadConfig.getPassword()

    logger=custom_Logger.custstomLogger()

    @pytest.mark.regression
    def test_searchByEmail(self,setup):
        self.logger.info("Starting - Test_SearchByEmail_005")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating To an Application")
        self.driver.maximize_window()

        self.loginPageObj=LoginPage(self.driver)
        self.loginPageObj.setUserName(self.username)
        self.loginPageObj.setPassword(self.pwd)
        self.loginPageObj.clickLogin()

        self.logger.info("Login Successful")

        self.logger.info("Starting search Customer by Email")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOncustomerMenuItem()

        self.logger.info("Search Customer By Email")

        emailSearch=SearchCustomer(self.driver)
        emailSearch.setEmail("victoria_victoria@nopCommerce.com")
        emailSearch.clickOnSearch()
        time.sleep(3)
        status=emailSearch.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True==status

        self.logger.info("---------------Completed - Test_SearchByEmail_005----------------")

        self.driver.close()
