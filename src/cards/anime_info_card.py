import tkinter
from tkinter import ttk, NW
from PIL import Image, ImageTk


class AnimeInfoCard(ttk.Frame):
    def __init__(self, anime, master=None):
        super().__init__(master)
        self.anime = anime
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.image = Image.open('C:\\Users\\pooetitu\\Desktop\\3ucn50Y6.jpg')
        resized = self.image.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.canvas = tkinter.Canvas(self, width=80, height=80)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.pack(side="left", anchor=NW)

        self.details = ttk.Frame(self)
        self.details.pack(side="left")
        self.anime_name = ttk.Label(self.details, wraplength=290, text=self.anime.title)
        self.anime_name.pack(anchor=NW)
        self.anime_description = ttk.Label(self.details, wraplength=290,
                                           text=self.anime.synopsis.split(' ')[:50])
        self.anime_description.pack(anchor=NW)
