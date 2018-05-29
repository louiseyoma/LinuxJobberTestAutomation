from selenium import webdriver
from selenium.webdriver.common import keys

#driver = webdriver.Chrome("C:/Users/Oluwafemi/Documents/sir akej sys/chromedriver.exe")

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")

driver.get("http://test.linuxjobber.com")

#driver.implicitly_wait(5)


click = driver.find_element_by_xpath("//a[@href='/users/login']")
click.click()


userName = driver.find_element_by_id("UserUsername")
userName.send_keys("sirbossakej")

select = driver.find_element_by_xpath("//a[@href='/users/reset']")
select.click()

userName = driver.find_element_by_id("UserEmail")
userName.send_keys("sirbossakej@gmail.com")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()