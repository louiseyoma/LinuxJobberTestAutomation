from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://test.linuxjobber.com/tryservices")

driver.find_element_by_id('fname').send_keys('')

driver.find_element_by_id('lname').send_keys('')

driver.find_element_by_id('email').send_keys('')

driver.find_element_by_xpath(".//*[@id='Form_1527415349']/fieldset/div[4]/div[2]/div/button").click()

