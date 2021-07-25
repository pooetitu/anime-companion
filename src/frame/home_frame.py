from tkinter import ttk

import requests
from kitsu.models import Anime

from src.cards.anime_info_card import AnimeInfoCard
from src.frame.scrollable_frame import ScrollableFrame


class HomeFrame(ttk.Frame):
    def __init__(self, function_display_anime_details, master=None):
        super().__init__(master)
        self.master = master
        self.function_display_anime_details = function_display_anime_details
        self.pack()
        self.anime_list = []
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.load_trend()

    def load_trend(self):
        animes = requests.get("https://kitsu.io/api/edge/trending/anime?limit=9").json()
        for data in animes['data']:
            card = AnimeInfoCard(Anime("anime", data), self.function_display_anime_details,
                                 master=self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5, fill='both', expand=1)
