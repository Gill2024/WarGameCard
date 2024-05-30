from unittest import TestCase
from Player import Player
from CardGame import CardGame


class TestCardGame(TestCase):

    def setUp(self):
        """Set up the test case environment."""
        self.game1=CardGame('Itay','Noa',26)
        print("Test started.")

    def test_init_player1_name_Player(self):
        """Test if player1 is of type Player."""
        self.assertEqual(type(self.game1.player1), type(Player('Itay',26)))

    def test_init_player2_type_Player(self):
        """Test if player2 is of type Player."""
        self.assertEqual(type(self.game1.player2), type(Player('Noa',26)))

    def test_init_num_of_cards_type_int(self):
        """Test if num_of_cards_per_player is of type int."""
        self.assertEqual(type(self.game1.num_of_cards_per_player),int)

    def test_init_valid_num_of_cards_both_players_same_amount(self):
        """Test if both players have the same valid number of cards."""
        self.assertEqual(len(self.game1.player1.player_deck),26)
        self.assertEqual(len(self.game1.player2.player_deck),26)
    def test_init_invalid_num_of_cards_under_range_both_players_fix_26(self):
        """Test if both players have 26 cards when initialized below the range of number of cards."""
        self.game1.cards_in_games=0
        self.assertEqual(len(self.game1.player1.player_deck), 26)
        self.assertEqual(len(self.game1.player2.player_deck), 26)

    def test_init_invalid_num_of_cards_over_range_both_players_fix_26(self):
        """Test if both players have 26 cards when initialized above the range of number of cards."""
        self.game1.cards_in_games = 30
        self.assertEqual(len(self.game1.player1.player_deck), 26)
        self.assertEqual(len(self.game1.player2.player_deck), 26)

    def test_init_invalid_type_num_of_cards(self):
        """Test if an invalid type for num_of_cards_per_player raises a TypeError."""
        with self.assertRaises(TypeError):
            CardGame('Michal','Alon', 'Ten')

    def test_init_same_num_of_cards_to_both_players(self):
        """Test if both players have the same number of cards."""
        self.assertTrue(self.game1.player1.num_of_cards==self.game1.player2.num_of_cards)

    def test_init_new_game_after_shuffle_cards_in_deck(self):
        """Test if the deck has the correct number of remaining cards after dealing."""
        test_game=CardGame('Ido','Neta',10)
        self.assertEqual(32,len(test_game.deck.full_deck))

    def test_new_game_invalid_call(self):
        """Test if calling new_game after the game has started does nothing. New cards are not delt to players."""
        test_game=CardGame('Itamar','Noga',10)
        player_deck_pre_new_game=test_game.player1.player_deck
        test_game.new_game()
        self.assertEqual(test_game.player1.player_deck,player_deck_pre_new_game)

    def test_get_winner_player1(self):
        """Test if player1 is the winner when they have more cards."""
        self.game1.player2.player_deck.pop()
        self.assertTrue(len(self.game1.player1.player_deck)>len(self.game1.player2.player_deck))
        self.assertIs(self.game1.get_winner(),self.game1.player1)
    def test_get_winner_player2(self):
        """Test if player2 is the winner when they have more cards."""
        self.game1.player1.player_deck.pop()
        self.assertTrue(len(self.game1.player2.player_deck)>len(self.game1.player1.player_deck))
        self.assertIs(self.game1.get_winner(),self.game1.player2)

    def test_get_winner_draw(self):
        """Test if there is no winner when both players have the same number of cards."""
        self.assertTrue(len(self.game1.player2.player_deck) == len(self.game1.player1.player_deck))
        self.assertIsNone(self.game1.get_winner())

    def tearDown(self):
        """Tear down the test case environment."""
        print("Test ended.")