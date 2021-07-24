from src.cards.view_list_card import ViewListCard
from tkinter import ttk
from PIL import Image, ImageTk
from src.frame.scrollable_frame import ScrollableFrame
from src.utils.file_utils import save_view_list_data


class ViewListFrame(ttk.Frame):
    def __init__(self, master=None, anime_list: dict = None):
        super().__init__(master)
        self.master = master
        self.anime_list = anime_list
        self.pack()
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.create_widgets()

    def create_widgets(self):
        print()
        for anime in self.anime_list.values():
            # print(anime)
            self.anime_card = ViewListCard(anime, self.scrollable.scrollable_frame)
            self.anime_card.delete_button["command"] = lambda: self.delete_clicked(self.anime_card)
            self.anime_card.pack(pady=50)

    def delete_clicked(self, anime_card):
        del self.anime_list[anime_card.anime["name"]]
        save_view_list_data(self.anime_list)
        anime_card.destroy()
