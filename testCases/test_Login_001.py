import pytest
from selenium import webdriver
import logging
from pageObjects.Login_PageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger


class Test_Login_001:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUserEmail()
    password=ReadConfig.getPassword()

    logger=custom_Logger.custstomLogger()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("Starting - Test_Login_001")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating To Application")
        act_title=self.driver.title
        print(act_title)
        self.logger.info("Verifying the Homepage Title")
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("Homepage Title test is Passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("Homepage Title test is Failed")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("Verifying Login Test")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.loginPageobjects=LoginPage(self.driver)
        self.loginPageobjects.setUserName(self.username)
        self.loginPageobjects.setPassword(self.password)
        self.loginPageobjects.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboar / nopCommerce administration":
            assert True
            self.logger.info("Login Test is Passed")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("Login Test is Failed")
            assert False

            self.logger.info("---------------Completed - Test_Login_001---------------")


