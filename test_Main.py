import unittest
from Main import Main

class MainTest(unittest.TestCase):
    def test_deck_generation_from_seed(self):
        """Generate a deck with the same seed, then compare the hands with expected values"""
        #self.skipTest("Skipping test, uncomment this line when previous step is commited")

        main = Main()
        main.initialize_game(3746925965984614406)

        self.assertEqual(
            [
                str(main.player_1.hand[0]),
                str(main.i_a_1.hand[1]),
                str(main.cards_on_table[2])
            ],
            ["9h", "4c", "6d"],
            "With a determined seed, cards in hand are different than expected!"
        )

    def test_cards_count(self):
        """check the number of cards for players and table when game initializes"""
        # self.skipTest("Skipping test, uncomment this line when previous step is commited")

        main = Main()
        main.initialize_game()

        self.assertEqual(
            len(main.player_1.hand),
            2,
            "Player 1 has not 2 cards in hand!"
        )
        self.assertEqual(
            len(main.i_a_1.hand),
            2,
            "Ia 1 has not 2 cards in hand!"
        )
        self.assertEqual(
            len(main.i_a_2.hand),
            2,
            "Ia 2 has not 2 cards in hand!"
        )
        self.assertEqual(
            len(main.i_a_3.hand),
            2,
            "Ia 3 has not 2 cards in hand!"
        )
        self.assertEqual(
            len(main.cards_on_table),
            3,
            "There is not 3 cards on the table!"
        )

if __name__ == '__main__':
    unittest.main()
