from week_9.day_1.selenium_1 import webdriver
from selenium.webdriver.common.by import By

# Create a Firefox WebDriver instance
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://www.python.org/")

# Locate an element by its ID ('id-search')
element = driver.find_element(By.ID, 'id-search')

# Do something with the located element, for example, print its tag name
print("Tag Name of the Element:", element.tag_name)

# Close the browser window
driver.quit()
