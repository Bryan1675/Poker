import os
import tkinter

from Deck import Deck
from Player import Player
from Ia import Ia
from tkinter import *
from tkinter.ttk import *

class Main:

    """ Variables for display cards """
    GAP_BETWEEN_TWO_CARDS= 91
    CARDS_PER_TABLE = 3
    CARDS_PER_PLAYER = 2

    def __init__(self):
        self.player_1 = Player("WelcomePlayerOne")
        self.i_a_1 = Ia('Stu Ungar')
        self.i_a_2 = Ia('Chip Reese')
        self.i_a_3 = Ia('Phil Hellmuth')
        self.players = [
            self.player_1,
            self.i_a_1,
            self.i_a_2,
            self.i_a_3
        ]
        self.cards_on_table = []


    """blend the cards, serve each player and the table."""
    def initialize_game(self, seed=None):
        deck = Deck(seed)
        while len(self.cards_on_table) < self.CARDS_PER_TABLE :
            self.cards_on_table.append(deck.pick_a_card())
        for player in self.players:
            while len(player.hand) < self.CARDS_PER_PLAYER:
                player.hand.append(deck.pick_a_card())
        return deck.game_seed

    """launch a new game from the given seed."""
    def new_game(self, root, seed=None):
        for player in self.players:
            player.hand = []
        self.cards_on_table = []
        self.initialize_game(seed)

        # LEFT TO DO : game is reinitilized here, but we do not have any refresh in the windows yet.
        # what about refactoring the game display in a function ?


    def refresh(self):
        root = Tk
        root.mainloop()


if __name__ == '__main__':
    main = Main()
    print("Game seed : " + str(main.initialize_game()))
    deck = Deck()

    root = Tk()
    root.title('Poker')

    """ Screen size """
    root.geometry("1200x600")

    """ Button style """
    style = Style()

    style.configure('TButton', font=
    ('calibri', 10), foreground='blue',
                    borderwidth='4')

    """ Background color """
    root.configure(background='green')

    """ Load a new game """
    reloadGame = Button(root, text="New game", command=main.new_game(root, deck.game_seed)).pack(padx=5, pady=5, side=TOP, anchor=NW)

    """ Show actual seed """
    labelActualSeed = Label(root, text="Actual seed:").place(x=930, y=10)
    showActuelSeed = Label(root, text=deck.game_seed).place(x=930, y=35)

    """ Seed input with default seed """
    labelSearchSeed = Label(root, text="Change seed:").place(x=1075, y=10)
    inputSeed = Entry(root)
    inputSeed.insert(END, deck.game_seed)
    inputSeed.pack(side=TOP, anchor=NE)

    # TO DO : Create method to find the game of the seed
    buttonSearchSeed = Button(root, text="Go to this seed", command=main.refresh).pack(anchor=NE)

    # TO DO : Improve the display code of the cards because it is too long and too repetitive
    """ Cards display for player_1"""
    cards_player_1 = []
    for card in main.player_1.hand:
        photo = PhotoImage(file="gif/cards/" + str(card) + ".gif")
        cards_player_1.append(photo)

    label_cards_player_1 = ['first_card_player_1', 'second_card_player_1']
    x = 519
    for i in range(Main.CARDS_PER_PLAYER):
        label_cards_player_1[i] = Label(root, image=cards_player_1[i])
        label_cards_player_1[i].place(x=x, y=494)
        x += Main.GAP_BETWEEN_TWO_CARDS

    label_player_1 = Label(root, text="Player 1").place(x=580, y=470)

    """ Cards display for i_a_1"""
    cards_i_a_1 = []
    for card in main.i_a_1.hand:
        photo = PhotoImage(file="gif/cards/" + str(card) + ".gif")
        cards_i_a_1.append(photo)

    label_cards_i_a_1 = ['first_card_i_a_1', 'second_card_i_a_1']
    x = 10
    for i in range(Main.CARDS_PER_PLAYER):
        label_cards_i_a_1[i] = Label(root, image=cards_i_a_1[i])
        label_cards_i_a_1[i].place(x=x, y=252)
        x += Main.GAP_BETWEEN_TWO_CARDS

    label_i_a_1 = Label(root, text= "IA 1").place(x=195, y=297)

    """ Cards display for i_a_2"""
    cards_i_a_2 = []
    for card in main.i_a_2.hand:
        photo = PhotoImage(file="gif/cards/" + str(card) + ".gif")
        cards_i_a_2.append(photo)

    label_cards_i_a_2 = ['first_card_i_a_2', 'second_card_i_a_2']
    x =519
    for i in range(Main.CARDS_PER_PLAYER):
        label_cards_i_a_2[i] = Label(root, image=cards_i_a_2[i])
        label_cards_i_a_2[i].place(x=x, y=10)
        x += Main.GAP_BETWEEN_TWO_CARDS

    label_i_a_2 = Label(root, text="IA 2").place(x=985, y=297)

    """ Cards display for i_a_3"""
    cards_i_a_3 = []
    for card in main.i_a_3.hand:
        photo = PhotoImage(file="gif/cards/" + str(card) + ".gif")
        cards_i_a_3.append(photo)

    label_cards_i_a_3 = ['first_card_i_a_3', 'second_card_i_a_3']
    x = 1028
    for i in range(Main.CARDS_PER_PLAYER):
        label_cards_i_a_3[i] = Label(root, image=cards_i_a_3[i])
        label_cards_i_a_3[i].place(x=x, y=252)
        x += Main.GAP_BETWEEN_TWO_CARDS

    label_i_a_3 = Label(root, text="IA 3").place(x=590, y=120)

    """ Cards display for table"""
    cards_table = []
    for card in main.cards_on_table:
        photo = PhotoImage(file="gif/cards/" + str(card) + ".gif")
        cards_table.append(photo)

    label_table = ['first_card_table', 'second_card_table', 'third_card_table']
    x = 474
    for i in range(Main.CARDS_PER_TABLE):
        label_table[i] = Label(root, image=cards_table[i])
        label_table[i].place(x=x, y=252)
        x += Main.GAP_BETWEEN_TWO_CARDS

    root.mainloop()