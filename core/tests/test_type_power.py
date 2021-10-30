import unittest
from core.player import Player
from core.dealer import Dealer


class TestTypePower(unittest.TestCase):
    
    def setUp(self):
        self.dealer = Dealer()
        self.player1 = Player("Player1")
        self.player2 = Player("Player2")


    def test_high_card_power(self):

        cards = [
            [{"name": "A", "value": 14}],
            [{"name": "5", "value": 5}],
            [{"name": "4", "value": 4}],
            [{"name": "3", "value": 3}],
            [{"name": "2", "value": 2}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "High Card")


    def test_pair_power(self):

        cards = [
            [{"name": "A", "value": 14}, {"name": "A", "value": 14}],
            [{"name": "4", "value": 4}],
            [{"name": "3", "value": 3}],
            [{"name": "2", "value": 2}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Pair")


    def test_two_pair_power(self):

        cards = [
            [{"name": "A", "value": 14}, {"name": "A", "value": 14}],
            [{"name": "4", "value": 4}, {"name": "4", "value": 4}],
            [{"name": "2", "value": 2}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Two pair")

    def test_three_of_kind_power(self):

        cards = [
            [{"name": "A", "value": 14}, {"name": "A", "value": 14}, {"name": "A", "value": 14}],
            [{"name": "4", "value": 4}],
            [{"name": "2", "value": 2}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Three of a kind")

    
    def test_straight_power(self):

        cards = [
            [{"name": "2", "value": 2}],
            [{"name": "3", "value": 3}],
            [{"name": "4", "value": 4}],
            [{"name": "5", "value": 5}],
            [{"name": "6", "value": 6}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Straight")



    def test_full_house_power(self):

        cards = [
            [{"name": "A", "value": 14}, {"name": "A", "value": 14}, {"name": "A", "value": 14}],
            [{"name": "4", "value": 4}, {"name": "2", "value": 2}]
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Full House")


    def test_four_of_kind_power(self):

        cards = [
            [{"name": "A", "value": 14}, {"name": "A", "value": 14}, {"name": "A", "value": 14}, {"name": "A", "value": 14}],
            [{"name": "K", "value": 13}],
        ]

        self.player1.hand = cards
        self.dealer.check_winner(self.player1, self.player1)

        self.assertEqual(self.player1.power['name'], "Four of kind")    


if __name__ == '__main__':
    unittest.main() 