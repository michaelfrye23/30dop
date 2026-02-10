import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = "https://archive.ics.uci.edu/dataset/53/iris"

# Use requests to get the content of the webpage
response = requests.get(url)
status = response.status_code       # Check status
print(status)

# Parse content from the page using BeautifulSoup
content = response.content
soup = BeautifulSoup(content, 'html.parser')
# print(soup.title)
print(soup.title.get_text())        # Print the text of the title
# print(soup.body)                    # Print the body of the page

"""

Printing the body of the page gives us the HTML layout of the page.

We can use this to identify not only specific elements that we want to scrape
but also the structure of the page to navigate to those elements.

i.e. we can find the information we want, and use identifiers to navigate to it

"""

tables = soup.find_all('table', {"class": "table my-4 w-full"})        # Target the table with class "table my-4 w-full"
table = tables[0]
print(table)

tbody = table.find('tbody')                                            # Specify the tbody element of the table to target the body of the table
for row in tbody.find_all('tr'):
    for td in row.find_all('td'):
        print(td.get_text())                                           # Print the text of each td element in the first tr of the table

