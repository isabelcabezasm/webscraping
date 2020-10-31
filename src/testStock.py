import unittest
import os
from bs4 import BeautifulSoup
from stock import StockScraper
from companydetail import DetailScraper
from testfixtures import TempDirectory, compare

class TestStocks(unittest.TestCase):

    def setUp(self):
        self.url = "https://www.bolsamadrid.es"
        self.domain = "/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000"
        
        pass

    def tearDown(self):
        
        pass


    def test_get_headers_ibex35(self):
        expected = ['Nombre', 'Últ.', '% Dif.', 'Máx.', 'Mín.', 'Volumen', 'Efectivo (miles €)', 'Fecha', 'Hora']

        html = """<table class="TblPort" cellspacing="0" cellpadding="3" id="ctl00_Contenido_tblAcciones" style="width:100%;border-collapse:collapse;">
		<tbody><tr align="center">
			<th scope="col">Nombre</th><th scope="col">Últ.</th><th scope="col">% Dif.</th><th scope="col">Máx.</th><th scope="col">Mín.</th><th scope="col">Volumen</th><th scope="col">Efectivo (miles €)</th><th scope="col">Fecha</th><th class="Ult" scope="col">Hora</th>
		</tr><tr align="right">
			<td class="DifFlBj" align="left"><a href="/esp/aspx/Empresas/FichaValor.aspx?ISIN=ES0125220311">ACCIONA</a></td><td>86,9000</td><td class="DifClBj">-3,34</td><td>91,1000</td><td>86,7000</td><td>139.018</td><td>12.227,00</td><td align="center">29/10/2020</td><td class="Ult" align="center">Cierre</td>
		</tr><tr align="right">
			<td class="DifFlBj" align="left"><a href="/esp/aspx/Empresas/FichaValor.aspx?ISIN=ES0132105018">ACERINOX</a></td><td>6,7500</td><td class="DifClBj">-2,09</td><td>6,9560</td><td>6,6880</td><td>1.253.406</td><td>8.483,15</td><td align="center">29/10/2020</td><td class="Ult" align="center">Cierre</td>
		</tr>
	</tbody></table>"""
        soup =  BeautifulSoup(html, 'html.parser') 
        stocks = StockScraper(self.url, self.domain)
        stockTable = stocks._StockScraper__getStockTable(soup, 'ctl00_Contenido_tblAcciones')
        actual = stocks._StockScraper__getIbex35Headers(stockTable)
        
        self.assertEqual(expected, actual)



    def test_get_headers_company_details(self):
        expected = ['ISIN', 'Ticker', 'Nominal', 'Mercado', 'Capital Admitido', 'Fecha', 'Hora', 'Cierre', 'Ref.', '% Dif.', 'Últ.', 'Máx.', 'Mín.', 'Medio', 'Volumen', 'Efectivo']

        details= DetailScraper()

        html = """<table class="TblPort" cellspacing="0" cellpadding="3" id="ctl00_Contenido_tblAcciones" style="width:100%;border-collapse:collapse;">
		<tbody><tr align="center">
			<th scope="col">Nombre</th><th scope="col">Últ.</th><th scope="col">% Dif.</th><th scope="col">Máx.</th><th scope="col">Mín.</th><th scope="col">Volumen</th><th scope="col">Efectivo (miles €)</th><th scope="col">Fecha</th><th class="Ult" scope="col">Hora</th>
		</tr><tr align="right">
			<td class="DifFlBj" align="left"><a href="/esp/aspx/Empresas/FichaValor.aspx?ISIN=ES0125220311">ACCIONA</a></td><td>86,9000</td><td class="DifClBj">-3,34</td><td>91,1000</td><td>86,7000</td><td>139.018</td><td>12.227,00</td><td align="center">29/10/2020</td><td class="Ult" align="center">Cierre</td>
		</tr><tr align="right">
			<td class="DifFlBj" align="left"><a href="/esp/aspx/Empresas/FichaValor.aspx?ISIN=ES0132105018">ACERINOX</a></td><td>6,7500</td><td class="DifClBj">-2,09</td><td>6,9560</td><td>6,6880</td><td>1.253.406</td><td>8.483,15</td><td align="center">29/10/2020</td><td class="Ult" align="center">Cierre</td>
		</tr>
	    </tbody></table>"""

        soup =  BeautifulSoup(html, 'html.parser') 

        stocks = StockScraper(self.url, self.domain)

        stockTable = stocks._StockScraper__getStockTable(soup, 'ctl00_Contenido_tblAcciones')
        actual = stocks._StockScraper__getCompanyDetailHeaders(stockTable,details)
        
        self.assertEqual(expected, actual)

  

 
if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStocks)
    unittest.TextTestRunner(verbosity=2).run(suite) 