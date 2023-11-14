import os
import base64
import requests
import pandas as pd
from tkinter import filedialog, messagebox
import tkinter as tk
from tkinter import ttk
from dotenv import load_dotenv

'''
lista de comandos para instalar las librerias necesarias
pip install pandas requests tqdm
pip install openai
pip install python-dotenv

'''

# Configura tu clave API de OpenAI
api_key = "API_KEY"
load_dotenv()
def leer_imagenes(carpeta):
    archivos = []
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.jpg') or archivo.endswith('.png'):
            archivos.append(archivo)
    return archivos

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def procesar_imagenes(archivos, carpeta, progress_callback):
    dataset = []
    for i, archivo in enumerate(archivos):
        print(f"Procesando {archivo}...")
        image_path = os.path.join(carpeta, archivo)
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
                            "text": "This image has numbers and letters, I need you to extract them and send it to me, only respond with the code, the code has numbers and letters"
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

        # Actualizar la barra de progreso
        progress_callback(i + 1, len(archivos))

    return dataset

def guardar_en_excel(dataset, nombre_archivo):
    df = pd.DataFrame(dataset)
    df.to_excel(nombre_archivo, index=False)

def seleccionar_carpeta_imagenes():
    carpeta_imagenes = filedialog.askdirectory()
    entrada_ruta_imagenes.delete(0, tk.END)
    entrada_ruta_imagenes.insert(0, carpeta_imagenes)

def seleccionar_ruta_excel():
    ruta_excel = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    entrada_ruta_excel.delete(0, tk.END)
    entrada_ruta_excel.insert(0, ruta_excel)

def iniciar_proceso():
    carpeta_imagenes = entrada_ruta_imagenes.get()
    ruta_excel = entrada_ruta_excel.get()

    if not carpeta_imagenes or not ruta_excel:
        messagebox.showerror("Error", "Por favor, seleccione la carpeta de imágenes y la ruta del archivo Excel.")
        return

    archivos = leer_imagenes(carpeta_imagenes)
    if not archivos:
        messagebox.showerror("Error", "No se encontraron imágenes en la carpeta seleccionada.")
        return

    def update_progress(current, total):
        barra_progreso['value'] = (current / total) * 100
        root.update_idletasks()

    dataset = procesar_imagenes(archivos, carpeta_imagenes, update_progress)
    guardar_en_excel(dataset, ruta_excel)

    messagebox.showinfo("Completado", "Proceso completado. El dataset se ha guardado en el archivo Excel seleccionado.")

# Crear ventana principal
root = tk.Tk()
root.title("Procesador de Imágenes")

# Crear y colocar widgets
etiqueta_ruta_imagenes = tk.Label(root, text="Ruta de imágenes:")
etiqueta_ruta_imagenes.pack()

entrada_ruta_imagenes = tk.Entry(root, width=50)
entrada_ruta_imagenes.pack()

boton_seleccionar_carpeta = tk.Button(root, text="Seleccionar Carpeta de Imágenes", command=seleccionar_carpeta_imagenes)
boton_seleccionar_carpeta.pack()

etiqueta_ruta_excel = tk.Label(root, text="Ruta de archivo Excel:")
etiqueta_ruta_excel.pack()

entrada_ruta_excel = tk.Entry(root, width=50)
entrada_ruta_excel.pack()

boton_seleccionar_excel = tk.Button(root, text="Seleccionar Archivo Excel", command=seleccionar_ruta_excel)
boton_seleccionar_excel.pack()

boton_procesar = tk.Button(root, text="Procesar", command=iniciar_proceso)
boton_procesar.pack()

# Barra de progreso
barra_progreso = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
barra_progreso.pack()

# Iniciar la aplicación
root.mainloop()
