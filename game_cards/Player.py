from DeckOfCards import DeckOfCards
from Card import Card


class Player:
    def __init__(self,player_name,num_of_cards):
        """Initialize a player with a name and a number of cards.
        Parameters:
        player_name (str): The name of the player.
        num_of_cards (int): The number of cards to be dealt to the player.
                            Must be between 10 and 26 inclusive.
                            Defaults to 26 if out of range."""
        self.player_name = player_name
        self.player_deck = []

        if self.player_name=="" or self.player_name.isspace():
            raise ValueError("Player`s name is empty or contains only spaces.")

        if type(num_of_cards)!= int:
            raise TypeError("Only int type values allowed")
        if 10 <= num_of_cards <= 26:
            self.num_of_cards = num_of_cards
        else:
            self.num_of_cards = 26

    def __str__(self):
        """Return a string representation of the player's name and deck."""
        return f'{self.player_name}\n{self.player_deck}'

    def set_hand(self, deck: DeckOfCards):

        """Method that deals cards to the player based on num_of_cards from __init__."""
        for i in range(self.num_of_cards):
            card=deck.deal_one()
            self.player_deck.append(card)

    def get_card(self):
        """Method that plays (remove and return) the first card from the player's deck."""
        if len(self.player_deck)>0:
            return self.player_deck.pop(0)
        else:
            return None

    def add_card(self, card:Card):
        """Method that adds card to the end of player's deck """
        if card not in self.player_deck:
            self.player_deck.append(card)
        else:
            return False


