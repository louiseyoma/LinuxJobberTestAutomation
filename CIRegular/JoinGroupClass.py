from selenium import webdriver
from selenium.webdriver.common import keys

driver = webdriver.Chrome("C:/Users/Louis/LinuxjobberWorkSpace/LinuxJobberAutomationWithPython/chromedriver.exe")


driver.get("http://ci.linuxjobber.com")

driver.implicitly_wait(10)


click = driver.find_element_by_xpath("//a[@href='http://ci.linuxjobber.com/users/groupCourse']")
click.click()

userName = driver.find_element_by_id("fullname")
userName.send_keys("janer")

mail = driver.find_element_by_id("email")
mail.send_keys("mjm@gmail.com")

real = driver.find_element_by_id("password")
real.send_keys("1234")

payCard = driver.get("http://ci.linuxjobber.com/users/grouppaynow")

userName = driver.find_element_by_id("UserUsername")
userName.send_keys("sirbossakej")

password = driver.find_element_by_id("UserPassword")
password.send_keys("dkingstonboss")

sign =  driver.find_element_by_xpath("//*[@type='submit']")
sign.click()

signPay = driver.find_element_by_xpath("//*[@type='submit']")
signPay.click()


#driver.switch_to.frame("stripe_checkout_app")

#mail =  driver.find_element_by_xpath("//*[@placeholder='Email']")
#mail.send_keys("mjm@gmail.com")

#cardNumber =  driver.find_element_by_xpath("//*[@type='tel']")
#cardNumber.send_keys("42424242424242424")

#date = driver.find_element_by_xpath("//*[@placeholder='MM / YY']")
#date.send_keys("0318")

#cvc = driver.find_element_by_xpath("//*[@placeholder='CVC']")
#cvc.send_keys("1234")

#pay = driver.find_element_by_xpath("//*[@type='submit']")
#pay.click()

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