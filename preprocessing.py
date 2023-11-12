


import cv2
import numpy as np
import pytesseract
import re

class Preprocessor:
    @staticmethod
    def preprocess_image(image_path, scale_factor=1.5):
        # Leer la imagen desde el archivo
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Cambiar el tamaño de la imagen (escalar)
        width = int(img.shape[1] * scale_factor)
        height = int(img.shape[0] * scale_factor)
        img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
        # Preprocesamiento de la imagen escalada
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        # Intentar detectar la orientación del texto
        try:
            osd = pytesseract.image_to_osd(img)
            angle = int(re.search(r'(?<=Rotate: )\d+', osd).group(0))
            if angle != 0:
                center = (width // 2, height // 2)
                M = cv2.getRotationMatrix2D(center, angle, 1.0)
                img = cv2.warpAffine(img, M, (width, height), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        except (pytesseract.pytesseract.TesseractError, ValueError) as e:
            print(f"No se pudo obtener la orientación de la imagen {image_path}. Error: {e}")
            # Aquí podrías implementar una rotación alternativa basada en la detección de bordes si fuera necesario.

        return img



"""
import cv2
import numpy as np

class Preprocessor:
    @staticmethod
    def preprocess_image(image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        coords = np.column_stack(np.where(img > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        
        return img
"""
"""
import cv2
import numpy as np
import pytesseract
import re  # Importa el módulo de expresiones regulares

class Preprocessor:
    @staticmethod
    def preprocess_image(image_path):
        # Carga la imagen en escala de grises
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        # Aplica un umbral para crear una imagen binaria
        _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        
        try:
            # Utiliza pytesseract para obtener la orientación del texto
            osd = pytesseract.image_to_osd(img)
            angle = int(re.search('(?<=Rotate: )\d+', osd).group(0))

            # Si el ángulo es diferente de cero, procede a rotar la imagen
            if angle != 0:
                # Calcula el centro de la imagen y la matriz de rotación
                (h, w) = img.shape[:2]
                center = (w // 2, h // 2)
                M = cv2.getRotationMatrix2D(center, angle, 1.0)
                # Aplica la rotación
                img = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        except (pytesseract.pytesseract.TesseractError, ValueError) as e:
            # Manejo de errores si pytesseract no puede obtener los datos de orientación
            print(f"No se pudo obtener la orientación de la imagen {image_path}. Error: {e}")

        return img


def upscale_image(image_path, scale_factor):
    # Leer la imagen desde el archivo
    img = cv2.imread(image_path)
    # Calcular las nuevas dimensiones
    width = int(img.shape[1] * scale_factor)
    height = int(img.shape[0] * scale_factor)
    # Cambiar el tamaño de la imagen
    upscaled_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_CUBIC)
    return upscaled_img
"""
# Usar la función y guardar la imagen escalada
#upscaled_image = upscale_image('tu_imagen.jpg', 2) # Cambiar el factor de escala según sea necesario
#cv2.imwrite('imagen_escalada.jpg', upscaled_image)
