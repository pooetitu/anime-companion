import tkinter as tk
from tkinter import ttk, NW
import json
from PIL import Image, ImageTk

class ViewListCard(ttk.Frame):
    def __init__(self, anime, index, master=None):
        super().__init__(master)
        self.master = master
        self.index = index
        self.anime = anime
        self.pack()
        self.card = ttk.Frame(self)
        self.create_widgets()

    def create_widgets(self):
        self.card.pack(ipadx=10, ipady=10, fill='x')

        # IMAGE / TITLE / DATE IN LEFT
        self.poster_original = Image.open(self.anime["image"])
        poster_image = self.poster_original.resize((120, 150), Image.ANTIALIAS)
        self.poster_image = ImageTk.PhotoImage(poster_image)
        ttk.Label(self, image=self.poster_image).pack(in_=self.card, side="left", padx=5)


        ttk.Label(self, text=self.anime["name"]).pack(in_=self.card, side="left")
        ttk.Label(self, text=self.anime["date"]).pack(in_=self.card, side="left")

        # OPITONS RIGHT
        self.delete_original = Image.open('./assets/icons/delete_icon.png')
        delete_resized = self.delete_original.resize((30, 30), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(delete_resized)
        ttk.Button(self, image=self.delete_icon, command=self.delete_clicked).pack(in_=self.card, side="right", padx=5)

        # STAR LABEL
        self.star_original = Image.open('./assets/icons/star_icon.png')
        star_resized = self.star_original.resize((20, 20), Image.ANTIALIAS)
        self.star_icon = ImageTk.PhotoImage(star_resized)
        ttk.Label(self, image=self.star_icon).pack(in_=self.card, side="right")

        ttk.Label(self, text=self.anime["rating"]).pack(in_=self.card, side="right")

        # MENU BUTTON

        options = ('En cours', 'Je sais pas', 'Mehdi la merde')
        # create the Menubutton
        menu_button = ttk.Menubutton(self, text=self.anime["status"])

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for option in options:
            menu.add_radiobutton(
                label=option,
                value=option)

        menu_button["menu"] = menu

        menu_button.pack(in_=self.card, side="right")

        # Separator
        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x')

    def delete_clicked(self):
        file = open("./assets/anime.json", "r")
        data = json.load(file)
        del data['animes'][self.index]
        file = open("./assets/anime.json", "w")
        json.dump(data, file)
        file.close()
        self.destroy()