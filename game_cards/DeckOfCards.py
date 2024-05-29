from Card import Card
import random


class DeckOfCards:
    """Initialize the deck of cards with 52 unique cards."""
    def __init__(self):
        self.full_deck = []
        for suit in range(1, 5):
            # self.full_deck.append({key: self.values_dict})
            for value in range(1, 14):
                card = Card(value, suit)
                self.full_deck.append(card)

    def cards_shuffle(self):
        """Method that shuffles full_deck"""
        random.shuffle(self.full_deck)

    def deal_one(self):
        """Method that picks one card and removes it from that deck."""
        if len(self.full_deck)>0:
            return self.full_deck.pop(-1)
        else:
            return None

    def __str__(self):
        """Return a string representation of the card."""
        return f'{self.full_deck}'

    def __repr__(self):
        """Return a string representation of the card."""
        return f'{self.full_deck}'
