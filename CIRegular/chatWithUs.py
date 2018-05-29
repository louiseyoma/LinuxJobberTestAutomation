from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://test.linuxjobber.com/companys/contact")

driver.find_element_by_id('fname').send_keys('')

driver.find_element_by_id('phone').send_keys('')

driver.find_element_by_id('email').send_keys('')

driver.find_element_by_id('subject').send_keys('')

driver.find_element_by_id('message').send_keys('')

driver.find_element_by_xpath(".//*[@id='Form_1527417093']/div[5]/div/input").click()

