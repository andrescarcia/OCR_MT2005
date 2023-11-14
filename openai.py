import os
import base64
import requests
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
'''
lista de comandos para instalar las librerias necesarias
pip install pandas requests tqdm
pip install openai
pip install python-dotenv

'''

load_dotenv()
# Configura tu clave API de OpenAI
api_key = "API_KEY"

def leer_imagenes(carpeta):
    archivos = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.jpg') or archivo.endswith('.png'):
            archivos.append(archivo)
    return archivos

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def procesar_imagenes(archivos, carpeta):
    dataset = []
    for archivo in tqdm(archivos, desc="Procesando imágenes"):
        print(f"Procesando {archivo}...")
        image_path = f"{carpeta}/{archivo}"
        base64_image = encode_image(image_path)

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "This image has numbers and letters, i need you to extract them and send it to me, only respond with the code, the code has numbers and letters"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            respuesta = response.json()
            texto = respuesta['choices'][0]['message']['content']
            dataset.append({'imagen': archivo, 'texto': texto})
        else:
            print(f"Error procesando {archivo}: {response.status_code}")

    return dataset


def guardar_en_excel(dataset, nombre_archivo):
    df = pd.DataFrame(dataset)
    df.to_excel(nombre_archivo, index=False)

# Ruta de la carpeta donde están las imágenes y donde se guardará el Excel
carpeta_imagenes = r'C:\Users\AndreScarcia\OneDrive - MTIC\Escritorio\temporales'
ruta_excel = r'C:\Users\AndreScarcia\OneDrive - MTIC\Escritorio\temporales\dataset.xlsx'

# Procesar
archivos = leer_imagenes(carpeta_imagenes)
dataset = procesar_imagenes(archivos, carpeta_imagenes)
guardar_en_excel(dataset, ruta_excel)

print(f"Proceso completado. El dataset se ha guardado en '{ruta_excel}'.")
