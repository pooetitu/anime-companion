import threading
from tkinter import ttk, NW, Frame

import requests
from PIL import Image, ImageTk


class AnimeInfoCard(Frame):
    def __init__(self, anime, master=None):
        super().__init__(master, highlightbackground="grey", highlightthickness=1)
        self.anime = anime
        self.master = master
        self.pack()
        self.imageLabel = ttk.Label(self)
        self.details = ttk.Frame(self)
        self.anime_name = ttk.Label(self.details, wraplength=290, text=self.anime.title)
        self.anime_description = ttk.Label(self.details, wraplength=290)
        self.create_widgets()

    def create_widgets(self):
        image_recuperation_thread = threading.Thread(target=self.get_image_from_url)
        image_recuperation_thread.start()
        self.imageLabel.pack(side="left", anchor=NW)

        self.details.pack(side="left", anchor=NW)
        self.anime_name.pack(anchor=NW)
        synopsis = ' '.join(self.anime.synopsis.split(' ')[:30]) +\
                   ('...' if len(self.anime.synopsis.split(' ')) > 30 else '')
        self.anime_description.configure(text=synopsis)
        self.anime_description.pack(anchor=NW)

    def get_image_from_url(self):
        image_from_url = requests.get(self.anime.poster_image_url, stream=True).raw
        original = Image.open(image_from_url)
        resized = original.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.imageLabel.configure(image=self.image)
