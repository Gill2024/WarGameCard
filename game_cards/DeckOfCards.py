# import game_cards
# from Card import Card
# class DeckOfCards:
#     def __init__(self):
#         self.full_deck = []
        # for i in


#     def __str__(self):
#         return f"{self.full_deck}"
#
# newdeck=DeckOfCards()
# print(newdeck)


from Card import Card
import random
class DeckOfCards:
    """Method of the Deck of Cards that shows 4 suits and 13 values for each Card."""
    def __init__(self):
        self.full_deck = []
        for suit in range(1, 5):
            # self.full_deck.append({key: self.values_dict})
            for value in range(1, 14):
                card = Card(value, suit)
                self.full_deck.append(card)
        # self.cards_shuffle()

    # def __str__(self):
    #     self.cards_shuffle()

    def cards_shuffle(self):
        '''Method that making shuffle for Cards'''
        random.shuffle(self.full_deck)

    def deal_one(self):
        '''Method that picks one, removes it from that deck and returning it.'''
        return f'{self.full_deck.pop(-1)}'


if __name__== '__main__':
    """This print shows the full deck of cards in order."""
    deck = DeckOfCards()
    print(deck.full_deck)
    """This print shows the full deck of cards in shuffle."""
    deck.cards_shuffle()
    print(deck.full_deck)
    print(deck.deal_one())




