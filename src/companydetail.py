import requests 
from bs4 import BeautifulSoup 
import csv 
from decimal import Decimal 
from datetime import date, timedelta

class DetailScraper():

    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.data = []

    def __typefyArray(self, array):
        array2 = []
        for a in array:
            if type(a) == int:
                array2.append(a)
            else:
                item = self.__typefy(a)
                if item:
                    array2.append(item)
                else:
                    array2.append(a)
        return array2

    def __typefy(self, text):
        # si el número tiene comas las quitamos
        try:
            return float(text.replace(".","").replace(",","."))
        except ValueError:
            return None

    def __getPrizeTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblPrecios') 
        items = table.find_all('tr')

        #get only the second rows:
        row2 = items[1]
       
        values=[]      
        for p in row2.find_all('td'):
            values.append(p.contents[0])

        return self.__typefyArray(values)

    def __getHeaderPrizeTable(self, soup):
        table = soup.find(id='ctl00_Contenido_tblPrecios') 
        items = table.find_all('tr')

        #get only the first row:
        row1= items[0]
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

        return self.__typefyArray(values)

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
        # headers2= self.__getHeaderPrizeTable(soup)     
        return headers

    def scrapeValueDetails(self, url):
        page = requests.get(self.url+url) 
        soup = BeautifulSoup(page.text, 'html.parser')    
        
        # Descripción empresa
        values = self.__getValuesTable(soup) 
        # Últimos precios     
        # values2 = self.__getPrizeTable(soup)               

        return values
