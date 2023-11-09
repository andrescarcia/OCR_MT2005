import threading
from ocr_process import OCRProcess

class OCRThread:
    @staticmethod
    def start_ocr_thread(image_folder, excel_path, text_widget, progress, status_var, output_folder):
        ocr_thread = threading.Thread(
            target=OCRProcess.start_ocr_process,
            args=(image_folder, excel_path, text_widget, progress, status_var, output_folder)
        )
        ocr_thread.start()
