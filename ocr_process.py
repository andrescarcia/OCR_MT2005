from concurrent.futures import ThreadPoolExecutor
import os
import pandas as pd
from ocr import OCR

class OCRProcess:
    @staticmethod
    def start_ocr_process(image_folder, excel_path, text_widget, progress, status_var, output_folder):
        if not image_folder or not excel_path:
            text_widget.insert('end', "Por favor, selecciona la carpeta de imágenes y la ruta del archivo de Excel.\n")
            return
        
        image_files = [filename for filename in os.listdir(image_folder)
                    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
        total_images = len(image_files)
        progress['maximum'] = total_images
        progress['value'] = 0

        data = []

        with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
            futures = []
            for filename in image_files:
                futures.append(executor.submit(OCR.ocr_image, os.path.join(image_folder, filename), text_widget, output_folder))
            
            for i, future in enumerate(futures):
                try:
                    image_path, result, output_path = future.result()
                    progress['value'] = i + 1
                    percentage = (i + 1) / total_images * 100
                    status_var.set(f"Procesando... {percentage:.2f}%")
                    if result:
                        data.append((image_path, result))
                except Exception as e:
                    text_widget.insert('end', f"Error procesando imagen: {e}\n")

        df = pd.DataFrame(data, columns=['Nombre de archivo', 'Texto'])
        try:
            df.to_excel(excel_path, engine='xlsxwriter')
            text_widget.insert('end', f"El texto de las imágenes ha sido guardado en {excel_path}\n")
        except Exception as e:
            text_widget.insert('end', f"Error al guardar el archivo de Excel: {e}\n")
        finally:
            progress['value'] = 0
            status_var.set("Estado: Proceso completado.")
