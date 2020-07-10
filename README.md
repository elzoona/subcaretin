# subcaretin-manual

`subcaretin` busca, descarga, extrae, renombra y sincroniza subtítulos de Subdivx y Argenteam.

> Nota: para búsquedas y descargas automáticas, visita [subcaretin-auto](https://github.com/vitiko123/subcaretin-auto)

## Demostración
![búsqueda con su bcaretin](screenshots/screen.png "subcaretin en acción")


## Características

* Búsqueda manual de subtítulos en Subdivx y Argenteam
* Decarga y extracción automática del subtítulo elegido para luego ser renombrado de acuerdo al archivo de vídeo referenciado
* Conversión automática de los subtítulos a UTF-8 para evitar problemas de compatibilidad
* Chequeo de integridad de subtítulos descargados
 
## Uso

> Nota: por ahora, el port de python está escrito como la mierda y sólo soporta búsquedas de Subdivx. Es mejor usar el bash script.

```
chmod +x subcaretin
pip3 install -r requirements.txt --user ## Ignora si no usarás el port de python
```
```
## shell
./subcaretin VIDEO.mkv
## python
python3 subcaretin.py VIDEO.mkv
```

## Dependencias
### Obligatorio
#### bash script
* wget
* iconv
* unrar
* unzip
#### python
* ver el archivo de texto "requirements.txt"

## Por hacer

* Hacer un port en Rust o Python

## Miscelánea

* Testeado en Arch Linux, Slackware, Debian Server y Ubuntu Server. ~~Puede que funcione en MAC OS~~. Habrán problemas con las flags de `grep` en MAC, pero se pueden resolver manualmente. Es muy probable que el script funcione en el subsistema de Linux en Windows 10
* Mi subdivx: https://www.subdivx.com/X9X2117299

## Changelog

### 0.1 - May 19 2020

- Lanzamiento inicial

### 0.2 - May 27 2020

- Soporte para Argenteam agregado

### 0.3 - Jul 03 2020

- Soporte para ffsubsync eliminado
