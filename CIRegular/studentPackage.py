from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://ci.linuxjobber.com")

driver.implicitly_wait(10)

click_attempt = driver.find_element_by_xpath("//a[@href = 'http://ci.linuxjobber.com/homes/packages' ]")
click_attempt.click()

signUp = driver.find_element_by_xpath("//a[@href = 'http://ci.linuxjobber.com/tryservices/package/standard']")
signUp.click()

name = driver.find_element_by_id("fname")
name.send_keys("adetunji")

lastName = driver.find_element_by_id("lname")
lastName.send_keys("olugbenga")

mail = driver.find_element_by_id("email")
mail.send_keys("udd@gmail.com")

submit = driver.find_element_by_xpath("//*[@type='submit']")
submit.click()


signPay = driver.find_element_by_xpath("//*[@type='submit']")
signPay.click()


driver.switch_to.frame("stripe_checkout_app")

cardNumber =  driver.find_element_by_xpath("//*[@type='tel']")
cardNumber.send_keys("42424242424242424")

date = driver.find_element_by_xpath("//*[@placeholder='MM / YY']")
date.send_keys("0318")

cvc = driver.find_element_by_xpath("//*[@placeholder='CVC']")
cvc.send_keys("1234")

pay = driver.find_element_by_xpath("//*[@type='submit']")
pay.click()

day = driver.find_element_by_xpath("//select[@name='data[Schedule][day]']/option[text()='Tuesday']")
day.click()

time = driver.find_element_by_xpath("//select[@name='data[Schedule][time]']/option[text()='00:30:00']")
time.click()

ar = driver.find_element_by_xpath("//select[@name='data[Schedule][mode]']/option[text()='pm']")
ar.click()

day2 = driver.find_element_by_xpath("//select[@name='data[Schedule][day_2]']/option[text()='Monday']")
day2.click()

time2 = driver.find_element_by_xpath("//select[@name='data[Schedule][time_2]']/option[text()='01:00:00']")
time2.click()

ar2 = driver.find_element_by_xpath("//select[@name='data[Schedule][mode_2]']/option[text()='pm']")
ar2.click()

lastName = driver.find_element_by_id("phone")
lastName.send_keys("55555555")

submit = driver.find_element_by_xpath("//*[@type='submit']")
submit.click()