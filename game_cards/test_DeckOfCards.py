from unittest import TestCase
from DeckOfCards import DeckOfCards
from Card import Card



class TestDeckOfCards(TestCase):
    def setUp(self):
        """Set up the test case environment."""
        self.deck=DeckOfCards()
        print("Test started.")
    def test_init_full_deck_eq_52_cards(self):
        """Test if the deck is initialized with 52 cards."""
        self.assertEqual(len(self.deck.full_deck),52)

    def test_init_full_deck_52unique_cards(self):
        """Test if the deck contains 52 unique cards."""
        for card in self.deck.full_deck:
            self.assertEqual(self.deck.full_deck.count(card),1)

    def test_cards_shuffle_eq_52cards(self):
        """Test if the number of cards remains 52 after shuffling."""
        deck_shuffled=DeckOfCards()
        deck_shuffled.cards_shuffle()
        self.assertEqual(len(self.deck.full_deck),len(deck_shuffled.full_deck))

    def test_cards_shuffle_different_order(self):
        """Test if the order of cards changes after shuffling."""
        deck_shuffled = DeckOfCards()
        deck_shuffled.cards_shuffle()
        self.assertNotEqual(deck_shuffled.full_deck,self.deck.full_deck)
    def test_deal_one_deck_eq_51(self):
        """Test if dealing one card reduces the deck size to 51 and returns the correct card."""
        a=self.deck.deal_one()
        self.assertEqual(51,len(self.deck.full_deck))
        self.assertEqual(a,Card(13,4))
    def test_deal_one_deck_eq_0(self):
        """Test if dealing one card from an empty deck returns None."""
        self.deck.full_deck=[]
        self.assertIsNone(self.deck.deal_one())

    def tearDown(self):
        """Tear down the test case environment."""
        print("Test ended.")
