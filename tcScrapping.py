import requests
from bs4 import BeautifulSoup

url="https://www.sbs.gob.pe/app/pp/SISTIP_PORTAL/Paginas/Publicacion/TipoCambioPromedio.aspx"

peticionUrl = requests.get(url)

def tcScrapping(monedas):
  if(peticionUrl.status_code == 200):
    html = BeautifulSoup(peticionUrl.text, 'html.parser')
    tabla = html.find_all('table',{'id':'ctl00_cphContent_rgTipoCambio_ctl00'})
    tabla = BeautifulSoup(str(tabla), 'html.parser')
    filasMonedas = tabla.find_all('td')
    for fila in range(0, len(filasMonedas), 3):
      dicMoneda = {
        'currency':filasMonedas[fila].get_text(),
        'buy':filasMonedas[fila + 1].get_text(),
        'sell':filasMonedas[fila + 2].get_text(),
      }
      monedas.append(dicMoneda)
  else:
    print("error" + str(peticionUrl.status_code))
  return monedas