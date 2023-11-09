from tkinter import Label, Entry, StringVar, Text, Scrollbar, Button, ttk

class GUI:
    def __init__(self, master):
        self.master = master

        # Definir las variables StringVar para los paths
        self.image_folder_path = StringVar()
        self.excel_file_path = StringVar()
        self.output_folder_path = StringVar()
        self.processing_status = StringVar()
        self.processing_status.set("Estado: Esperando iniciar.")

        # Configurar la disposición de los widgets
        self.layout_widgets()

    def layout_widgets(self):
        Label(self.master, text="Carpeta de Imágenes:").grid(row=0, column=0, sticky='e')
        Entry(self.master, textvariable=self.image_folder_path, width=50).grid(row=0, column=1)
        Button(self.master, text="Seleccionar").grid(row=0, column=2)

        Label(self.master, text="Guardar Excel en:").grid(row=1, column=0, sticky='e')
        Entry(self.master, textvariable=self.excel_file_path, width=50).grid(row=1, column=1)
        Button(self.master, text="Seleccionar").grid(row=1, column=2)

        Label(self.master, text="Directorio de Salida:").grid(row=2, column=0, sticky='e')
        Entry(self.master, textvariable=self.output_folder_path, width=50).grid(row=2, column=1)
        Button(self.master, text="Seleccionar").grid(row=2, column=2)

        Button(self.master, text="Iniciar OCR").grid(row=3, column=0, columnspan=3)

        self.text_widget = Text(self.master, height=10, width=80)
        scrollbar = Scrollbar(self.master, command=self.text_widget.yview)
        self.text_widget.configure(yscrollcommand=scrollbar.set)
        self.text_widget.grid(row=4, column=0, columnspan=2)
        scrollbar.grid(row=4, column=2, sticky='nsew')

        self.progress = ttk.Progressbar(self.master, orient='horizontal', length=300, mode='determinate')
        self.progress.grid(row=5, column=0, columnspan=3, pady=10)

        Label(self.master, textvariable=self.processing_status).grid(row=6, column=0, columnspan=3)

    def set_image_folder_command(self, command):
        self.master.grid_slaves(row=0, column=2)[0].config(command=command)

    def set_excel_path_command(self, command):
        self.master.grid_slaves(row=1, column=2)[0].config(command=command)

    def set_output_folder_command(self, command):
        self.master.grid_slaves(row=2, column=2)[0].config(command=command)

    def set_start_ocr_command(self, command):
        self.master.grid_slaves(row=3, column=0)[0].config(command=command)
