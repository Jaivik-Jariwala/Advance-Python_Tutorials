#switching to an iframe and then switching back to main content 
from selenium import webdriver 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep, strftime, gmtime
driver = webdriver.Firefox()
#driver.get()
driver.get("https://www.hyrtutorials.com/frames-practice.html")
# find the iframe using its Xpath 
iframe = driver.find_element(By.XPATH,"//iframe[@id='fml]")
#replace frame_id witht he actual iframe id or other locator 
print(iframe.id)
#switch to the iframe 
driver.switch_to.frame(iframe)
dropdown=
Select(driver.find_element(By.CSS_SELECTOR,"select#selectnav2.selectnav"))
dropdown.select_by_value("")
#for selecting "contact" from dropdown
sleep(5)
#switch back to main content 
driver.switch_to.default_content()