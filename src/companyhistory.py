import requests 
from bs4 import BeautifulSoup 

from datetime import date, timedelta
# from calendar import monthrange
import calendar

class historicScraper():

    def __init__(self, url,subdomain):
            self.url = url 
            self.subdomain = subdomain 
            # self.data = []
            # self.storeobject = StoreService(os.getcwd(), "stocks.csv")

    def __getPageHistoric(self,isin):
        url = self.url + self.subdomain + isin
        # print("getting Historic data: "+ url)
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

    def __getPageHistoric_Filtered(self, response, initialDate, endDate):
        url = response.url
        soup = BeautifulSoup(response.text, 'html.parser')
        
        formData = self.__getFormData(soup,initialDate.day,initialDate.month,initialDate.year,endDate.day,endDate.month,endDate.year)        
        filteredpage = requests.post(url,data = formData) 
        soup = BeautifulSoup(filteredpage.text , 'html.parser')
        return soup

    def __getDataTable(self, soup, id):
        table = soup.find(id=id) 
        if table: 
            items = table.find_all('tr') 
            return items
    
    def __getCompanyDataInfo(self, soup, classid):
        table = soup.find(class_=classid)
        if table: 
            items = table.find_all('tr') 
            cells = items[1].find_all('td')
            info = [self.__cleanText(cells[2].text), self.__cleanText(cells[4].text), self.__cleanText(cells[5].text)]
            return info
    
    def __getHistoricDataFromTable(self, table, addedCompanyInfo):
        data = []
        for row in table:
            if row.find('td'): #is value row                
                cells = row.find_all('td')
                values = [i.text for i in cells] 
                values = addedCompanyInfo+values
                data.append(values)

        return data

    def __cleanText(self, text):
        return text.replace("\n", "").replace("\r", "").replace(" ", "")

    def __getHistoricHeadersFromTable(self, table):           
        fixheaders=["Nombre", "Ticker", "ISIN"]
        if(len(table)>0):     
            cells = table[0].find_all('th')
            headers = [i.text for i in cells]  
        fixheaders = fixheaders + headers                   
        return fixheaders

    def __getDateRanges(self):
        dateList = []

        endDate = date.today()
        initialDate = endDate - timedelta(days=+365)

        firstRangeIni = initialDate
        firstRangeFin = date(year=initialDate.year, month=initialDate.month, day=self.__lastDayOfMonth(initialDate.year, initialDate.month))   #último dia de este mes
        dateList.append([firstRangeIni,firstRangeFin ])

        while(firstRangeFin < date.today()):
            initialDate = initialDate + timedelta(days=+30)
            firstRangeIni = date(year=initialDate.year, month= initialDate.month, day=1) #first day of the month
            firstRangeFin = date(year=initialDate.year, month=initialDate.month, day=self.__lastDayOfMonth(initialDate.year, initialDate.month))   #last day of the month
            dateList.append([firstRangeIni,firstRangeFin ])

        return dateList


    def __lastDayOfMonth(self, year, month):
        return calendar.monthrange(year,month)[1]

    def getCompanyHistoricHeaders (self, isin):
         # get page historic
        pageHistoric = self.__getPageHistoric(isin)

        # get headers
        pageHistoricFiltered = self.__getPageHistoric_Filtered(pageHistoric, date.today()- timedelta(days=+5), date.today())
        dataTable = self.__getDataTable(pageHistoricFiltered, "ctl00_Contenido_tblDatos")
        headers = self.__getHistoricHeadersFromTable(dataTable) #getOnlyHeaders 

        return headers
    
    def scrapeCompanyHistoric(self, isin):

        # get page historic
        pageHistoric = self.__getPageHistoric(isin)

        # get range of dates for 1 year
        dateRanges = self.__getDateRanges()
        
        data = []

        for dateR in dateRanges:

            initialDate = dateR[0]
            finishDate  = dateR[1]

            # get data
            pageHistoricFiltered = self.__getPageHistoric_Filtered(pageHistoric, initialDate, finishDate)
            companyDataInfo = self.__getCompanyDataInfo(pageHistoricFiltered, "FrmBusq")            
            dataTable = self.__getDataTable(pageHistoricFiltered, "ctl00_Contenido_tblDatos")
            if dataTable: 
                values = self.__getHistoricDataFromTable(dataTable, companyDataInfo)
                data = data + values
       
        return data