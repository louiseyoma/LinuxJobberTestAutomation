from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")

driver.implicitly_wait(10)


driver.get("http://test.linuxjobber.com")


logIn = driver.find_element_by_xpath(".//a[@href='/users/login']").click()

userName = driver.find_element_by_id("username")
userName.send_keys("louiseyoma")

password = driver.find_element_by_id("password")
password.send_keys("password")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

select_courses_dropdown = driver.find_element_by_xpath(".//*[@id='header']/div/div/div/div[2]/nav/ul/li[1]/a").click()

select_linuxfundamentals = driver.find_element_by_xpath(".//*[@id='course']/div/div[1]/ul/li[1]/a[1]").click()

select_sisth_quiz = driver.find_element_by_xpath(".//*[@id='myList']/div[8]/div[3]/a/img").click()

#Start answering quiz questions

question1 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[2]/td[2]/ul/li[1]/input").click()
question2 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[3]/td[2]/ul/li[2]/input").click()
question3 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[4]/td[2]/ul/li[2]/input").click()
question4 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[5]/td[2]/ul/li[3]/input").click()
question5 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[6]/td[2]/ul/li[4]/input").click()
question6 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[7]/td[2]/ul/li[3]/input").click()
question7 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[8]/td[2]/ul/li[1]/input").click()
question8 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[9]/td[2]/ul/li[4]/input").click()
question9 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[10]/td[2]/ul/li[2]/input").click()
question10 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[11]/td[2]/ul/li[2]/input").click()
question10 = driver.find_element_by_xpath(".//*[@id='formId']/table/tbody/tr[12]/td[2]/ul/li[2]/input").click()

driver.find_element_by_id('finish').click()

