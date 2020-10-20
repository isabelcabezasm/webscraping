import requests 
from bs4 import BeautifulSoup 
import csv 

class StockScraper():

    def __internalMethod(self, attr):
        print("Just to try")
        return "nothing"
    
    
    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.subdomain = "/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
            self.data = []

    def __getHtml(self, url):
        print("getting: "+ url)
        return requests.get(url) 

    def __getStockTable(self, soup, id):
        table = soup.find(id=id) 
        items = table.find_all('tr') 
        return items

    def __getArrayFromRow(self, row):
        cells = row.find_all('td')
        array = [i.text for i in cells]        
        return array

    def scrape(self):
        print ("Stocks Web Scraping  from " + "'" + self.url + "'...")
        print ("Hello world")

        page = self.__getHtml(self.url+self.subdomain)
        soup = BeautifulSoup(page.text, 'html.parser') 

        stockTable = self.__getStockTable(soup, 'ctl00_Contenido_tblAcciones')

        for row in stockTable: 
            cells = self.__getArrayFromRow(row)

            #todo: get link to the detail page here.

            if len(cells) != 0:
                print(cells)

