from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver .implicitly_wait(1)

driver.get("hhtps://google.com")

# driver .maximize weindows()

Element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"APjFqb"))
)

#wait for a maximun of 10 sec 
Timeout = driver.find_element(By.ID, "APjFqb")
Element.send_keys("jaivik_jariwala")
Element.submit()