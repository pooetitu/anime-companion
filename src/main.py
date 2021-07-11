import tkinter as tk

from src.main_window import Application

root = tk.Tk()
root.title("Anime companion")
root.wm_minsize(600, 400)
root.geometry('600x400+0+0')
app = Application(master=root)
app.pack(fill='both', expand=1)
app.mainloop()