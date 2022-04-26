from AbstractPlayer import AbstractPlayer


class Player(AbstractPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.hand = []

    def show_hand(self):
        for card in self.hand:
            card.show()
