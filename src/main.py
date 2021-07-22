import tkinter as tk

import kitsu

from src.main_window import Application

root = tk.Tk()
root.title("Anime companion")
root.wm_minsize(600, 400)
root.geometry('600x400+0+0')
client = kitsu.Client()
app = Application(master=root, kitsu_client=client)
app.pack(fill='both', expand=1)
app.mainloop()
