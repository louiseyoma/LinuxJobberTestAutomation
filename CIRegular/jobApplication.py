from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://test.linuxjobber.com/companys/jobs")

driver.find_element_by_link_text('Apply').click()

driver.find_element_by_id('JobFname').send_keys('')

driver.find_element_by_id('JobLname').send_keys('')

driver.find_element_by_id('JobEmail').send_keys('')

driver.find_element_by_id('JobFname').send_keys('')

driver.find_element_by_id('JobPhone').send_keys('')

driver.find_element_by_id('JobResume').send_keys('')

driver.find_element_by_xpath("//*[@type='submit']").click()