import random
import string
import time

import pytest
from selenium import webdriver
import logging
from pageObjects.Login_PageObjects import LoginPage
from pageObjects.AddCustomer_PageObjects import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import custom_Logger
from utilities import XLUtilies


class Test_Login_DDT_002:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    path = ".\\TestData\\LoginDataWithExp.xlsx"

    logger = custom_Logger.custstomLogger()

    def test_add(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)

        self.loginpo = LoginPage(self.driver)
        self.loginpo.setUserName(self.username)
        self.loginpo.setPassword(self.password)
        self.loginpo.clickLogin()

        self.addmem = AddCustomer(self.driver)
        self.addmem.clickOnCustomerMenu()
        time.sleep(3)
        self.addmem.clickOncustomerMenuItem()
        self.addmem.clickOnAddNew()



        self.rows = XLUtilies.getRowCount(self.path, 'AddCustomer')
        for xlrows in range(2, self.rows+1):
            self.pwd = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 1)
            self.fName = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 2)
            self.lName = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 3)
            self.bday = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 4)
            self.CN = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 5)
            self.comment = XLUtilies.readData(self.path, 'AddCustomer', xlrows, 6)

            self.emailid = random_string() + "@gmail.com"
            self.addmem.setEmail(self.emailid)

            self.addmem.setPwd(self.pwd)
            self.addmem.setFirstname(self.fName)
            self.addmem.setLasttname(self.lName)
            self.addmem.setGender("Male")
            self.addmem.setDOB(self.bday)
            self.addmem.setCompanyName(self.CN)
            self.addmem.setVendor("Vendor 1")
            self.addmem.setAdminComment(self.comment)






def random_string(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))