from unittest import TestCase,mock
from Card import Card
from DeckOfCards import DeckOfCards
from Player import Player


class TestPlayer(TestCase):
    def setUp(self):
        """Set up the test case environment"""
        self.player1=Player('Tomer',10)
        self.player2=Player('Shani',26)

        print("Test started.")

    def test_init_valid_num_of_cards(self):
        """Test if Player is initialized with the correct number of cards when within valid range."""
        self.assertEqual(self.player1.num_of_cards,10)
        self.assertEqual(self.player2.num_of_cards,26)
        self.assertEqual(Player('Idan', 20).num_of_cards, 20)

    def test_init_invalid_num_of_cards_under_range(self):
        """Test if Player is initialized with 26 cards when given a below the range invalid number of cards."""
        test_player1=Player('Shuky',0)
        self.assertEqual(test_player1.num_of_cards,26)

    def test_init_invalid_num_of_cards_over_range(self):
        """Test if Player is initialized with 26 cards when given an above the range invalid number of cards."""

        test_player2 = Player('Adi', 30)
        self.assertEqual(test_player2.num_of_cards,26)

    def test_init_invalid_type_num_of_cards(self):
        """Test if initializing Player with an invalid type for num_of_cards raises a TypeError."""
        with self.assertRaises(TypeError):
            Player('Yoni',20.0)
            Player('Yoni',"20")

    def test_init_player_name_str(self):
        """Test if Player name is of type str."""
        self.assertEqual(type(self.player1.player_name),str)

    def test_init_player_name_str_special_characters(self):
        """Test if Player name with special characters is of type str."""
        test_player3 = Player('!?@Liel501.#', 26)
        self.assertEqual(type(test_player3.player_name), str)


    @mock.patch('DeckOfCards.DeckOfCards.deal_one', return_value=Card(13,3))
    def test_set_hand(self, mock_deal_one):
        """Test if set_hand deals the correct number of cards to the player."""
        card_for_mock=Card(13,3)
        deck_test=DeckOfCards()
        self.player1.set_hand(deck_test)
        self.assertEqual(len(self.player1.player_deck),10)
        self.assertTrue(self.player1.player_deck.count(card_for_mock)==10)

    def test_get_card_removed_from_player_hand(self):
        """Test if get_card removes the card from the player's hand."""
        card_test=Card(12,3)
        self.player1.player_deck=[card_test,card_test]
        self.player1.get_card()
        self.assertEqual(len(self.player1.player_deck),1)


    def test_get_card_removed_right_card(self):
        """Test if get_card returns the correct card from the player's hand."""
        card_test = Card(5, 4)
        self.player1.player_deck = [card_test, card_test]
        card_get_card = self.player1.get_card()
        self.assertEqual(card_get_card, Card(5, 4))

    def test_get_card_player_deck_empty(self):
        """Test if get_card returns None when the player's deck is empty."""
        self.assertIsNone(self.player1.get_card())

    def test_add_card_card_added(self):
        """Test if add_card adds a new card to the player's deck."""
        card_test = Card(10, 4)
        card_test2 = Card(11,3)
        self.player1.player_deck = [card_test]
        self.player1.add_card(card_test2)
        self.assertEqual(len(self.player1.player_deck), 2)
        self.assertIn(card_test, self.player1.player_deck)

    def test_add_card_existing_card(self):
        """Test if add_card does not add a card already present in the player's deck."""
        card_test=Card(9,1)
        self.player1.player_deck=[Card(9,1)]
        self.assertFalse(self.player1.add_card(card_test))


    def tearDown(self):
        """Tear down the test case environment."""
        print("Test ended.")