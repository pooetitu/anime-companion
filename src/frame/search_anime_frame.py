import asyncio
from tkinter import ttk, filedialog

from src.cards.anime_info_card import AnimeInfoCard
from src.frame.scrollable_frame import ScrollableFrame


class SearchAnimeFrame(ttk.Frame):
    def __init__(self, master=None, kitsu_client=None):
        super().__init__(master)
        self.master = master
        self.kitsu_client = kitsu_client
        self.pack()
        self.container = ttk.Frame(self)
        self.searchField = ttk.Entry(self.container)
        self.searchButton = ttk.Button(self.container, text="Chercher")
        self.selectFileButton = ttk.Button(self, text="Chercher par image")
        self.create_widgets()
        self.anime_list = []
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)

    def create_widgets(self):
        self.searchButton.pack()
        self.container.pack(side="top")
        self.searchField.pack(in_=self.container, side="left")
        self.searchButton.pack(in_=self.container, side="left")
        self.searchButton["command"] = self.search_by_name_wrapper
        self.selectFileButton["command"] = self.open_file_selection
        self.selectFileButton.pack()

    def open_file_selection(self):
        file = filedialog.askopenfile(parent=self, mode='rb', title='Choisissez une image à rechercher', filetypes=[
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg")])
        if file:
            print(file.read())

    def search_by_name_wrapper(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.search_by_name())

    async def search_by_name(self):
        animes = await self.kitsu_client.search('anime', self.searchField.get())
        self.display_anime_infos(animes)

    def display_anime_infos(self, animes):
        self.anime_list_clear()
        for anime in animes:
            card = AnimeInfoCard(anime, self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5, anchor='nw')

    def anime_list_clear(self):
        for card in self.anime_list:
            card.destroy()
        self.anime_list.clear()
