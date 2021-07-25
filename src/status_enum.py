from enum import Enum


class ViewStatus(str, Enum):
    NOT_STARTED = "Pas commencer"
    ONGOING = "En cours"
    FINISHED = "Fini"
    ABANDONED = "Abandonne"
