from Card import Card
import random


class DeckOfCards:
    """Method of the Deck of Cards that shows
    4 suits and 13 values for each Card."""
    def __init__(self):
        self.full_deck = []
        for suit in range(1, 5):
            # self.full_deck.append({key: self.values_dict})
            for value in range(1, 14):
                card = Card(value, suit)
                self.full_deck.append(card)

    def cards_shuffle(self):
        '''Method that making shuffle for Cards'''
        random.shuffle(self.full_deck)

    def deal_one(self):
        '''Method that picks one, removes it from that deck
        and returning it.'''
        if len(self.full_deck)>0:
            return self.full_deck.pop(-1)
        else:
            return None

    def __str__(self):
        return f'{self.full_deck}'

    def __repr__(self):
        return f'{self.full_deck}'
