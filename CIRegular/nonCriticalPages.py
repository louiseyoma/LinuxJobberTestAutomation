from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://test.linuxjobber.com/tutorials/awsstart")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/users/orderlist")

driver.implicitly_wait(15)

driver.get("http:test.linuxjobber.com/newlabs/uploaded")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/newlabs/labs")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/tutorials/linuxstart")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/labprofiles")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/companys/aboutus")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/companys/policy")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com/companys/location")





