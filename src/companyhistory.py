import requests 
from bs4 import BeautifulSoup 

from datetime import date, timedelta

class historicScraper():

    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            # self.data = []
            # self.storeobject = StoreService(os.getcwd(), "stocks.csv")

    def __getPageHistoric(self,isin):
        url = self.url + self.subdomain + isin
        print("getting Historic data: "+ url)
        return requests.get(url) 


    def __getFormData(self, soup, initialDay, initialMonth, initialYear, finalDay, finalMonth, finalYear):
        return {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': soup.find(id='__VIEWSTATE')['value'],
        '__VIEWSTATEGENERATOR': soup.find(id='__VIEWSTATEGENERATOR')['value'],
        '__EVENTVALIDATION': soup.find(id='__EVENTVALIDATION')['value'],
        'ctl00$Contenido$Desde$Dia': initialDay,
        'ctl00$Contenido$Desde$Mes': initialMonth,
        'ctl00$Contenido$Desde$Año': initialYear,
        'ctl00$Contenido$Hasta$Dia': finalDay,
        'ctl00$Contenido$Hasta$Mes': finalMonth,
        'ctl00$Contenido$Hasta$Año': finalYear,
        'ctl00$Contenido$Buscar': 'Buscar'

    }    

    def __getPageHistoric_Filtered(self, response):
        url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')

        endDate = date.today()
        initialDate = endDate - timedelta(days=+730)
        formData = self.__getFormData(soup,initialDate.day,initialDate.month,initialDate.year,endDate.day,endDate.month,endDate.year)
        
        return requests.post(url,data = formData) 

    
    def scrapeCompanyHistori(self, isin):

        # get page historic
        pageHistoric = self.__getPageHistoric(isin)

        # filter dates --> 1 year
        # get data
        pageHistoricFiltered = self.__getPageHistoric_Filtered(pageHistoric)

        # navigate  all next pages
        # get data
        # return data
        pass 
