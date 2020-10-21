import requests 
from bs4 import BeautifulSoup 
import csv 


class DetailScraper():

    def __init__(self):
            self.url = "https://www.bolsamadrid.es"
            self.subdomain = "/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
            self.data = []

    def scrapeDetails(self, url):
        print("this is the page with the details: ")
        print (self.url+url)

        #todo: request and parse
