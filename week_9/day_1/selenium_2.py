from week_9.day_1.selenium_1 import webdriver
from selenium.webdriver.common.by import By

# Create a Firefox WebDriver instance
driver = webdriver.Firefox()

# Open a website
driver.get("https://www.python.org/")

try:
    # Locate the search input field by name attribute
    search_field = driver.find_element(By.NAME, 'q')

    # Click the search input field to activate it
    search_field.click()

    # Enter the search query
    search_field.send_keys("for loop")

    # Optionally, locate and click the search button
    search_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  # Adjust the XPath selector as needed
    search_button.click()

except Exception as e:
    # Handle exceptions, e.g., if the elements are not found or other issues occur
    print("An error occurred:", e)

finally:
    # Close the browser window
    driver.quit()
