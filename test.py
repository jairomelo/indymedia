import waybackpy
from waybackpy import Cdx
from waybackpy.exceptions import WaybackError
from bs4 import BeautifulSoup
import os
import time


def get_info_page(url, user_agent):
    '''
    use the waybackpy library to retrieve the content from a specific page
    '''
    if url.startswith('https://web.archive.org'):
        archive = waybackpy.Url(url, user_agent)
    else:
        wb = waybackpy.Url(url, user_agent)
        archive = wb.oldest()
        archive.archive_url
    return archive.get()


def get_texto(url, user_agent):
    '''
    get the text from a specific page
    '''
    try:
        texto = get_info_page(url, user_agent)
        sopa = BeautifulSoup(texto, 'html.parser')
        return sopa.get_text()
    except WaybackError as e:
        urls_rezagadas = open('urls_rezagadas.txt', 'a')
        urls_rezagadas.write(url + '\n')
        urls_rezagadas.close()
        return None


url = "http://colombia.indymedia.org"
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'

if not os.path.exists('capturas_listado.txt'):
    cdx = Cdx(url=url, user_agent=user_agent, start_timestamp=2000,
              end_timestamp=2011, filters=["statuscode:200"], collapses=["digest"])
    # filters: solamente páginas completas, collapses: elimina duplicados en capturas inmediatas
    capturas = cdx.snapshots()

    capturas_listado = open('capturas_listado.txt', 'w')

    for c in capturas:
        capturas_listado.write(c.archive_url + '\n')
    capturas_listado.close()

urls_capturas = open('capturas_listado.txt', 'r')
lista_capturas = urls_capturas.readlines()

try:
    os.makedirs('textos', exist_ok=True)
except OSError as e:
    raise

for lc in lista_capturas:
    filename = 'textos/' + lc.split('/')[4].strip()[:8] + '.txt'
    if not os.path.exists(filename):
        texto = get_texto(lc, user_agent)
        time.sleep(2)
        if texto:
            archivo = open(filename, 'w', encoding='utf-8')
            archivo.write(texto)
            print(f"guardado el archivo {filename}")
            archivo.close()
        else:
            print('No se pudo obtener el texto de la página: ' + lc)
    else:
        print(f"El archivo {filename} ya existe")
