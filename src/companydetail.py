import requests 
from bs4 import BeautifulSoup 
import csv 


class DetailScraper():

    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.data = []

    def __getPrizeTable(self, soup, id):
        table = soup.find(id=id) 
        items = table.find_all('tr') 
        return items

    def scrapeDetails(self, url):
        page = requests.get(self.url+url) 
        soup = BeautifulSoup(page.text, 'html.parser')    
        
        # Últimos precios     
        prizeTable = self.__getPrizeTable(soup, 'ctl00_Contenido_tblPrecios')
        print (prizeTable)
