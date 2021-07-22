import asyncio
import threading, requests
from tkinter import ttk, filedialog


class AnimeDetailsFrame(ttk.Frame):
    def __init__(self, kitsu_client, function_close, master=None):
        super().__init__(master)
        self.master = master
        self.closeButton = ttk.Button(self, text="Retour")
        self.closeButton['command'] = function_close
        self.closeButton.pack(side='bottom')

