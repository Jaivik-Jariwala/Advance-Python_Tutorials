from bs4 import BeautifulSoup

# Sample HTML content
html_content = "<a href='https://www.redbus.in/railways/search?src=BRC&dst=ST&doj=20230927&srcName=Vadodara&dstName=Surat%20-%20All%20Stations'>visit example</a>"

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract attributes from the anchor element
link = soup.a

# Extract and print the text within the anchor tag
print("Link text:", link.text)

# Extract and print the value of the 'href' attribute
print("Linked URL:", link.get('href'))
