import os.path
import Drivers

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
       path=Service(".\\Drivers\\chromedriver.exe")
       driver=webdriver.Chrome(service=path)
       print("Launching chrome browser.......")
    elif browser=='firefox':
        path=Service(".\\Drivers\\geckodriver.exe")
        driver=webdriver.Firefox(service=path)
        print("Launching Firefox browser....")
    else:
        path=Service(".\\Drivers\\IEDriverServer.exe")
        driver=webdriver.Ie(service=path)
        print("Launching IE Browser....")
    return driver
 
def pytest_addoption(parser):  # This will return value from CLI/hooks.
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):    # This will return the Browser value to setup method.
    return request.config.getoption("--browser")

def pytest_html_report_title(report):
    report.title = "eCommerce Web App Automation_Report"


########### PyTest HTML Report ##############

#It is hook for adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'eCommerce App'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pradeep'




#It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



