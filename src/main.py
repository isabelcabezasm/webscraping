from stock import StockScraper

url = "https://www.bolsamadrid.es"
domain = "/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
stock = StockScraper(url, domain)
stock.scrape()