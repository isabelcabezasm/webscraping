import requests
from bs4 import BeautifulSoup

str = "https://www.bolsamadrid.es/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0125220311&ClvEmis=25220"


query= "ctl00$Contenido$Desde$Dia=20&ctl00$Contenido$Desde$Mes=09&ctl00$Contenido$Desde$Año=2019&ctl00$Contenido$Hasta$Dia=19&ctl00$Contenido$Hasta$Mes=10&ctl00$Contenido$Hasta$Año=2019&ctl00$Contenido$Buscar=+Buscar+"

# query2 = "ctl00%24Contenido%24Desde%24Dia=20& \
# ctl00%24Contenido%24Desde%24Mes=09& \ 
# ctl00%24Contenido%24Desde%24A%C3%B1o=2019&

# ctl00%24Contenido%24Hasta%24Dia=19&
# ctl00%24Contenido%24Hasta%24Mes=10&
# ctl00%24Contenido%24Hasta%24A%C3%B1o=2019&

# ctl00%24Contenido%24Buscar=+Buscar+"

data ={'ctl00%24Contenido%24Desde%24Dia' : '20',
'ctl00%24Contenido%24Desde%24Mes': '09', 
'ctl00%24Contenido%24Desde%24A%C3%B1o':'2019',
'ctl00%24Contenido%24Hasta%24Dia':'19',
'ctl00%24Contenido%24Hasta%24Mes':'10',
'ctl00%24Contenido%24Hasta%24A%C3%B1o':'2019'        
}

data ={'ctl00$Contenido$Desde$Dia' : '20',
'ctl00$Contenido$Desde$Mes': '09', 
'ctl00$Contenido$Desde$Año':'2019',
'ctl00$Contenido$Hasta$Dia':'19',
'ctl00$Contenido$Hasta$Mes':'10',
'ctl00$Contenido$Hasta$Año':'2019'        
}



page = requests.post(str, data=data) 
bs = BeautifulSoup(page.content, 'html.parser')

print(bs)







