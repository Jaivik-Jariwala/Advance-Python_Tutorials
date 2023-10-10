import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Set up Selenium WebDriver (replace with the path to your WebDriver executable)
driver_path = "/path/to/chromedriver"
service = Service(driver_path)
driver: WebDriver = webdriver.Chrome(service=service)

# Replace with the URL of the news website you want to scrape
url = "https://github.com/Jaivik-Jariwala"

# Open the website
driver.get(url)

# Scroll down the page to load more articles (modify as needed)
for _ in range(3):  # Adjust the number of times to scroll
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(2)  # Adjust the wait time as needed

# Get the page source after loading articles
page_source = driver.page_source

# Close the browser
driver.quit()

# Parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

# Find and extract the news articles (modify the selectors accordingly)
article_elements = soup.find_all('div', class_='article')

# Iterate through the articles and extract data
for article in article_elements:
    # Extract the article title
    title = article.find('h2').text.strip()

    # Extract the article content
    content = article.find('p').text.strip()

    # Print the title and content
    print("Title:", title)
    print("Content:", content)
    print("=" * 50)
