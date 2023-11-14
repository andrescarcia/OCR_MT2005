# Manual de Instalación del Programa OCR

Este documento proporciona instrucciones detalladas sobre cómo configurar y ejecutar el programa OCR (Reconocimiento Óptico de Caracteres) tanto en sistemas operativos Windows como en Linux. 
# Nota importante
Se recomienda el uso de una distro Linux, Windows suele dar problemas con Tesseract. Ademas, se recomienda usar imagenes de pequeño tamaño, el programa es CPU intensivo, y estandarizar lo que se desea extraer de las imagenes es primordial para el uso del script.

## Requisitos del Sistema

- **Windows**: Windows 7 o superior.
- **Linux**: Cualquier distribución reciente.
- Python 3.6 o superior instalado.
- Acceso a Internet para la instalación de paquetes.

## Instalación en Windows

### Instalación de Tesseract OCR

1. Descargue el instalador de Tesseract OCR desde su [página de GitHub](https://github.com/tesseract-ocr/tesseract/releases).
2. Ejecute el instalador y siga las instrucciones. Asegúrese de permitir que Tesseract se agregue a la variable de entorno PATH.

### Instalación de Dependencias de Python

Abra la línea de comandos y ejecute:

```shell
pip install pillow pandas pytesseract tqdm
```
Si tiene más de una versión de Python instalada, puede que necesite utilizar pip3.

# Instalación en Linux
## Instalación de Tesseract OCR
Abra una terminal y ejecute:
```shell
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-spa
```
## Instalación de Dependencias de Python
En la terminal, ejecute:
```shell
pip3 install pillow pandas pytesseract tqdm
```
# Configuración del Programa OCR
Guarde el script de Python proporcionado en un archivo con la extensión .py, por ejemplo, script_ocr.py.

# Ejecución del Programa OCR
## En Windows
1. Abra la línea de comandos y navegue hasta la carpeta donde guardó el script.
```shell
cd C:\Users\TuUsuario\DirectorioDelScript
```
2. Ejecute el script con Python:
```shell
python script_ocr.py
```
# En Linux
Abra una terminal y navegue hasta la carpeta donde guardó el script.
```shell
cd /ruta/al/directorio/del/script
```
Ejecute el script con Python:
```shell
python3 script_ocr.py
```
Siga las instrucciones en la terminal, proporcionando la ruta de la carpeta de imágenes y la ruta de salida del archivo Excel cuando se le solicite.

# Notas Adicionales
Si encuentra errores relacionados con la ruta de Tesseract OCR en Windows, puede que necesite especificarla manualmente en el script. Encuentre la ruta de instalación de Tesseract (usualmente C:\Program Files\Tesseract-OCR) y añada la siguiente línea al principio del script:
```shell
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
En Linux, asegúrese de que Tesseract OCR esté correctamente instalado y que el idioma requerido esté disponible.

Si hay problemas con la ejecución del script o errores de instalación, asegúrese de que todas las rutas y comandos estén escritos correctamente y que todas las dependencias estén instaladas.
