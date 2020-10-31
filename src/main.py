from stock import StockScraper

output_file = "dataset.csv"

url = "https://www.bolsamadrid.es"
domain = "/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
stock = StockScraper(url, domain)
stock.scrape()
# stock.data2csv(output_file);cls
