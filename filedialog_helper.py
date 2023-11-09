from tkinter import filedialog

class FileDialogHelper:
    @staticmethod
    def select_image_folder(entry):
        folder_selected = filedialog.askdirectory()
        entry.set(folder_selected)

    @staticmethod
    def select_excel_path(entry):
        file_selected = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )
        entry.set(file_selected)

    @staticmethod
    def select_output_folder(entry):
        folder_selected = filedialog.askdirectory()
        entry.set(folder_selected)
