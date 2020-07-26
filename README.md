# subcaretin-manual

`subcaretin` busca, descarga, extrae y renombra subtítulos de Subdivx y Argenteam

> Nota: para búsquedas y descargas automáticas, visita [subcaretin-auto](https://github.com/vitiko123/subcaretin-auto)

## Características

* Búsqueda manual de subtítulos en Subdivx y Argenteam
* Decarga y extracción automática del subtítulo elegido para luego ser renombrado de acuerdo al archivo de vídeo referenciado
* Chequeo de integridad de subtítulos descargados
 
## Alistar uso

Primero, instala los módulos necesarios con pip. Este comando depende de la configuración de tu OS, pero la forma más segura y común de introducirlo es la siguiente:
```
pip3 install -r requirements.txt --user
```

## Comenzar

Luego, corre el script con tu intérprete de python. Dependiendo de tu OS, puede ser 'python' o 'python3'. En mi caso es python3 (recorto los resultados para no saturar el README):
```console
[xd@arch subcaretin]$ python3 subcaretin.py Taxi.Driver.1976.Bluray.x264.mkv

Introduce el nombre de la película y su año:
- Taxi Driver 1976

Buscando subtítulos...
0: [Argenteam] Taxi Driver (1976) - Taxi.Driver.%281976%29.DVDRip.DivX-NoGRP
1: [Argenteam] Taxi Driver (1976) - Taxi.Driver.%281976%29.DVDRip.XviD.AC3-Taitongtan
2: [Argenteam] Taxi Driver (1976) - Taxi.Driver.%281976%29.BDRip.x264.720p.DTS-AMIABLE
3: [Argenteam] Taxi Driver (1976) - Taxi.Driver.%281976%29.BDRip.x264.1080p.DTS-AMIABLE
4: Subtitulos de Taxi Driver (1976) - son para la nueva versión taxi driver 1976 1080p  x264-amiable  tome los que subió jfca283 (leanlestat) "taxi driver 1976 720p  dts x264 ebp" y los resincronicé  espero les sirva
5: Subtitulos de Taxi Driver (1976) - sirve para taxi driver [bdrip-1080p-multilang-multisub-chapters][rip by max]
6: Subtitulos de Taxi Driver (1976) - para la version de "zeus diaz" que ocupa 700 mb
7: Subtitulos de Taxi Driver (1976) - a este lo bake del donkey, esta coordinado con la version que tewngo de 706 3 mb que comienza directamente con los titulos de la columbia, aparte estan corregidas las letras z que aparecian el algunas partes remplazando a la a, a diferencia de las demas e
8: Subtitulos de Taxi Driver (1976) - son los de leanlestat  ajustados para "taxi driver 1976 720p  dts x264 ebp"
(...)

Elige el número a descargar:
- 3

Bajando: [Argenteam] Taxi Driver (1976) Taxi.Driver.%281976%29.BDRip.x264.1080p.DTS-AMIABLE

Archivos a extraer:
0: ['Taxi.Driver.1976.1080p.BluRay.X264-AMIABLE.srt']

Elige el número del archivo a extraer:
- 0

Subtítulo descargado correctamente: Taxi.Driver.1976.Bluray.x264.es.srt
[xd@arch subcaretin]$
```

## Miscelánea

* Para mejorar la compatibilidad, este script fue reescrito en Python el 25 de Julio de 2020. Anteriormente fue un bash script. Puedes encontrarlo en la historia del repositorio. Eso sí: el historial de commits es un desastre
* Mi subdivx: https://www.subdivx.com/X9X2117299
