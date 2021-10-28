from selenium.webdriver.common.by import By

class SearchCustomer:
    hideMenu_xpath="//i[@class='far fa-angle-down']"
    txtEmail_id="SearchEmail"
    txtFirstname_id="SearchFirstName"
    txtLastname_id="SearchLastName"
    btnSearch_id="search-customers"

    tableSerchResults_xpath="//table[@role='grid']"
    table_xpath="//table[@id='customers-grid']"
    tableRows_xpath="//table[@id='customers-grid']//tbody//tr"
    tableColumns_xpath="//table[@id='customers-grid']//tbody/tr/td"


    def __init__(self,driver):
        self.driver = driver

    def clickOnHide(self):
        self.driver.find_element(By.XPATH, self.hideMenu_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_keys(email)

    def setFirstname(self,firstName):
        self.driver.find_element(By.ID, self.txtFirstname_id).send_keys(firstName)
    def setLastname(self,lastName):
        self.driver.find_element(By.ID, self.txtLastname_id).send_keys(lastName)

    def clickOnSearch(self):
        self.driver.find_element(By.ID, self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumn(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumns_xpath))



    def searchCustomerByEmail(self,mail):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element(By.XPATH, self.table_xpath)
            emailID=table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + " ]/td[2]").text
            if emailID==mail:
                flag=True
                break
        return flag

    def searchByCustomerName(self,Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + " ]/td[3]").text
            print(name)
            if name == Name:
                flag = True
                break
        return flag


