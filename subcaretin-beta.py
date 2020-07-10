import requests
import magic
import os
import sys
from bs4 import BeautifulSoup as bso
from unrar import rarfile
from zipfile import ZipFile

if len(sys.argv) == 2:
    movie_name = sys.argv
    movie_name1 = os.path.splitext(movie_name[1])
else:
    print('\nUso: python3 subcaretin.py VIDEO.mkv\n')
    sys.exit()

name = input("\nIntroduce el nombre de la película y su año:\n- ")

print('\nBuscando subtítulos para %s...\n' % (name))

subdivx = 'http://www.subdivx.com/index.php?q=%s&accion=5&masdesc=&subtitulos=1&realiza_b=1' % (name)
page = requests.get(subdivx)
soup = bso(page.content, 'html.parser')

titulos = []
links = []
descripciones = []

for titulo in soup.find_all(id='menu_titulo_buscador'):
    titulos.append(titulo.text)

for descripcion in soup.find_all(id='buscador_detalle_sub'):
    descripciones.append(descripcion.text)

for a in soup.find_all('a', class_='titulo_menu_izq'):
    links.append(a.get('href'))

limite = len(titulos)

for number in range(limite):
    print('%s: %s - %s' % (number, titulos[number], descripciones[number]))

eleccion = int(input("\nElige el número a descargar: \n- "))
elegido = requests.get(links[eleccion])
sopa = bso(elegido.content, 'html.parser')
descargar = sopa.find('a', class_='link1')['href']

r = requests.get(descargar, allow_redirects=True)
open('subs', 'wb').write(r.content)

tipo = magic.from_file('subs')

def archivos():
    limite1 = len(nombre)
    for d in range(limite1):
        print('%s: %s' % (d,nombre))

print('\nArchivos a extraer:')

if 'Zip' in tipo:
    zip1 = ZipFile('subs')
    nombre = zip1.namelist()
    archivos()
    eleccion1 = int(input("\nElige el número del archivo a extraer:\n- "))
    source = '/tmp/%s' % (nombre[eleccion1])
    dest = '%s.es.srt' % (movie_name1[0])
    zip1.extract(nombre[eleccion1],r'/tmp/')
    os.rename(source, dest)
else:
    rar = rarfile.RarFile('subs')
    nombre = rar.namelist()
    archivos()
    eleccion1 = int(input("\nElige el número del archivo a extraer:\n- "))
    source = '/tmp/%s' % (nombre[eleccion1])
    dest = '%s.es.srt' % (movie_name1[0])
    rar.extract(nombre[eleccion1],r'/tmp/')
    os.rename(source, dest)

if os.path.isfile(dest) is True:
    print('Listo')
else:
    print('Hubo un error. Intenta de nuevo')
