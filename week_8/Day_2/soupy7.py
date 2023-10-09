import requests
from bs4 import BeautifulSoup

# Initialize a list to store data from multiple pages
all_data = []

# Define the base URL and page number
base_url = "https://visualstudio.microsoft.com/visual-cpp-build-tools/"
page_number = 1

while True:
    # Construct the URL for the current page
    url = f"{base_url}/{page_number}"
    
    # Make an HTTP GET request to the page
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract data from the current page
    items = soup.find_all("div", class_="item")  # Adjust the selector according to the actual HTML structure
    
    for item in items:
        title = item.find("h2").text.strip()
        description = item.find("p").text.strip()
        all_data.append({"Title": title, "Description": description})
    
    # Check for pagination end conditions (e.g., reaching the last page)
    if some_condition:  # Define your pagination end condition here
        break
    
    # Increment the page number for the next iteration
    page_number += 1

# Now, 'all_data' contains data from all pages
for data in all_data:
    print(data)
