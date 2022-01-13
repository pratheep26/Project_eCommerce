import xlrd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuItem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddNew_xpath="//a[normalize-space()='Add new']"
    txtEmail_id="Email"
    txtPassword_id="Password"
    txtFirstname_id="FirstName"
    txtLastname_id="LastName"
    rdMale_id="Gender_Male"
    rdFemale_id="Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    cbTax_xpath = "//input[@id='IsTaxExempt']"
    txtDeletedefault_xpath="//span[@title='delete']"
    txtCustomerRoles_xpath="//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    liGuests_xpath = "//span[normalize-space()='Guests']"
    drpVendor_id="VendorId"
    cbActive_xpath = "//input[@id='Active']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickOncustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menuItem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH, self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setPwd(self,password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_keys(password)

    def setFirstname(self,firstname):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstname)

    def setLasttname(self,lastname):
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastname)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.ID, self.rdMale_id).click()
        elif gender=='Female':
            self.driver.find_element(By.ID, self.rdFemale_id).click()

    def setDOB(self,dob):
        self.driver.find_element(By.XPATH, self.txtDOB_xpath).send_keys(dob)

    def setCompanyName(self,cName):
        self.driver.find_element(By.XPATH, self.txtCompanyName_xpath).send_keys(cName)

    def deleteDefault(self):
        self.driver.find_element(By.XPATH, self.txtDeletedefault_xpath).click()

    def setVendor(self,value):
        dropdown=self.driver.find_element(By.ID, self.drpVendor_id)
        drp=Select(dropdown)
        drp.select_by_visible_text(value)

    def setAdminComment(self, adminComment):
        self.driver.find_element(By.XPATH, self.txtAdminComment_xpath).send_keys(adminComment)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btnSave_xpath).click()








