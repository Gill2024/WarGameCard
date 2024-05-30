from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card



class TestDeckOfCards(TestCase):
    def setUp(self):
        self.deck=DeckOfCards()
        print("Test started.")
    def test_init_full_deck_eq_52_cards(self):
        self.assertEqual(len(self.deck.full_deck),52)

    def test_init_full_deck_52unique_cards(self):
        for card in self.deck.full_deck:
            self.assertEqual(self.deck.full_deck.count(card),1)

    def test_cards_shuffle_eq_52cards(self):
        deck_shuffled=DeckOfCards()
        deck_shuffled.cards_shuffle()
        self.assertEqual(len(self.deck.full_deck),len(deck_shuffled.full_deck))

    def test_cards_shuffle_different_order(self):
        deck_shuffled = DeckOfCards()
        deck_shuffled.cards_shuffle()
        self.assertNotEqual(deck_shuffled.full_deck,self.deck.full_deck)
    def test_deal_one_deck_eq_51(self):
        a=self.deck.deal_one()
        self.assertEqual(51,len(self.deck.full_deck))
        self.assertEqual(a,Card(13,4))
    def test_deal_one_deck_eq_0(self):
        self.deck.full_deck=[]
        self.assertIsNone(self.deck.deal_one())

    def tearDown(self):
        print("Test ended.")
