from tkinter import ttk

from src.frame.anime_details_frame import AnimeDetailsFrame
from src.frame.home_frame import HomeFrame
from src.frame.search_anime_frame import SearchAnimeFrame
from src.frame.view_list_frame import ViewListFrame


class Application(ttk.Frame):
    def __init__(self, master=None, kitsu_client=None, anime_list=None):
        super().__init__(master)
        self.master = master
        self.anime_list = anime_list
        self.kitsu_client = kitsu_client
        self.tabControl = ttk.Notebook(self)
        self.homeFrameTab = HomeFrame(self.display_anime_details_page, master=self.tabControl)
        self.searchAnimeTab = SearchAnimeFrame(kitsu_client, self.display_anime_details_page, self.tabControl)
        self.viewListTab = ViewListFrame(self.tabControl, anime_list=anime_list)
        self.animeDetailsFrame = AnimeDetailsFrame(kitsu_client, self.close_anime_details_page, master=self,
                                                   anime_list=anime_list)
        self.master = master
        self.pack()
        self.create_widgets()
        self.style = ttk.Style(self.master)
        self.style.configure('TNotebook.Tab', width=self.master.winfo_screenwidth())
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.close_anime_details_page()

    def display_anime_details_page(self, anime):
        self.tabControl.pack_forget()
        self.animeDetailsFrame.set_anime(anime)
        self.animeDetailsFrame.pack(fill='both', expand=1)

    def close_anime_details_page(self):
        self.animeDetailsFrame.pack_forget()
        self.tabControl.pack(fill='both', expand=1)

    def create_widgets(self):
        self.tabControl.columnconfigure(0, weight=1)
        self.tabControl.rowconfigure(0, weight=1)
        self.tabControl.add(self.homeFrameTab, text='Accueil')
        self.tabControl.add(self.searchAnimeTab, text='Rechercher')
        self.tabControl.add(self.viewListTab, text='View list')
        self.tabControl.pack(fill='both', expand=1)
