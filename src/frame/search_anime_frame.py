from tkinter import ttk, filedialog

from src.cards.anime_info_card import AnimeInfoCard
from src.frame.scrollable_frame import ScrollableFrame


class SearchAnimeFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.container = ttk.Frame(self)
        self.textField = ttk.Entry(self.container)
        self.searchButton = ttk.Button(self.container, text="Chercher")
        self.selectFileButton = ttk.Button(self, text="Chercher par image")
        self.create_widgets()
        self.anime_list = []
        self.scrollable = ScrollableFrame(self)
        self.scrollable.pack()

    def create_widgets(self):
        self.searchButton.pack()
        self.container.pack(side="top")
        self.textField.pack(in_=self.container, side="left")
        self.searchButton.pack(in_=self.container, side="left")
        self.selectFileButton["command"] = self.open_file_selection
        self.selectFileButton.pack()

    def open_file_selection(self):
        file = filedialog.askopenfile(parent=self, mode='rb', title='Choisissez une image à rechercher', filetypes=[
            ("image", ".jpeg"),
            ("image", ".png"),
            ("image", ".jpg")])
        if file:
            print(file.read())

    def display_anime_infos(self, animes):
        self.anime_list_clear()
        for anime in animes:
            card = AnimeInfoCard(self.scrollable.scrollable_frame)
            self.anime_list.append(card)
            card.pack(pady=5)

    def anime_list_clear(self):
        for card in self.anime_list:
            card.destroy()
        self.anime_list.clear()
