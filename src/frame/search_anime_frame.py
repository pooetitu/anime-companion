from tkinter import ttk, filedialog


class SearchAnimeFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.container = ttk.Frame(self)
        self.textField = ttk.Entry(self.container)
        self.searchButton = ttk.Button(self.container, text="Chercher")
        self.selectFileButton = ttk.Button(self, text="Chercher par image")
        self.create_widgets()

    def create_widgets(self):
        self.searchButton.pack()
        self.container.pack(side="top")
        self.textField.pack(in_=self.container, side="left")
        self.searchButton.pack(in_=self.container, side="left")
        self.selectFileButton["command"] = self.open_file_selection
        self.selectFileButton.pack()

    def open_file_selection(self):
        file = filedialog.askopenfile(parent=self, mode='rb', title='Choisissez une image à rechercher', filetypes=[
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg")])
        if file:
            print(file.read())
