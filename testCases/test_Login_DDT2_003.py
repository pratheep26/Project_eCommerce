import time

import pytest
from selenium import webdriver
import logging
from pageObjects.Login_PageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger
from utilities import XLUtilies

class Test_Login_DDT_003:
    baseURL=ReadConfig.getApplicationURL()
    path=".\\TestData\\LoginDataWithOutExp.xlsx"

    logger=custom_Logger.custstomLogger()

    def test_login_DDT2(self,setup):
        self.logger.info("Starting - Test_Login_DDT_003")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating To Application")
        self.loginPageobjects=LoginPage(self.driver)

        self.logger.info("Verifying Login DDT Test")

        self.rows=XLUtilies.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:",self.rows)

        for r in range(2, self.rows + 1):
            self.userName = XLUtilies.readData(self.path, "Sheet1", r, 1)
            self.pwd = XLUtilies.readData(self.path, "Sheet1", r, 2)

            self.loginPageobjects.setUserName(self.userName)
            self.loginPageobjects.setPassword(self.pwd)
            self.loginPageobjects.clickLogin()

            actTitle = self.driver.title
            exptitle = "Dashboard / nopCommerce administration"

            if actTitle == exptitle:
                print("Test is passed")
                self.loginPageobjects.clickLogout()
                XLUtilies.writeData(self.path, "Sheet1", r, 3, "Test passed")
            else:
                print("Test is passed")
                XLUtilies.writeData(self.path, "Sheet1", r, 3, "Test failed")

        self.driver.close()

        self.logger.info("---------------Completed - Test_Login_DDT_003----------------")
