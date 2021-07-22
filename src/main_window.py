from tkinter import ttk

from src.frame.home_frame import HomeFrame
from src.frame.search_anime_frame import SearchAnimeFrame
from src.frame.view_list_frame import ViewListFrame


class Application(ttk.Frame):
    def __init__(self, master=None, kitsu_client=None):
        super().__init__(master)
        self.tabControl = ttk.Notebook(self)
        self.homeFrameTab = HomeFrame(self.tabControl)
        self.searchAnimeTab = SearchAnimeFrame(self.tabControl, kitsu_client)
        self.viewListTab = ViewListFrame(self.tabControl)
        self.master = master
        self.pack()
        self.create_widgets()
        self.style = ttk.Style(self.master)
        self.style.configure('TNotebook.Tab', width=self.master.winfo_screenwidth())
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def create_widgets(self):
        self.tabControl.columnconfigure(0, weight=1)
        self.tabControl.rowconfigure(0, weight=1)
        self.tabControl.add(self.homeFrameTab, text='Accueil')
        self.tabControl.add(self.searchAnimeTab, text='Rechercher')
        self.tabControl.add(self.viewListTab, text='View list')
        self.tabControl.pack(fill='both', expand=1)
