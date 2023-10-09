import time
from week_9.day_1.selenium_1 import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# Create a Firefox WebDriver instance
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://bstackdemo.com/")

# Find the dropdown element by CSS selector
dropdown = Select(driver.find_element(By.CSS_SELECTOR, "select"))

# Select an option by its value (assuming the option values are 'lowestprice')
dropdown.select_by_value("lowestprice")

# Wait for 5 seconds (note the correct spelling of 'time' here)
time.sleep(5)

# Close the browser window
driver.quit()
