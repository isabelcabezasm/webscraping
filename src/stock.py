import requests 
import csv 
import os

from bs4 import BeautifulSoup 
from companydetail import DetailScraper
from StocksStore import StoreService
from companyhistory import historicScraper

class StockScraper():
    
    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            self.data = []
            self.storeobject = StoreService(os.getcwd(), "stocks.csv")
            self.histDomain = "/esp/aspx/Empresas/InfHistorica.aspx?ISIN="
            self.storeHistoryobject = StoreService(os.getcwd(), "stocksHistory.csv")


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

    def __getIbex35Headers(self,stockTable):
        
        row = stockTable[0]
        cells = self.__getArrayFromRow(row)
        
        return cells

    def __getCompanyDetailHeaders(self, stockTable, detailsScraper):
        row = stockTable[1]
        link = self.__getLinkURL(row)
        array = detailsScraper.scapeHeaderDetails(link)     
        return array



    def scrape(self):
        print ("Stocks Web Scraping  from " + "'" + self.url + "'...")

        page = self.__getHtml(self.url+self.subdomain)
        soup = BeautifulSoup(page.text, 'html.parser') 

        stockTable = self.__getStockTable(soup, 'ctl00_Contenido_tblAcciones')
        details= DetailScraper()

        links = []
        ISINs = []
       
        headersIbex35 = self.__getIbex35Headers(stockTable)        
        headersDetail = self.__getCompanyDetailHeaders(stockTable,details)
        headers = headersIbex35 + headersDetail

        self.storeobject.open_file()
        self.storeobject.write_row(headers)
    
        for row in stockTable: 
            cells = self.__getArrayFromRow(row)            
            if len(cells) != 0:
                link = self.__getLinkURL(row)
                if link is not None:
                    links.append(link)
                    values = details.scrapeValueDetails(link)
                    ISINs.append(values[0])
                    self.storeobject.write_row(cells+values)   
    
        self.storeobject.close_file()
        
        self.storeHistoryobject.open_file()
        scraper = historicScraper(self.url,self.histDomain)
        headers = scraper.getCompanyHistoricHeaders(ISINs[0])
        self.storeHistoryobject.write_row(headers)
        for isin in ISINs:
            companyData= scraper.scrapeCompanyHistoric(isin)
            for row in companyData:
                self.storeHistoryobject.write_row(row)
        self.storeHistoryobject.close_file()
       
       