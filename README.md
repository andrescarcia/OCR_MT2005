- **[OCR MT2005 V-OCR-LOCAL](#ocr-mt2005-v-ocr-local)**
- **[OCR MT2005 V-OCR-OPENAI (script)](#ocr-mt2005-v-ocr-openai)**
- **[OCR MT2005 V-OCR-OPENAI (CON GUI)](#ocr-mt2005-v-ocr-openai-gui)**
- **[Ejemplos de Imágenes](#ejemplos-de-imágenes)**
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

## Uso de la Versión OCR Local con GUI

Para aquellos usuarios que prefieran utilizar la versión OCR local, esta cuenta con una interfaz gráfica de usuario (GUI) que facilita el proceso. Después de instalar todas las dependencias y herramientas necesarias, como se explicó anteriormente, puedes seguir estos pasos para utilizar la GUI:

### Pasos para Utilizar la GUI del OCR Local
La versión OCR local incluye una interfaz gráfica de usuario (GUI) diseñada para facilitar el proceso de reconocimiento óptico de caracteres. A diferencia de la versión que utiliza GPT-4 Vision de OpenAI, la versión local realiza un preprocesamiento binario de las imágenes para maximizar la tasa de éxito en el reconocimiento de texto.

1. **Seleccionar la Ruta de las Imágenes**:
   - Desde la GUI, selecciona la ruta de la carpeta que contiene las imágenes que deseas procesar.  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/1.png)  

2. **Seleccionar la Ruta para Guardar el Excel**:
   - Elige la ruta de la carpeta donde deseas guardar el archivo Excel con los resultados del procesamiento OCR.  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/2.png)  
   - Tambien debe escribir el nombre que desea darle al excel  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/3.png)  

4. **Seleccionar la Ruta para Guardar las Imágenes Procesadas**:
   - Indica la ruta donde se guardarán las imágenes después de ser procesadas por el OCR.
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/4.png)  

### Nota sobre el Preprocesamiento Binario

La versión con GUI, a diferencia de la versión que utiliza GPT-4 Vision de OpenAI, realiza un preprocesamiento binario de las imágenes. Este paso es crucial para maximizar la tasa de éxito en el reconocimiento de texto, especialmente dado que la IA de OCR local puede no ser tan avanzada como la de OpenAI GPT-4 Vision.

### Ejecución de la GUI

Una vez seleccionadas todas las rutas necesarias, puedes iniciar el proceso de OCR haciendo clic en el botón correspondiente en la GUI. El programa procesará las imágenes y generará el archivo Excel en la ubicación especificada.

Recuerda que la calidad de las imágenes y su adecuación a los requisitos previamente mencionados son factores clave para obtener resultados óptimos en el reconocimiento de texto.


