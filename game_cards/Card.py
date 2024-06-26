class Card:

    def __init__(self,value,suit):
        """Initialize a card with a value and a suit.
        Parameters:
        value (int): The value of the card (1-13, Ace-King)
        suit (int): The suit of the card (1: diamonds (♦️), 2: spades (♠️), 3: hearts(♥️), 4: clubs(♣️))."""
        if type(value) != int:
            raise TypeError("Only int type values allowed")
        elif 1>value or value>13:
            raise ValueError("Only values between 1-13 are allowed")
        elif type(suit) != int:
            raise TypeError("Only int type values allowed")
        elif 1 > suit or suit > 4:
            raise ValueError("Only values between 1-4 are allowed")
        else:
            self.suit = suit
            self.suits_dict = {1: '♦️', 2: '♠️', 3: '♥️', 4: '♣️'}
            self.value = value
            self.values_dict = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                                7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}


    def __str__(self):
        """Return a string representation of the card."""
        return f'[{self.values_dict[self.value]} {self.suits_dict[self.suit]}]'

    def __repr__(self):
        """Return a string representation of the card."""
        return f'{self.values_dict[self.value]}{self.suits_dict[self.suit]}'

    def __gt__(self, other):
        """Method that compares card to another card to determine if it is of greater value. """
        if self.value == other.value:
            return self.suit > other.suit
        elif self.value == 1:
            return True
        elif other.value == 1:
            return False
        else:
            return self.value > other.value

    def __eq__(self, other):
        """Method that compares card to another card to determine if they are equal."""
        if self.value == other.value:
            if self.suit == other.suit:
                return True
        else:
            return False
