from time import sleep, strftime, gmtime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()
driver.get("https://google.com")
sleep(5)
#navigate to another page
driver.get("https://aajtak.com")

#go back to previous page 
driver.back()
#go forward()
driver.forward()

#close the browser
#driver .quit()