#open a webpage scroll down to load dynamic contetn and captie the page source acfte the scrolling
from selenium import webdriver
from bs4 import BeautifulSoup

driver=webdriver.Firefox()
driver.get("https://github.com/Jaivik-Jariwala")

#scroll down tolad dynamic content 
driver.execute_script("window.scollTo(10, doscuments.body.scrollHeight);")

#retrerive the page source HTML of the webpage ftet the scrollign action 
page_source=driver.page_source

#parse the paf source uing beautifulsoup
soup = BeautifulSoup(page_source,'html.parser')

#print the title tag
print("title:", soup.title.text)

