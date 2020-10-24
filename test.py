import requests
from bs4 import BeautifulSoup

str = "https://www.bolsamadrid.es/esp/aspx/Empresas/InfHistorica.aspx?ISIN=ES0125220311&ClvEmis=25220"



headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = "__VIEWSTATE=aWd24Hetn%2F7hc9v9QS8JxB3IcDJn6pm%2BVwo47jOyUwBUcPHwkSXuymigdhDR0RfPfmKWgaSJdm%2F%2BzEwiT5IVtDXuA87XhmdqznKmDfAA6F3mn8rekZN5Hcc5VlIldXaRfuGYkySTZv7q8Q6SUKN11KDockijh1k2q8TykbNOecUxcZkayp72VjM0Dv7%2FpveT5G%2BWWu8q2ED6%2B4etSNiyWyZm2FlX0Dv%2FYhUSIM03%2FH6Y4C%2F4dByVTlJxd%2Bk8I%2Bqs5q%2FEUHzY1%2FgT41s4twb5z5BFpEqrwNUi4sQPzrMXXcbYIPepUG93UI48%2BB7YhaU66fgcObbF7Hy4%2FT4%2FwjeCD7VrkHjcj%2FbErEfw1siroiDk486XNPHuO3T6zcU0H%2FtSpOldT6f8cy2r8M18Y5qGYlpvRW4CD2W7RFy%2FrUO8S5B%2BVQ7PdFYx19aRkwaMaSYafhZecVU6jxFLWJygcmqvmqFP%2BNzx7xwIs2S9jLEyJ%2Fb3i3DTRVhrN02h404SYiqI1G14D%2BCw2SQtPhOoMQoCU3q2KOtRFszTxG3Dmrn7dUNWudnUs9s%2FtnRgjiT8JMHQK38dFWJP2S2rqRyvUJOmjOwrbSpahqIHkIaYc0babbscxWMo0nTKz2ry6Ua4nI2HjWnAAyf7HwWfqIT3ik1ZNF1mPuw%3D&__VIEWSTATEGENERATOR=1538A4A5&__EVENTVALIDATION=W7RUMYmlXBDtr1L5xNo9RgnVFrUtNEINt8xgp7YqieDuDunRdF3qvo6sE6jjWkasyRNDVVKWrE%2BnVbl58GOXxd0pS%2FyTgD6vkkkcHHyWcJRkVXcjcDKcTsdjeyBDAWxAFHQXBV2Y8ZwoGRtUlGWfesdLL%2F5d%2B0PEiq5ffXKSOMczDj8UzeOBQylkonRTXO1RDUEz1%2BLH4ovnKylc0gvS1fX3mYc6DUR%2BRMXrkqqH9Nk7o%2BNgbou2GjFQwmsIesHIyPYLOsPaxO1oFsRCFT4WrRXcBsM%3D&ctl00%24Contenido%24Desde%24Dia=24&ctl00%24Contenido%24Desde%24Mes=09&ctl00%24Contenido%24Desde%24A%C3%B1o=2019&ctl00%24Contenido%24Hasta%24Dia=23&ctl00%24Contenido%24Hasta%24Mes=10&ctl00%24Contenido%24Hasta%24A%C3%B1o=2019&ctl00%24Contenido%24Buscar=+Buscar+"


page = requests.post(str, data=data, headers = headers)
bs = BeautifulSoup(page.content, 'html.parser')

print(bs)







