from src.cards.view_list_card import ViewListCard
from tkinter import ttk
from PIL import Image, ImageTk
from src.frame.scrollable_frame import ScrollableFrame


class ViewListFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack(fill='both', expand=1)
        self.create_widgets()


    def create_widgets(self):
        print()
        for i in range(0, 10):
            self.anime_card = ViewListCard(self.scrollable.scrollable_frame)
            self.anime_card.pack(pady=50)
