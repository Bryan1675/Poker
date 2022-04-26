import random
import sys
import Card


class Deck:
    SIGNS = ['h', 'c', 's', 'd']
    NUMBER_OF_VALUES_PER_SIGN = 13

    def __init__(self, seed=None):
        self.cards = []
        self.game_seed = seed
        self.generate_a_blended_deck()

    """generate a random deck of cards from the game seed"""
    def generate_a_blended_deck(self):
        for sign in self.SIGNS:
            for value in range(1, self.NUMBER_OF_VALUES_PER_SIGN + 1):
                self.cards.append(Card.Card(value, sign))

        if self.game_seed is None:
            self.game_seed = self.seed_generator()

        random.seed(self.game_seed)
        random.shuffle(self.cards)

        return self

    """generate a random seed"""
    def seed_generator(self):
        seed = random.randrange(sys.maxsize)
        self.game_seed = seed
        return seed

    """take off and return a card from the deck"""
    def pick_a_card(self):
        return self.cards.pop()
