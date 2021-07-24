import asyncio
import threading, requests
from tkinter import ttk

from PIL import Image, ImageTk



class AnimeDetailsFrame(ttk.Frame):
    def __init__(self, kitsu_client, function_close, master=None):
        super().__init__(master)
        self.destroyed = False
        self.anime = None
        self.master = master
        self.closeButton = ttk.Button(self, text="Retour")
        self.imageLabel = ttk.Label(self)
        self.anime_name = ttk.Label(self, font="Helvetica 18 bold")
        self.anime_description = ttk.Label(self, wraplength=300)
        self.anime_description = ttk.Label(self, wraplength=300)
        self.closeButton['command'] = function_close
        self.closeButton.pack(side='bottom')

    def set_anime(self, anime):
        self.anime = anime
        self.anime_name.configure(text=anime.title)
        self.anime_description.configure(text=anime.synopsis)
        self.anime_description.configure(text=anime.synopsis)
        self.image_recuperation_thread = threading.Thread(target=self.get_image_from_url)
        self.image_recuperation_thread.start()
        self.imageLabel.pack(side="top", padx=20)
        self.anime_name.pack(side='top')
        self.anime_description.pack(side='top')

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
            self.imageLabel.configure(image=self.image)

    def destroy(self):
        self.destroyed = True
        super().destroy()
