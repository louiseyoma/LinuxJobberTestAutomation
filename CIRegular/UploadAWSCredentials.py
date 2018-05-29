from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://ci.linuxjobber.com")


logIn = driver.find_element_by_xpath(".//a[@href='/users/login']").click()

userName = driver.find_element_by_id("UserUsername")
userName.send_keys("janeright")

password = driver.find_element_by_id("UserPassword")
password.send_keys("samjam1989")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

go = driver.find_element_by_xpath('//a[contains(text(), "janeright")]').click()

select = driver.get("http://ci.linuxjobber.com/users/accountSetting")

elm = driver.find_element_by_name("data[csvfile]").send_keys("C:\\credentials.csv")

upload = driver.find_element_by_xpath("//*[@type='submit']").click()