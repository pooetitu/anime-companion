from tkinter import ttk
import json
import threading, requests

from src.cards.anime_info_card import AnimeInfoCard
from src.cards.trend_info_card import TrendInfoCard
from src.frame.scrollable_frame import ScrollableFrame

class Trend:
    def __init__(self, image, name, description):
        self.image = image
        self.name = name
        self.description = description


class HomeFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.anime_list = []
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.label = ttk.Label(self.scrollable, text="Accueil")
        self.label.pack()
        self.create_widgets()

<<<<<<< Updated upstream
    def create_widgets(self):
        self.label.pack()
        for i in range(0, 10):
            self.anime_card = AnimeInfoCard(self.scrollable_frame)
            self.anime_card.pack(pady=50)
=======
>>>>>>> Stashed changes


    def create_widgets(self):
        self.load_trend()

    def display_trend(self, animes):
        for anime in animes:
            card = TrendInfoCard(anime, self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5, fill='both', expand=1)

    def load_trend(self):
        animes = requests.get("https://kitsu.io/api/edge/trending/anime?limit=9").json()
        #animes = json.loads(animes)
        print(animes['data'][0]['attributes']["slug"])
        for anime in animes['data']:
            print(anime)
            card = TrendInfoCard(Trend(
                anime["attributes"]["posterImage"]["original"],
                anime["attributes"]["titles"]["en"],
                anime["attributes"]["synopsis"]
            ), self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5, fill='both', expand=1)
        #print(self.anime_list[0].image)
        #self.display_trend(self.anime_list)

    def say_hi(self):
        print("coucou c'est moi")


