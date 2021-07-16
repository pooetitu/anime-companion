import tkinter
from tkinter import ttk, NW
from PIL import Image, ImageTk


class HomeFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.frame1 = ttk.Frame(self)
        self.create_widgets()

    def create_widgets(self):
        self.frame1 = ttk.Frame(self)
        self.image = Image.open('image/user_icon.png')
        resized = self.image.resize((80, 80), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.label = ttk.Label(self)
        self.label["text"] = "cooucou"
        self.label.place(x=90, y=40)
        self.canvas = tkinter.Canvas(self, width=80, height=80)
        self.canvas.create_image(0, 0, anchor=NW, image=self.image)
        self.canvas.place(x=0, y=0)


    def say_hi(self):
        print("coucou c'est moi")


