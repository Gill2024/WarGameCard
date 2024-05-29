from DeckOfCards import DeckOfCards
from Card import Card


class Player:
    def __init__(self,player_name,num_of_cards):
        self.player_name = player_name
        if 10 <= num_of_cards <= 26:
            self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 26
        self.player_deck = []

    def __str__(self):
        return self.player_name

    def set_hand(self, deck: DeckOfCards):
        """Deal cards to the player based on num_of_cards from __init__"""
        for i in range(self.num_of_cards):
            card=deck.deal_one()
            self.player_deck.append(card)

    def get_card(self):
        if len(self.player_deck)>0:
            return self.player_deck.pop()
        else:
            return None

    def add_card(self, card:Card):
        if card not in self.player_deck:
            self.player_deck.append(card)
        else:
            return False


