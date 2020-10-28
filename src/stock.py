import requests 
import csv 
import os

from bs4 import BeautifulSoup 
from companydetail import DetailScraper
from StocksStore import StoreService

class StockScraper():
    
    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            self.data = []
            self.storeobject = StoreService(os.getcwd(), "stocks.csv")
            # self.storeHistoryobject = StoreService(os.getcwd(), "stocksHistory.csv")


    def __getHtml(self, url):
        print("getting: "+ url)
        return requests.get(url) 

    def __getStockTable(self, soup, id):
        table = soup.find(id=id) 
        items = table.find_all('tr') 
        return items

    def __getArrayFromRow(self, row):
        cells = row.find_all('td')
        if len(cells)==0 :
            cells = row.find_all('th')

        array = [i.text for i in cells]        
        return array

    def __getLinkURL(self, row):
        link = row.find('a')
        if link is not None: 
            return link.get('href')
        else:
            return None

    def scrape(self):
        print ("Stocks Web Scraping  from " + "'" + self.url + "'...")

        page = self.__getHtml(self.url+self.subdomain)
        soup = BeautifulSoup(page.text, 'html.parser') 

        stockTable = self.__getStockTable(soup, 'ctl00_Contenido_tblAcciones')
        details= DetailScraper()

        links = []
        stockInfo = []
        headers = []
       
        for row in stockTable: 
            cells = self.__getArrayFromRow(row)            
            if len(cells) != 0:
                link = self.__getLinkURL(row)
                if link is not None:
                    links.append(link)
                    print(link)
                    values = details.scrapeValueDetails(link)
                    stockInfo.append(cells+values)
                else:
                    headers=cells
        
        headers = headers+details.scapeHeaderDetails(links[0])           

        self.storeobject.open_file()        
        self.storeobject.write_row(headers)
        for stock in stockInfo:
            self.storeobject.write_row(stock)      
        self.storeobject.close_file()