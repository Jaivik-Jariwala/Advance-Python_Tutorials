from bs4 import BeautifulSoup

# Sample HTML content (corrected)
html_content = "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Navigate the HTML tree
div_element = soup.div  # Get the <div> element

# Find all <p> elements within the <div> and print their text
for p in div_element.find_all("p"):
    print(p.text)
