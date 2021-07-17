import tkinter as tk
from tkinter import ttk, NW
import requests
from PIL import Image, ImageTk


class ViewListCard(ttk.Frame):
    def __init__(self, anime, master=None):
        super().__init__(master)
        self.anime = anime
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.card = ttk.Frame(self)
        self.card.pack(ipadx=10, ipady=10, fill='x')

        # IMAGE / TITLE / DATE IN LEFT
        self.mha_image = tk.PhotoImage(file='./assets/images/MHA.png')
        self.mha_image = self.mha_image.zoom(2)
        self.mha_image = self.mha_image.subsample(7)
        ttk.Label(self, image=self.mha_image).pack(in_=self.card, side="left")
        ttk.Label(self, text="My Hero Academia").pack(in_=self.card, side="left")
        ttk.Label(self, text="(2017)").pack(in_=self.card, side="left")

        # OPITONS RIGHT
        self.delete_original = Image.open('./assets/icons/delete_icon.png')
        delete_resized = self.delete_original.resize((30, 30), Image.ANTIALIAS)
        self.delete_icon = ImageTk.PhotoImage(delete_resized)
        ttk.Button(self, image=self.delete_icon, command=self.delete_clicked).pack(in_=self.card, side="right", padx=5)

        self.setting_original = Image.open('./assets/icons/setting_icon.png')
        setting_resized = self.setting_original.resize((30, 30), Image.ANTIALIAS)
        self.setting_icon = ImageTk.PhotoImage(setting_resized)
        ttk.Button(self, image=self.setting_icon, command=self.delete_clicked).pack(in_=self.card, side="right", padx=5)

        self.fav_original = Image.open('./assets/icons/fav_icon.png')
        fav_resized = self.fav_original.resize((30, 30), Image.ANTIALIAS)
        self.fav_icon = ImageTk.PhotoImage(fav_resized)
        ttk.Button(self, image=self.fav_icon, command=self.delete_clicked).pack(in_=self.card, side="right", padx=5)

        # STAR LABEL
        self.star_original = Image.open('./assets/icons/star_icon.png')
        star_resized = self.star_original.resize((20, 20), Image.ANTIALIAS)
        self.star_icon = ImageTk.PhotoImage(star_resized)
        ttk.Label(self, image=self.star_icon).pack(in_=self.card, side="right")

        ttk.Label(self, text="5").pack(in_=self.card, side="right")

        # MENU BUTTON

        options = ('En cours', 'Je sais pas', 'Mehdi la merde')
        # create the Menubutton
        menu_button = ttk.Menubutton(self, text='Select an option')

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
        exit(1)