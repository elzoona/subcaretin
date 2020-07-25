import requests, magic, os, sys, shutil, json
from pathlib import Path
from bs4 import BeautifulSoup as bso
from unrar import rarfile
from zipfile import ZipFile

if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('\nUso: python3 subcaretin.py VIDEO.mkv\n')
        sys.exit()

api_search = "http://argenteam.net/api/v1/search"
api_episode = "http://argenteam.net/api/v1/episode"
api_movie = "http://argenteam.net/api/v1/movie"

movie_name = sys.argv[1]
wo_ext = Path(movie_name).with_suffix('')

titulos = []
links = []
descripciones = []
total = []

def entrada():
    name = input("\nIntroduce el nombre de la película y su año:\n- ")
    name = name.replace(" ", "+")
    
    if not name:
        print('Inválido')
        sys.exit()
    else:
        print('\nBuscando subtítulos...')
        return name
    
def subdivx(movie):
    core = 'http://www.subdivx.com/index.php?q='
    subdivx = '%s%s&accion=5&masdesc=&subtitulos=1&realiza_b=1' % (core, movie)
    page = requests.get(subdivx)
    soup = bso(page.content, 'html.parser')
    
    for titulo in soup.find_all(id='menu_titulo_buscador'):
        titulos.append(titulo.text)

    for descripcion in soup.find_all(id='buscador_detalle_sub'):
        descripciones.append(descripcion.text)

    for a in soup.find_all('a', class_='titulo_menu_izq'):
        links.append(a.get('href'))

def argenteam(movie):
    argenteam_search = '%s?q=%s' % (api_search, movie)
    page = requests.get(argenteam_search)
    soup = bso(page.content, 'html.parser')
    arg_json = json.loads(soup.text)

    def get_arg_links(moviePag):
        moviePag = requests.get('%s?id=%s' % (api_movie, arg_id))
        movieSop = bso(moviePag.content, 'html.parser')
        movieJson = json.loads(movieSop.text)
        movieTitle = movieJson['title']
        for rele in movieJson['releases']:
            if rele['subtitles']:
                for uri in rele['subtitles']:
                    titulos.append('[Argenteam] %s' % (movieTitle))
                    links.append(uri['uri'])
                    descripciones.append(uri['uri'].rsplit('/', 1)[-1])
    
    for tipo in arg_json['results']:
        mov_o_tv = tipo['type']
        arg_id = tipo['id']
        if mov_o_tv == 'movie':
            moviePag = requests.get('%s?id=%s' % (api_movie, arg_id))
            get_arg_links(moviePag)              
        else:
            moviePag = requests.get('%s?id=%s' % (api_episode, arg_id))
            get_arg_links(moviePag)
 
def arg_subd():
    limite = len(titulos)
    for number in range(limite):
        total.append('%s: %s - %s' % (number, titulos[number], descripciones[number]))
    if not total:
        print('Sin resultados\n')
        sys.exit()
    else:
        return total

def elegir(res_array):
    for each in res_array:
        print(each)

    eleccion = int(input("\nElige el número a descargar: \n- "))

    if "argenteam.net" in links[eleccion]:
        print('\nBajando: %s %s\n' % (titulos[eleccion], descripciones[eleccion]))
        comprimido = requests.get(links[eleccion], allow_redirects=True)
        open(r'/tmp/subs', 'wb').write(comprimido.content)
    else:
        print('\nBajando: %s %s\n' % (titulos[eleccion], descripciones[eleccion]))
        elegido = requests.get(links[eleccion])    
        sopa = bso(elegido.content, 'html.parser')
        descargar = sopa.find('a', class_='link1')['href']
        comprimido = requests.get(descargar, allow_redirects=True)
        open(r'/tmp/subs', 'wb').write(comprimido.content)

def descomprimir():
    tipo = magic.from_file('/tmp/subs')
    
    def archivos():
        limite1 = len(nombre)
        for d in range(limite1):
            print('%s: %s' % (d, nombre))

    print('\nArchivos a extraer:')

    def eleccion_com():
        eleccion1 = int(input("\nElige el número del archivo a extraer:\n- "))
        return eleccion1

    def direcciones():
        source = '/tmp/%s' % (nombre[eleccion1])
        dest = '%s.es.srt' % (wo_ext)
        return source, dest

    if 'Zip' in tipo:
        zip1 = ZipFile(r'/tmp/subs')
        nombre = zip1.namelist()
        archivos()
        eleccion1 = eleccion_com()
        source, dest = direcciones()
        try:
            zip1.extract(nombre[eleccion1],r'/tmp/')
            shutil.move(source, dest)
        except:
            print('Error al extraer. Prueba con otro subtítulo')
    else:
        rar = rarfile.RarFile(r'/tmp/subs')
        nombre = rar.namelist()
        archivos()
        eleccion1 = eleccion_com()
        source, dest = direcciones()
        try:
            rar.extract(nombre[eleccion1], r'/tmp/')
            shutil.move(source, dest)
        except:
            print('Error al extraer. Prueba con otro subtítulo')

    if os.stat(dest).st_size == 0:
        try:
            os.remove(dest)
            print('Hubo un error. Intenta de nuevo')
        except:
            print('Hubo un error. Intenta de nuevo')
    else:
        print('Subtítulo descargado correctamente: %s' % (dest))

def main():
    name = entrada()
    argenteam(name)
    subdivx(name)
    total = arg_subd()
    elegido = elegir(total)
    descomprimir()

if __name__ == '__main__':
    main()
