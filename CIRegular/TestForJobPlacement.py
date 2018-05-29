from selenium import webdriver
from selenium.webdriver.common import keys




driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://ci.linuxjobber.com")

login_attempt = driver.find_element_by_link_text("Job Placement Program")
login_attempt.click()

click_attempt = driver.find_element_by_xpath("//a[@href='/Jobplacements/apply']")
click_attempt.click()

firstName = driver.find_element_by_id("firstname")
firstName.send_keys("ADETUNJ")

lastName = driver.find_element_by_id("lastname")
lastName.send_keys("OLUGBENGA")

emailAddress = driver.find_element_by_id("email")
emailAddress.send_keys("adeolu@gmail.com")

elect = driver.find_element_by_xpath("//select[@name='data[Jobplacements][education]']/option[text()='Some High School']").click()

#upload the file
elm = driver.find_element_by_name("data[Jobplacements][resume]").send_keys("C:\\adetunji.docx")


submit = driver.find_element_by_xpath("//*[@type='submit']")
submit.click()

careerInterest = driver.find_element_by_xpath("//select[@name='data[Jobplacements][career]']/option[text()='DevOps']").click()

experience = driver.find_element_by_xpath("//select[@name='data[Jobplacements][experience]']/option[text()='1']").click()

cert = driver.find_element_by_xpath("//select[@name='data[Jobplacements][certification]']/option[text()='Yes']").click()

field = driver.find_element_by_xpath("//select[@name='data[Jobplacements][training]']/option[text()='No']").click()

willness = driver.find_element_by_xpath("//select[@name='data[Jobplacements][williness]']/option[text()='Yes']").click()

select = driver.find_element_by_xpath("//*[@type='submit']")
select.click()

decision = driver.find_element_by_xpath(".//a[@href ='/Jobplacements']").click()