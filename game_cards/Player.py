
class Player:
    def __init__(self,player_name,num_of_cards):
        self.player_name = player_name
        if num_of_cards>26 or num_of_cards<10:
            self.num_of_cards=26
        self.player_deck=[]

    def set_hand(self):
        '''Method that gets deck of cards and deals it
        to the player based of num_of_cards from __init__ '''

