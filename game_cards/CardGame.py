from DeckOfCards import DeckOfCards
from Card import Card
from Player import Player


class CardGame:
    def __init__(self, name_player1, name_player2, num_of_cards_per_player):
        """Initialize the card game with two players, number of cards to each player and a deck of cards."""
        if type(num_of_cards_per_player) != int:
            raise TypeError("Only int type values allowed")
        if 10 <= num_of_cards_per_player <= 26:
            self.num_of_cards_per_player = num_of_cards_per_player
        else:
            self.num_of_cards_per_player = 26
        self.player1 = Player(name_player1,num_of_cards_per_player)
        self.player2 = Player(name_player2,num_of_cards_per_player)
        self.deck = DeckOfCards()
        self.new_game()

        self.cards_in_games = self.player1.num_of_cards+self.player2.num_of_cards

    def __str__(self):
        """Return a string representation of the game state."""
        return (f'Player 1: {self.player1} \n'
                f'Player 2: {self.player2} ')

    def __repr__(self):
        """Return a string representation of the game state."""
        return (f'Player 1: {self.player1} {self.player1.player_deck}\n'
                f'Player 2: {self.player2} {self.player2.player_deck}')

    def new_game(self):
        '''Method that starts a new game by shuffling the deck and dealing it to both players.
        The method can only be callable, before the game starts, only from __init__ '''
        if len(self.deck.full_deck) == 52:
            self.deck.cards_shuffle()
            self.player1.set_hand(self.deck)
            self.player2.set_hand(self.deck)
        else:
            print('Error, game already started')

    def get_winner(self):
        """Method that determine the winner of the game based on the number of cards each player has."""

        if len(self.player1.player_deck)>len(self.player2.player_deck):
            return self.player1
        elif len(self.player1.player_deck)<len(self.player2.player_deck):
            return self.player2
        else:
            return None

