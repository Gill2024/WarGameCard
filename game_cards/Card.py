class Card:

    def __init__(self,value,suit):

        self.suit = suit
        self.suits_dict = {1: '♦', 2: '♠', 3: '♥', 4: '♣'} #1 clubs (♣),2 diamonds (♦),3 hearts(♥) 4 spades(♠)

        self.value = value
        self.values_dict = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
                            7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K'}


    def __str__(self):
        return f'[{self.values_dict[self.value]} {self.suits_dict[self.suit]}]'

    def __repr__(self):
        return f'{self.values_dict[self.value]}{self.suits_dict[self.suit]}'

    def __gt__(self, other):
        '''Method that decides who's card have grater value '''
        if self.value == other.value:
            return self.suit > other.suit
        elif self.value == 1:
            return True
        elif other.value == 1:
            return False
        else:
            return self.value > other.value


    def __eq__(self, other):
        if self.value == other.value:
            if self.suit == other.suit:
                return True
        elif self.suit == other.suit:
            if self.value == other.value:
                return True
        else:
            return False