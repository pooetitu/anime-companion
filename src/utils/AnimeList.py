from src.utils.file_utils import load_view_list_data, save_view_list_data


class AnimeList:
    def __init__(self):
        self.animes: dict = load_view_list_data()
        self.callbacks = []

    def add_anime(self, anime):
        self.animes[anime["title"]] = anime
        self.save_list()
        for callback in self.callbacks:
            callback()

    def remove_anime(self, anime_title):
        del self.animes[anime_title]
        self.save_list()
        for callback in self.callbacks:
            callback()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def save_list(self):
        save_view_list_data(self.animes)
