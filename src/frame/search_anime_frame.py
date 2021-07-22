import asyncio
import threading, requests
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
        self.searchButton["command"] = self.search_thread
        self.selectFileButton["command"] = self.open_file_selection
        self.selectFileButton.pack()

    def open_file_selection(self):
        file = filedialog.askopenfile(parent=self, mode='rb', title='Choisissez une image à rechercher', filetypes=[
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg")])
        if file:
            search_image_thread = threading.Thread(target=self.search_by_image, kwargs={'file': file})
            search_image_thread.start()

    def search_by_image(self, file=None):
        self.disable_search_buttons()
        anime = requests.post("https://api.trace.moe/search?anilistInfo", files={"image": file}).json()
        self.search_thread(name=anime["result"][0]["anilist"]["title"]["romaji"])
        self.enable_search_buttons()

    def search_thread(self, name=None):
        image_recuperation_thread = threading.Thread(target=self.search_by_name_wrapper, kwargs={'name': name})
        image_recuperation_thread.start()

    def search_by_name_wrapper(self, name=None):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.search_by_name(name=name))

    async def search_by_name(self, name=None):
        self.disable_search_buttons()
        if name is not None:
            animes = await self.kitsu_client.search('anime', name)
        else:
            animes = await self.kitsu_client.search('anime', self.searchField.get())
        self.display_anime_infos(animes)
        self.enable_search_buttons()

    def display_anime_infos(self, animes):
        self.anime_list_clear()
        for anime in animes:
            card = AnimeInfoCard(anime, self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5, fill='both', expand=1)

    def anime_list_clear(self):
        for card in self.anime_list:
            try:
                card.destroy()
            except Exception:
                pass
        self.anime_list.clear()

    def disable_search_buttons(self):
        self.searchButton["state"] = "disabled"
        self.selectFileButton["state"] = "disabled"

    def enable_search_buttons(self):
        self.searchButton["state"] = "normal"
        self.selectFileButton["state"] = "normal"
