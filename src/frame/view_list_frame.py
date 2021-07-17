from src.cards.view_list_card import ViewListCard
from tkinter import ttk
from PIL import Image, ImageTk


class ViewListFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        print()
        for i in range(0, 10):
            self.anime_card = ViewListCard(self)
            self.anime_card.pack(pady=50)
