import tkinter
from tkinter import ttk, NW

import requests
from PIL import Image, ImageTk


class AnimeInfoCard(ttk.Frame):
    def __init__(self, anime, master=None):
        super().__init__(master)
        self.anime = anime
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        image_from_url = requests.get(self.anime.poster_image_url, stream=True).raw
        self.image = Image.open(image_from_url)
        resized = self.image.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.canvas = tkinter.Canvas(self, width=80, height=80)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.pack(side="left", anchor=NW)

        self.details = ttk.Frame(self)
        self.details.pack(side="left")
        self.anime_name = ttk.Label(self.details, wraplength=290, text=self.anime.title)
        self.anime_name.pack(anchor=NW)
        synopsis = ' '.join(self.anime.synopsis.split(' ')[:30]) + ('...' if len(self.anime.synopsis.split(' ')) > 30 else '')
        self.anime_description = ttk.Label(self.details, wraplength=290,
                                           text=synopsis)
        self.anime_description.pack(anchor=NW)
