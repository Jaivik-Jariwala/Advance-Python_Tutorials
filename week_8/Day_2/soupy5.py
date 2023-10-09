#Scrape Titles and Links of Articles and Save to a CSV File
import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the news website
url = "https://visualstudio.microsoft.com/visual-cpp-build-tools/"

# Make an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Initialize a list to store article data
article_data = []

# Find and extract article titles and links
articles = soup.find_all("article")

for article in articles:
    title = article.find("h2").text.strip()
    link = article.find("a")["href"]
    article_data.append({"Title": title, "Link": link})

# Save the data to a CSV file
with open("news_articles.csv", "w", newline="") as csv_file:
    fieldnames = ["Title", "Link"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in article_data:
        writer.writerow(data)
