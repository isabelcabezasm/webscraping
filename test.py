import requests
from bs4 import BeautifulSoup

str = "https://www.bolsamadrid.es"
page = requests.get(str)
#soup = BeautifulSoup(page.content)
bs = BeautifulSoup(page.content, 'html.parser')

print(bs)

