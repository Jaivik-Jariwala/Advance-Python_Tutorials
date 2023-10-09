#Scrape Images and Save Them in a Folder
import requests
from bs4 import BeautifulSoup
import os

# Define the URL of the website with images
url = "https://visualstudio.microsoft.com/visual-cpp-build-tools/"

# Make an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Create a folder to save the images
if not os.path.exists("images"):
    os.makedirs("images")

# Find and download images
img_tags = soup.find_all("img")

for img_tag in img_tags:
    img_url = img_tag["src"]
    img_data = requests.get(img_url).content
    with open(os.path.join("images", img_url.split("/")[-1]), "wb") as img_file:
        img_file.write(img_data)
