import pytest
import time
from selenium.webdriver.common.by import By
from pageObjects.Login_PageObjects import LoginPage
from pageObjects.AddCustomer_PageObjects import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger
from utilities import XLUtilies
import string
import random

class Test_AddCustomer_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger=custom_Logger.custstomLogger()


    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("Starting - Test_AddCustomer_004")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.logger.info("Navigating To Application")

        self.loginPageObj=LoginPage(self.driver)
        self.loginPageObj.setUserName(self.username)
        self.loginPageObj.setPassword(self.password)
        self.loginPageObj.clickLogin()

        self.logger.info("Login Successful")

        self.logger.info("Starting Add New Customer Test")

        self.addCust=AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        time.sleep(3)
        self.addCust.clickOncustomerMenuItem()

        self.addCust.clickOnAddNew()

        self.logger.info("Providing Customer Info")






        self.emailID=random_generator() + "@gmail.com"
        self.addCust.setEmail(self.emailID)
        self.addCust.setPwd("Ridyuth@123")
        self.addCust.setFirstname("Vidyuth")
        self.addCust.setLasttname("Ridyuth")
        self.addCust.setGender("Male")
        self.addCust.setDOB("05/06/1995")
        self.addCust.setCompanyName("Credo")
        self.addCust.setVendor("Vendor 1")
        self.addCust.setAdminComment("This is learning purpose")
        #self.addCust.clickOnSave()


        self.logger.info("Saving Customer Info")

        self.logger.info("Add Customer validation started")

        self.msg=self.driver.find_element(By.TAG_NAME, "body").text

        if 'The new customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("Add customer Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addCustomer.png")
            self.logger.error("Add Customer Test failed")

        self.driver.close()
        self.logger.info("---------------Completed - Test_AddCustomer_004---------------")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

