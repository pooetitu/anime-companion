import asyncio
import threading
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from kitsu.models import Anime


class ViewListCard(ttk.Frame):
    def __init__(self, anime, master=None, kitsu=None):
        super().__init__(master)
        self.destroyed = False
        self.kitsu_client = kitsu
        self.master = master
        self.anime = anime
        self.create_widgets()
        threading.Thread(target=self.search_by_name_wrapper, kwargs={'name': anime["title"]}).start()
        self.pack()



    def create_widgets(self):

        # IMAGE / TITLE / DATE IN LEFT
        self.image_label = ttk.Label(self)
        self.image_label.pack(in_=self, side="left", padx=5)

        self.title = ttk.Label(self)
        self.title.pack(side="left")
        self.date = ttk.Label(self)
        self.date.pack(in_=self, side="left")

        # OPITONS RIGHT
        self.delete_original = Image.open('./assets/icons/delete_icon.png')
        delete_resized = self.delete_original.resize((30, 30), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(delete_resized)
        self.delete_button = ttk.Button(self, image=self.delete_icon)
        self.delete_button.pack(side="right", padx=5)

    def set_anime_card(self, anime: Anime):
        self.get_image_from_url(anime.poster_image_url)
        self.title.configure(text=anime.title)
        self.date.configure(text=anime.started_at.strftime("%d %B %Y"))


    def get_image_from_url(self, url):
        image_from_url = requests.get(url, stream=True).raw
        original = None
        if not self.destroyed:
            original = Image.open(image_from_url)
        if not self.destroyed:
            resized = original.resize((80, 80), Image.ANTIALIAS)
        if not self.destroyed:
            self.image = ImageTk.PhotoImage(resized)
        if not self.destroyed:
            self.image_label.configure(image=self.image)

    def search_by_name_wrapper(self, name=None):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.search_by_name(name=name))

    async def search_by_name(self, name=None):
        display_info = await self.kitsu_client.search('anime', name)
        self.set_anime_card(display_info[0])