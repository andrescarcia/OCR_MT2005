import os
from PIL import Image
import pytesseract
from preprocessing import Preprocessor

class OCR:
    custom_config = r'--oem 3 --psm 6'
    @staticmethod
    def ocr_image(image_path, text_widget, output_folder):
        base_name = os.path.basename(image_path) if image_path else "Unknown"
        
        try:
            preprocessed_img = Preprocessor.preprocess_image(image_path)
            img = Image.fromarray(preprocessed_img)
            #text = pytesseract.image_to_string(img, lang='eng', config='--psm 7')
            text = pytesseract.image_to_string(img, lang='eng', config=OCR.custom_config)
            text_widget.insert('end', f"Procesado: {image_path}\n")
            
            output_path = os.path.join(output_folder, f"preprocessed_{base_name}")
            img.save(output_path)
            
            return base_name, text, output_path
        except Exception as e:
            text_widget.insert('end', f"Error procesando {image_path}: {e}\n")
            return base_name, None, None
