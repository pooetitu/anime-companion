import asyncio
import threading, requests
from tkinter import ttk
from tkinter.ttk import Frame

from PIL import Image, ImageTk
from kitsu.models import Anime

from src.frame.scrollable_frame import ScrollableFrame
from src.status_enum import ViewStatus
from src.utils.file_utils import save_view_list_data


class AnimeDetailsFrame(Frame):
    def __init__(self, kitsu_client, function_close, master=None, anime_list: dict = None):
        super().__init__(master)
        self.destroyed = False
        self.anime = None
        self.anime_list = anime_list
        self.master = master
        self.anime_scrollable_frame = ScrollableFrame(self)
        self.close_button = ttk.Button(self, text="Retour")
        self.add_anime_button = ttk.Button(self)
        self.image_label = ttk.Label(self.anime_scrollable_frame.scrollable_frame)
        self.infos_frame = Frame(self.anime_scrollable_frame.scrollable_frame)
        self.date_label = ttk.Label(self.infos_frame)
        self.status_label = ttk.Label(self.infos_frame)

        self.anime_name = ttk.Label(self.anime_scrollable_frame.scrollable_frame, font="Helvetica 18 bold")
        self.anime_description = ttk.Label(self.anime_scrollable_frame.scrollable_frame, wraplength=300)
        self.anime_description = ttk.Label(self.anime_scrollable_frame.scrollable_frame, wraplength=300)
        self.close_button['command'] = function_close
        self.add_anime_button.pack(side="top")
        self.close_button.pack(side='bottom', pady=10)
        self.anime_scrollable_frame.pack(side="top", fill="both", expand=True)
        self.image_label.pack(side="top", padx=20)
        self.anime_name.pack(side='top')
        self.infos_frame.pack(side="top")
        self.status_label.pack(side='left')
        self.date_label.pack(side='left')
        self.anime_description.pack(side='top')

    def set_anime(self, anime: Anime):
        self.anime = anime
        self.image_recuperation_thread = threading.Thread(target=self.get_image_from_url)
        self.image_recuperation_thread.start()
        self.anime_name.configure(text=anime.title)
        self.status_label.configure(text="Status : " + anime.status)
        self.date_label.configure(text="Date de début: " + anime.started_at.strftime("%d %B %Y"))
        self.anime_description.configure(text=anime.synopsis)
        if self.anime.title in self.anime_list:
            self.add_anime_button.configure(text="Retirer de ma liste")
            self.add_anime_button['command'] = self.remove_anime_to_list
        else:
            self.add_anime_button.configure(text="Ajouter à ma liste")
            self.add_anime_button['command'] = self.add_anime_to_list


    def get_image_from_url(self):
        image_from_url = requests.get(self.anime.poster_image_url, stream=True).raw
        original = None
        if not self.destroyed:
            original = Image.open(image_from_url)
        if not self.destroyed:
            resized = original.resize((100, 120), Image.ANTIALIAS)
        if not self.destroyed:
            self.image = ImageTk.PhotoImage(resized)
        if not self.destroyed:
            self.image_label.configure(image=self.image)

    def add_anime_to_list(self):
        self.anime_list[self.anime.title] = {"title": self.anime.title, "date": self.anime.started_at,
                                             "viewed_episodes": 0, "status": ViewStatus.NOT_STARTED,
                                             "favorite": False}
        self.add_anime_button.configure(text="Retirer de ma liste")
        self.add_anime_button['command'] = self.remove_anime_to_list

    def remove_anime_to_list(self):
        del self.anime_list[self.anime.title]
        self.add_anime_button.configure(text="Ajouter à ma liste")
        self.add_anime_button['command'] = self.add_anime_to_list

    def destroy(self):
        self.destroyed = True
        super().destroy()
