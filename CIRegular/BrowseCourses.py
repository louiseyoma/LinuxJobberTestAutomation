from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")

#driver = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver.exe")

driver.implicitly_wait(15)

driver.get("http://test.linuxjobber.com")

driver.execute_script("window.scrollTo(1,10);")

click = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/LINUX-FUNDAMENTALS']")
click.click()

driver.execute_script("window.scrollTo(1,10);")
time.sleep(2)

select = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/']")
select.click()

lick = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/PUPPET-TRAINING']")
lick.click()

driver.execute_script("window.scrollTo(1,10);")

time.sleep(2)
elect = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/']")
elect.click()


ick = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/RHCSA']")
ick.click()

time.sleep(2)

lect = driver.get("http://test.linuxjobber.com")

k = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/JAVA']")
k.click()

driver.execute_script("window.scrollTo(1,10);")

time.sleep(2)

t = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/']")
t.click()

ck = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/AWS']")
ck.click()

driver.execute_script("window.scrollTo(1,10);")

time.sleep(2)

ect = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/']")
ect.click()

k = driver.find_element_by_xpath("//a[@href='http://test.linuxjobber.com/tutorials/coursedescription/BUSINESS-ANALYSIS']")
k.click()