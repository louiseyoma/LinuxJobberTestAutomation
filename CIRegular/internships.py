from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://test.linuxjobber.com/internships")

driver.find_element_by_id('InternshipFirst').send_keys('')

driver.find_element_by_id('InternshipSecond').send_keys('')

driver.find_element_by_id('InternshipPhoneNumber').send_keys('')

driver.find_element_by_id('InternshipEmail').send_keys('')

driver.find_element_by_id('InternshipHomeAddress').send_keys('')

driver.find_element_by_id('InternshipSchoolName').send_keys('')

driver.find_element_by_id('InternshipState/country').send_keys('')

driver.find_element_by_id('InternshipCourseTitle').send_keys('')

driver.find_element_by_id('InternshipProgramming').send_keys('')

driver.find_element_by_class_name('btn reg-submit').click('')