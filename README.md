# subcaretin-manual

`subcaretin` busca, descarga, extrae, renombra y sincroniza subtítulos de Subdivx y Argenteam.

Nota: visita también [subcaretin-auto](https://github.com/vitiko123/subcaretin-auto)

### Demostración
![búsqueda con subcaretin](screenshots/screen.png "subcaretin en acción")


## Características

* Búsqueda manual de subtítulos en Subdivx y Argenteam
* Decarga y extracción automática del subtítulo elegido para luego ser renombrado de acuerdo al archivo de vídeo referenciado
* Sincronización opcional del subtítulo gracias a [ffsubsync (subsync)](https://github.com/smacke/ffsubsync), programa escrito en python por [smacke](https://github.com/smacke)
* Conversión automática de los subtítulos a UTF-8 para evitar problemas de compatibilidad
* Chequeo de integridad de subtítulos descargados

## Uso
```
chmod +x subcaretin
```
```
./subcaretin VIDEO.mkv
./subcaretin VIDEO.mp4
```

## Dependencias
### Obligatorio
* wget
* iconv
* unrar
* unzip

### Opcional
* [ffsubsync (subsync)](https://github.com/smacke/ffsubsync) (para sincronizar los subtítulos descargados) 

## Por hacer

* Volver a comprimir subtítulos re-sincronizados con ffsubsync para que de esta manera el usuario pueda subirlos cómodamente a Subdivx y mejorar la database
* Hacer un port en Rust o Python

## Miscelánea

* Testeado en Arch Linux, Slackware, Debian Server y Ubuntu Server. ~~Puede que funcione en MAC OS~~. Habrán problemas con las flags de `grep` en MAC, pero se pueden resolver manualmente. Es muy probable que el script funcione en el subsistema de Linux en Windows 10
* Mi subdivx: https://www.subdivx.com/X9X2117299

## Changelog

### 0.1 - May 19 2020

- Lanzamiento inicial

### 0.2 - May 27 2020

- Soporte para Argenteam agregado


