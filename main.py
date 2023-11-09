from tkinter import Tk, Label, Button, Entry, StringVar, Text, Scrollbar, ttk
from ocr_thread import OCRThread
from filedialog_helper import FileDialogHelper
from gui import GUI

def main():
    root = Tk()
    root.title("OCR App")

    # Instanciar la interfaz de usuario
    gui = GUI(root)

    # Configurar los comandos para los botones
    gui.set_image_folder_command(lambda: FileDialogHelper.select_image_folder(gui.image_folder_path))
    gui.set_excel_path_command(lambda: FileDialogHelper.select_excel_path(gui.excel_file_path))
    gui.set_output_folder_command(lambda: FileDialogHelper.select_output_folder(gui.output_folder_path))
    gui.set_start_ocr_command(lambda: OCRThread.start_ocr_thread(
        gui.image_folder_path.get(),
        gui.excel_file_path.get(),
        gui.text_widget,
        gui.progress,
        gui.processing_status,
        gui.output_folder_path.get()
    ))

    root.mainloop()

if __name__ == "__main__":
    main()
