from tkinter import ttk

from src.frame.view_list_frame import ViewListFrame


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.style = ttk.Style(self.master)
        self.style.configure('TNotebook.Tab', width=self.master.winfo_screenwidth())
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_widgets(self):
        self.tabControl = ttk.Notebook(self)

        self.tabControl.columnconfigure(0, weight=1)
        self.tabControl.rowconfigure(0, weight=1)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ViewListFrame(self.tabControl)
        self.tabControl.add(self.tab1, text='Accueil')
        self.tabControl.add(self.tab2, text='Rechercher')
        self.tabControl.add(self.tab3, text='View list')
        self.tabControl.pack(fill='both', expand=1)