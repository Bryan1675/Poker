from abc import ABC, abstractmethod


class AbstractPlayer(ABC):
    def __init__(self, name):
        self.name = name
        self.hand = []

    @abstractmethod
    def show_hand(self):
        pass
