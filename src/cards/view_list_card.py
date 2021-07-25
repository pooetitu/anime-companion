import asyncio
import threading
from tkinter import ttk

import requests
from PIL import Image, ImageTk
from kitsu.models import Anime

from src.status_enum import ViewStatus
from src.utils.AnimeList import AnimeList


class ViewListCard(ttk.Frame):
    def __init__(self, anime, master=None, kitsu=None, anime_list: AnimeList = None):
        super().__init__(master)
        self.destroyed = False
        self.kitsu_client = kitsu
        self.master = master
        self.anime_list = anime_list
        self.anime = anime
        self.display_info = None
        self.create_widgets()
        threading.Thread(target=self.search_by_name_wrapper, kwargs={'name': anime["title"]}).start()
        self.pack()

    def create_widgets(self):

        # IMAGE / TITLE / DATE IN LEFT

        self.infos = ttk.Frame(self)
        self.infos.pack(side="left")
        self.image_label = ttk.Label(self.infos)
        self.image_label.pack(side="left", padx=5)
        self.title = ttk.Label(self.infos, text=self.anime["title"])
        self.title.pack(anchor="nw")
        self.date = ttk.Label(self.infos)
        self.date.pack(anchor="nw")
        # OPITONS RIGHT
        self.delete_original = Image.open('./assets/icons/delete_icon.png')
        delete_resized = self.delete_original.resize((30, 30), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(delete_resized)
        self.delete_button = ttk.Button(self, image=self.delete_icon)
        self.delete_button.pack(side="right", padx=5)

        self.interac_frame = ttk.Frame(self)
        self.interac_frame.pack(side="right", anchor="e", padx=5)

        self.button_plus = ttk.Button(self.interac_frame, text="+1")
        self.button_plus["command"] = self.add_viewed_episode
        self.button_plus.pack()

        self.episode_count_label = ttk.Label(self.interac_frame, text="%d/? episodes" % (self.anime["viewed_episodes"]))
        self.episode_count_label.pack()

        self.button_minus = ttk.Button(self.interac_frame, text="-1")
        self.button_minus["command"] = self.remove_viewed_episode
        self.button_minus.pack()
        # MENU BUTTON

        options = [e.value for e in ViewStatus]
        # create the Menubutton
        self.menu_button = ttk.Combobox(self, values=options)
        self.menu_button.pack(side="right")
        for i, e in enumerate(ViewStatus):
            if e.value == self.anime["status"]:
                self.menu_button.current(i)
        self.menu_button.bind("<<ComboboxSelected>>", self.select_status)

    def set_anime_card(self, anime: Anime):
        self.display_info: Anime = anime
        self.title.configure(text=anime.title)
        self.date.configure(text=anime.started_at.strftime("%d %B %Y"))
        text = ("%d/%s episodes" % (self.anime["viewed_episodes"],
                                    self.display_info.episode_count if self.display_info and self.display_info.episode_count else "?"))
        self.episode_count_label.configure(text=text)
        self.get_image_from_url(anime.poster_image_url)

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

    def add_viewed_episode(self):
        if self.display_info and not self.display_info.episode_count or self.anime[
            "viewed_episodes"] < self.display_info.episode_count:
            self.anime["viewed_episodes"] += 1
            text = ("%d/%s episodes" % (self.anime["viewed_episodes"],
                                        self.display_info.episode_count if self.display_info and self.display_info.episode_count else "?"))
            self.episode_count_label.configure(text=text)
            self.anime_list.save_list()

    def remove_viewed_episode(self):
        if self.display_info and not self.display_info.episode_count and self.anime["viewed_episodes"] > 0:
            self.anime["viewed_episodes"] -= 1
            text = ("%d/%s episodes" % (self.anime["viewed_episodes"],
                                        self.display_info.episode_count if self.display_info and self.display_info.episode_count else "?"))
            self.episode_count_label.configure(text=text)
            self.anime_list.save_list()

    def select_status(self, event):
        self.anime["status"] = ViewStatus(self.menu_button.get())
        self.anime_list.save_list()
