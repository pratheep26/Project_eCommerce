from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id="Email"
    textbox_passwor_id="Password"
    button_login_xpath="//button[contains(text(),'Log in')]"
    link_logout_linktext="Logout"

    def __init__(self,driver):   #This is constructor (It will automatically invoke at teh time of object creation).
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_passwor_id).clear()
        self.driver.find_element(By.ID,self.textbox_passwor_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()

