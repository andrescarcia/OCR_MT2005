- **[OCR MT2005 V-OCR-LOCAL](#ocr-mt2005-v-ocr-local)**
- **[OCR MT2005 V-OCR-OPENAI (mejor)](#ocr-mt2005-v-ocr-openai)**
# Manual de Instalación del Programa OCR LOCAL
## OCR MT2005 V-OCR-LOCAL
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

1. Descargue el instalador de Tesseract OCR desde su [página de GitHub](https://github.com/tesseract-ocr/tesseract/releases). tambien se puede seguir un [Tutorial de youtube](https://www.youtube.com/watch?v=DG5D8A3zi4o)
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
El repositorio puede ser guardado en cualquier lugar en su computadora, si decide usar la version OCR local, lo unico que debe hacer es hacer click dos veces sobre el archivo main.py, si todo esta correctamente instalado, se debe mostrar la GUI en su pantalla.
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

# OCR MT2005 V-OCR-OPENAI

# Manual de Uso del Script de OCR con OpenAI

Este script utiliza la API de OpenAI para procesar imágenes y extraer texto de ellas. Las imágenes se procesan y el texto extraído se guarda en un archivo Excel.

## Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado Python y las siguientes librerías:

```shell
pip install pandas requests tqdm
pip install openai
```

## Configuración

1. **Configura tu clave API de OpenAI**:
   - Reemplaza `API_KEY_HERE` en el script con tu clave API de OpenAI.

2. **Ruta de las Imágenes y del Archivo Excel**:
   - Modifica las variables `carpeta_imagenes` y `ruta_excel` en el script para indicar la ruta de tus imágenes y dónde deseas guardar el archivo Excel.

## Ejecución del Script

1. **Abrir Terminal o CMD**:
   - Navega hasta el directorio donde se encuentra el script.

2. **Ejecutar el Script**:
   - Ejecuta el script con el siguiente comando:
     ```shell
     python nombre_del_script.py
     ```
   - Asegúrate de reemplazar `nombre_del_script.py` con el nombre real de tu archivo.

3. **Procesamiento**:
   - El script procesará las imágenes de la carpeta especificada y guardará los resultados en el archivo Excel indicado.

4. **Revisar Resultados**:
   - Una vez completado el proceso, revisa el archivo Excel generado para ver los textos extraídos.

## Notas Adicionales

- El script está configurado para procesar imágenes con extensiones `.jpg` y `.png`.
- Asegúrate de que la ruta de las imágenes y del archivo Excel sean accesibles y correctas.
- Si encuentras algún error, verifica que todas las dependencias estén instaladas y que tu clave API de OpenAI sea válida.