# Notas Adicionales
Si encuentra errores relacionados con la ruta de Tesseract OCR en Windows, puede que necesite especificarla manualmente en el script. Encuentre la ruta de instalación de Tesseract (usualmente C:\Program Files\Tesseract-OCR) y añada la siguiente línea al principio del script:
```shell
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
En Linux, asegúrese de que Tesseract OCR esté correctamente instalado y que el idioma requerido esté disponible.

Si hay problemas con la ejecución del script o errores de instalación, asegúrese de que todas las rutas y comandos estén escritos correctamente y que todas las dependencias estén instaladas.

# OCR MT2005 V-OCR-OPENAI

# Manual de Uso del Script de OCR con OpenAI

Este script utiliza la API de OpenAI para procesar imágenes y extraer texto de ellas. Las imágenes se procesan y el texto extraído se guarda en un archivo Excel. Actualmente esta version no cuenta con una GUI, sin embargo solo se necesita un block de notas o Visual Studio Code para editar el archivo openai.py.  
Por el uso de una API KEY de OpenAI, se debera crear una cuenta en  [OpenAI API](https://openai.com/blog/openai-api), luego de crear una cuenta puede acceder al apartado "API Keys" y luego dar click en "Create new Secret Key" , elegir el nombre que tendra esta key y copiarla en la seccion de codigo "api_key = "API_KEY_HERE" en el archivo openai.py

## Especificaciones para las Imágenes

Para asegurar la eficiencia y precisión en el procesamiento de las imágenes por el script, es importante que las imágenes cumplan con ciertas especificaciones:

- **Tamaño Reducido**: Las imágenes deben ser de tamaño reducido para facilitar un procesamiento rápido y eficiente. Esto es especialmente importante si se procesa un gran número de imágenes.

- **Orientación Horizontal**: Las imágenes deben estar orientadas horizontalmente. Esto asegura que el texto, especialmente los números de serie, sean fácilmente detectables y legibles por el script.

- **Claridad y Precisión**: Las imágenes deben ser claras, con el texto o números de serie bien enfocados y legibles. Evita imágenes borrosas o con texto que esté parcialmente oculto o cortado.

- **Fondo y Contraste**: Un fondo uniforme y un buen contraste entre el texto y el fondo ayudarán a mejorar la precisión del reconocimiento de texto.

## Ejemplos de Imágenes
### no optimas pero funcionales
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/116_Kd0xnGNwU8.png)  
**Imagen 1, no optima pero funcional ✅**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/212_vR8y7RhV0v.png)  
**Imagen 2, no optima pero funcional ✅**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/32_acVkZpMm8v.png)  
**Imagen 3, no optima pero funcional ✅**  

### Imagenes inapropiadas
- *Nota:* A pesar de no ser apropiadas, aún muchas pueden seguir siendo interpretadas por GPT-4 Turbo, sin embargo no es capaz de discernir el codigo o serial que se desea extraer si la imagen no contiene solamente el serial (como se ve en la imagen 7). En las imagenes funcionales y optimas se demuestra como deben verse las imagenes solo con el serial o codigo.
- ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/247_zYcDGz1Q8p.png)   
**Imagen 4, imagen inapropiada ❌**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/49_BOd5Kk30mg.png)  
**Imagen 5, imagen inapropiada ❌**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/167_PKskS1iV4y.png)  
**Imagen 6, imagen inapropiada ❌**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/215_wJqQb6T8Ho.png)  
**Imagen 7, imagen inapropiada ❌**  

### Imagenes optimas
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/preprocessed_1_1AOmlCqkbJ.png)  
**Imagen 8, imagen optima ☑️**  
![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/preprocessed_2_1KngZ3w2VK.png)  
**Imagen 9, imagen optima ☑️**  
Recuerda que la calidad de las imágenes influye directamente en la precisión del texto extraído. Imágenes que no cumplan con estas especificaciones pueden resultar en errores o en una baja calidad en la extracción del texto.


## Uso Eficiente de GPT-4 Vision y Costos Asociados

Para optimizar el uso de GPT-4 Vision en el procesamiento de imágenes y entender cómo se calculan los costos, es importante considerar las siguientes pautas y detalles:

### Especificaciones de las Imágenes para GPT-4 Vision

- **Detalle de la Imagen**: GPT-4 Vision ofrece dos opciones de detalle: `low` y `high`. La opción `low` tiene un costo fijo, mientras que `high` varía según el tamaño y la cantidad de cuadros de 512px que componen la imagen.

- **Tamaño y Escalado**: Para la opción `high`, las imágenes se escalan para ajustarse dentro de un cuadrado de 2048 x 2048, manteniendo su relación de aspecto. Luego, se escalan de tal manera que el lado más corto de la imagen mida 768px.

### Cálculo de Costos

- **Detalle Bajo (`low`)**: Todas las imágenes con `detail: low` tienen un costo fijo de 85 tokens, independientemente de su tamaño.

- **Detalle Alto (`high`)**: 
  - Las imágenes se dividen en cuadros de 512px. Cada cuadro tiene un costo de 170 tokens.
  - Se añaden siempre 85 tokens adicionales al total final.
  (Para nuestro caso de uso con las imagenes de ejemplo en este repo, el costo fue de 0,01$ por 6 imagenes. siendo estas pequeñas)

#### Ejemplos de Costos

1. **Imagen de 1024 x 1024 en Modo `high`**: 
   - Costo: 765 tokens.
   - Cálculo: 4 cuadros de 512px (170 * 4) + 85 tokens adicionales.

2. **Imagen de 2048 x 4096 en Modo `high`**: 
   - Costo: 1105 tokens.
   - Cálculo: 6 cuadros de 512px (170 * 6) + 85 tokens adicionales.

3. **Imagen de 4096 x 8192 en Modo `low`**: 
   - Costo fijo de 85 tokens.

### Referencias Adicionales

Para más información sobre el uso de GPT-4 Vision y ejemplos prácticos, puedes consultar los siguientes enlaces:

- [Guía de GPT-4 Vision en OpenAI](https://platform.openai.com/docs/guides/vision)
- [Ejemplos de Uso de GPT-4 Vision para Entendimiento de Video](https://cookbook.openai.com/examples/gpt_with_vision_for_video_understanding)

Es crucial seleccionar el nivel de detalle adecuado y tener en cuenta el tamaño de las imágenes para gestionar de manera eficiente los costos asociados al uso de GPT-4 Vision.

## Requisitos Previos

Antes de ejecutar el script, asegúrate de tener instalado Python y las siguientes librerías:

```shell
pip install pandas requests tqdm
pip install openai
```

## Configuración
Para la configuracion debe abrir el archivo openai.py en el block de notas o en cualquier editor de codigo.
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

## OCR MT2005-V-OCR-OpenAI GUI
Para el uso de la herramienta con GUI se deben seguir los mismos pasos anteriores, y sencillamente ejecutar el archivo llamdo "openaiGUI.py" 
1. **Seleccionar la Ruta de las Imágenes**:
   - Desde la GUI, selecciona la ruta de la carpeta que contiene las imágenes que deseas procesar.  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/1GUI.png)  

2. **Seleccionar la Ruta para Guardar el Excel**:
   - Elige la ruta de la carpeta donde deseas guardar el archivo Excel con los resultados del procesamiento OCR.  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/2GUI.png)  
   - Tambien debe escribir el nombre que desea darle al excel  
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/3GUI.png)
3. **Empezar el Procesamiento**:     
   - ![](https://github.com/andrescarcia/OCR_MT2005/blob/main/Imagenes%20Ejemplo/Imagenes%20Tutorial/4GUI.png)
## Notas Adicionales

- El script está configurado para procesar imágenes con extensiones `.jpg` y `.png`.
- Asegúrate de que la ruta de las imágenes y del archivo Excel sean accesibles y correctas.
- Si encuentras algún error, verifica que todas las dependencias estén instaladas y que tu clave API de OpenAI sea válida.

