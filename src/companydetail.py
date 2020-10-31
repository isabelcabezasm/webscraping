import requests 
from bs4 import BeautifulSoup 
import csv 

from datetime import date, timedelta

class DetailScraper():

    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.data = []

    def __getPrizeTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblPrecios') 
        items = table.find_all('tr')

        #get only two first rows:
        row1= items[0]
        row2 = items[1]
       
        values=[]      
        for p in row2.find_all('td'):
            values.append(p.contents[0])

        return values


    def __getHeaderPrizeTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblPrecios') 
        items = table.find_all('tr')

        #get only two first rows:
        row1= items[0]
        row2 = items[1]

        headers=[]

        for h in row1.find_all('th'):
            headers.append(h.contents[0])
       
        return headers


    def __getValuesTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblValor') 

        row = table.find('tr')        #it only has one row
        cells = row.find_all('td')

        values=[]
        values.append(cells[1].contents[0].replace("\xa0", ""))
        values.append(row.find(id='ctl00_Contenido_TickerDat').contents[0].replace("\xa0", ""))
        
        if row.find(id='ctl00_Contenido_NominalDat'):
            values.append(row.find(id='ctl00_Contenido_NominalDat').contents[0].replace("\xa0", ""))
        else: 
            values.append(0)

        values.append(row.find(id='ctl00_Contenido_MercadoDat').contents[0].replace("\xa0", ""))  

        if row.find(id='ctl00_Contenido_CapAdmDat'):
            values.append(row.find(id='ctl00_Contenido_CapAdmDat').contents[0].replace("\xa0", ""))
        else:
            values.append(0)

        return values

    def __getHeadersTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblValor') 
        row = table.find('tr')        #it only has one row
        cells = row.find_all('td')

        headers=[]

        headers.append(cells[0].contents[0].replace("\xa0", ""))
        headers.append(row.find(id='ctl00_Contenido_TickerEtq').contents[0].replace("\xa0", ""))
        headers.append(row.find(id='ctl00_Contenido_NominalEtq').contents[0].replace("\xa0", ""))
        headers.append(row.find(id='ctl00_Contenido_MercadoEtq').contents[0].replace("\xa0", ""))
        headers.append(row.find(id='ctl00_Contenido_CapAdmEtq').contents[0].replace("\xa0", ""))

        return headers


    def scapeHeaderDetails(self, url):
        page = requests.get(self.url+url) 
        soup = BeautifulSoup(page.text, 'html.parser')   

        headers= self.__getHeadersTable(soup)          
        # Últimos precios     
        headers2= self.__getHeaderPrizeTable(soup)               
        return headers + headers2

    def scrapeValueDetails(self, url):
        page = requests.get(self.url+url) 
        soup = BeautifulSoup(page.text, 'html.parser')    
        
        # Descripción empresa
        values = self.__getValuesTable(soup) 
        # Últimos precios     
        values2 = self.__getPrizeTable(soup)               

        return values+values2
        
            
