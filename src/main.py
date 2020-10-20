from stock import StockScraper

output_file = "dataset.csv"

stock = StockScraper()
stock.scrape()
# stock.data2csv(output_file);