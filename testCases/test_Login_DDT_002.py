import time

import pytest
from selenium import webdriver
import logging
from pageObjects.Login_PageObjects import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger
from utilities import XLUtilies


class Test_Login_DDT_002:
    baseURL=ReadConfig.getApplicationURL()
    path=".\\TestData\\LoginData.xlsx"

    logger=custom_Logger.custstomLogger()

    @pytest.mark.regression
    def test_login_DDT(self,setup):
        self.logger.info("Starting - Test_Login_DDT_002")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating To Application")
        self.loginPageobjects=LoginPage(self.driver)

        self.logger.info("Verifying Login DDT Test")

        self.rows=XLUtilies.getRowCount(self.path,'Sheet1')
        print("Number of rows in Excel:",self.rows)

        lst_status=[]    #Empty list Variable

        for xlRows in range(2,self.rows+1):
            self.userName=XLUtilies.readData(self.path,'Sheet1',xlRows,1)
            self.pwd=XLUtilies.readData(self.path,'Sheet1',xlRows,2)
            self.EXP_Result=XLUtilies.readData(self.path,'Sheet1',xlRows,3)

            self.loginPageobjects.setUserName(self.userName)
            self.loginPageobjects.setPassword(self.pwd)
            time.sleep(2)
            self.loginPageobjects.clickLogin()
            time.sleep(3)

            actTitle=self.driver.title
            exptitle="Dashboard / nopCommerce administration"

            if actTitle==exptitle:
                if self.EXP_Result=="Pass":
                    self.logger.info("Test passed")
                    self.loginPageobjects.clickLogout()
                    lst_status.append("Passed")

                elif self.EXP_Result=="Fail":
                    self.logger.info("Test Failed")
                    self.loginPageobjects.clickLogout()
                    lst_status.append("failed")

            elif actTitle != exptitle:
                if self.EXP_Result=="Pass":
                    self.logger.info("Test Failed")
                    lst_status.append("Fail")
                elif self.EXP_Result=="Fail":
                    self.logger.info("Test passed")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test failed")
            self.driver.close()
            assert False

        self.logger.info("---------------Completed - Test_Login_DDT_002----------------")
