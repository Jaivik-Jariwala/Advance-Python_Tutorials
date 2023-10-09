import requests
from bs4 import BeautifulSoup

# Make an HTTP GET request
url = "https://www.example.com"  # Replace with the URL of the website you want to scrape
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract and print the page title
    print("Page title:", soup.title.text)
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
