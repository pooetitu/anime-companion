import tkinter as tk

import kitsu

from src.main_window import Application
from src.utils.AnimeList import AnimeList

root = tk.Tk()
root.title("Anime companion")
root.wm_minsize(600, 400)
root.wm_maxsize(600, 400)
root.geometry('600x400+0+0')
client = kitsu.Client()
anime_list = AnimeList()
app = Application(master=root, anime_list=anime_list, kitsu_client=client)
app.pack(fill='both', expand=1)
app.mainloop()
