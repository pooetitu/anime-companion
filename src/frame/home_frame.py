from tkinter import ttk

from src.cards.anime_info_card import AnimeInfoCard
from src.frame.scrollable_frame import ScrollableFrame


class HomeFrame(ScrollableFrame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.label = ttk.Label(self.scrollable_frame, text="Accueil")
        self.create_widgets()

    def create_widgets(self):
        self.label.pack()
        for i in range(0, 10):
            self.anime_card = AnimeInfoCard(self.scrollable_frame)
            self.anime_card.pack(pady=5)


    def say_hi(self):
        print("coucou c'est moi")


