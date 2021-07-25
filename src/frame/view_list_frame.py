from tkinter import ttk

from src.cards.view_list_card import ViewListCard
from src.frame.scrollable_frame import ScrollableFrame
from src.utils.AnimeList import AnimeList


class ViewListFrame(ttk.Frame):
    def __init__(self, master=None, kitsu_client=None, anime_list: AnimeList = None):
        super().__init__(master)
        self.master = master
        self.kitsu_client = kitsu_client
        self.anime_list = anime_list
        anime_list.add_callback(self.refresh)
        self.pack()
        self.anime_card = {}
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.create_widgets()

    def create_widgets(self):
        self.refresh()

    def delete_clicked(self, anime_title):
        self.anime_list.remove_anime(anime_title)
        self.anime_card[anime_title].destroy()

    def refresh(self):
        for card in self.anime_card.values():
            card.destroy()
        for anime in self.anime_list.animes.values():
            anime_card = ViewListCard(anime, self.scrollable.scrollable_frame, self.kitsu_client, self.anime_list)
            anime_card.delete_button["command"] = lambda title=anime["title"]: self.delete_clicked(title)
            anime_card.pack(pady=10, anchor="nw", fill='both', expand=1)
            self.anime_card[anime["title"]] = anime_card
