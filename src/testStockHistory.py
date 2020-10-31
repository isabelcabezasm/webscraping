import unittest
import os
from bs4 import BeautifulSoup
from stock import StockScraper
from companyhistory import historicScraper
from testfixtures import TempDirectory, compare

from datetime import date, timedelta

class TestHistoricStocks(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.bolsamadrid.es"
        self.domain = "/esp/aspx/Empresas/InfHistorica.aspx?ISIN=" #ES0125220311&ClvEmis=25220"
        
        pass

    def tearDown(self):
        
        pass


    def test_get_getHTML(self):
        
        scraper = historicScraper(self.url,self.domain)
        isin = 'ES0125220311'
        response = scraper._historicScraper__getPageHistoric(isin)

        self.assertTrue(response.ok)
        
    def test_get_getHTML_filtered(self):
            
        scraper = historicScraper(self.url,self.domain)
        isin = 'ES0125220311'
        response = scraper._historicScraper__getPageHistoric(isin)
        historicFiltered = scraper._historicScraper__getPageHistoric_Filtered(response)

        self.assertTrue(historicFiltered.ok)

    # def test_get_getHTML_filtered(self):
    #     today = date.today()
    #     initialDate = today - timedelta(days=+730)
    #     print("Hoy")
    #     print(initialDate.year)
 
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHistoricStocks)
    unittest.TextTestRunner(verbosity=2).run(suite) 