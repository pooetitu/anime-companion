import tkinter as tk

import kitsu

from src.main_window import Application

def load_view_list_data():
    print()
    return 1


def save_view_list_data(anime_list):
    print()

root = tk.Tk()
root.title("Anime companion")
root.wm_minsize(600, 400)
root.wm_maxsize(600, 400)
root.geometry('600x400+0+0')
client = kitsu.Client()
anime_list = load_view_list_data()
app = Application(master=root, anime_list=anime_list, kitsu_client=client)
app.pack(fill='both', expand=1)
app.mainloop()

