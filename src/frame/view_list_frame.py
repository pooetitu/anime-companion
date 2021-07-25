import copy

from src.cards.view_list_card import ViewListCard
from tkinter import ttk
from PIL import Image, ImageTk
from src.frame.scrollable_frame import ScrollableFrame
from src.utils.file_utils import save_view_list_data


class ViewListFrame(ttk.Frame):
    def __init__(self, master=None, kitsu_client=None, anime_list: dict = None):
        super().__init__(master)
        self.master = master
        self.kitsu_client = kitsu_client
        self.anime_list = anime_list
        self.pack()
        self.anime_card = {}
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.create_widgets()

    def create_widgets(self):
        print()
        for anime in self.anime_list.values():
            # print(anime)
            anime_card = ViewListCard(anime, self.scrollable.scrollable_frame, self.kitsu_client)
            anime_card.delete_button["command"] = lambda: self.delete_clicked(copy.deepcopy(anime["title"]))
            # print(anime["title"])

            anime_card.pack(pady=10, anchor="nw", fill='both', expand=1)
            self.anime_card[anime["title"]] = anime_card

    def delete_clicked(self, anime_title):
        print(anime_title)
        del self.anime_list[anime_title]
        save_view_list_data(self.anime_list)
        self.anime_card[anime_title].destroy()
