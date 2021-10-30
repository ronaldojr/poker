from .config import CARDS_TYPES

class Deck:

    def __init__(self, name, wilds=0):
        self.name = name
        self.wilds = wilds
        self.cards = []

    def __repr__(self):
        return f"{self.name} Deck: {self.cards}"

    def start_new_deck(self):

        for card in CARDS_TYPES:
            self.cards.append(card)

        self.cards = self.cards * 4

        for wild in range(0, self.wilds):
            self.cards.append({"name": "*", "value": 0})

    

    

