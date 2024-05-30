from unittest import TestCase
from Player import Player
from CardGame import CardGame


class TestCardGame(TestCase):

    def setUp(self):
        self.game1=CardGame('Itay','Noa',26)
        print("Test started.")

    def test_init_player1_name_Player(self):
        self.assertEqual(type(self.game1.player1), type(Player('Itay',26)))

    def test_init_player2_type_Player(self):
        self.assertEqual(type(self.game1.player2), type(Player('Noa',26)))

    def test_init_num_of_cards_type_int(self):
        self.assertEqual(type(self.game1.num_of_cards_per_player),int)

    def test_init_valid_num_of_cards_both_players_same_amount(self):
        self.assertEqual(len(self.game1.player1.player_deck),26)
        self.assertEqual(len(self.game1.player2.player_deck),26)
    def test_init_invalid_num_of_cards_under_range_both_players_fix_26(self):
        self.game1.cards_in_games=0
        self.assertEqual(len(self.game1.player1.player_deck), 26)
        self.assertEqual(len(self.game1.player2.player_deck), 26)

    def test_init_invalid_num_of_cards_over_range_both_players_fix_26(self):
        self.game1.cards_in_games = 30
        self.assertEqual(len(self.game1.player1.player_deck), 26)
        self.assertEqual(len(self.game1.player2.player_deck), 26)

    def test_init_invalid_type_num_of_cards(self):
        with self.assertRaises(TypeError):
            CardGame('Michal','Alon', 'Ten')

    def test_init_same_num_of_cards_to_both_players(self):
        self.assertTrue(self.game1.player1.num_of_cards==self.game1.player2.num_of_cards)

    def test_init_new_game_after_shuffle_cards_in_deeck(self):
        test_game=CardGame('Ido','Neta',10)
        self.assertEqual(32,len(test_game.deck.full_deck))

    def test_new_game_invalid_call(self):
        test_game=CardGame('Itamar','Noga',10)
        self.assertIs(None,self.game1.new_game())

    def test_get_winner_player1(self):
        self.game1.player2.player_deck.pop()
        self.assertTrue(len(self.game1.player1.player_deck)>len(self.game1.player2.player_deck))
        self.assertIs(self.game1.get_winner(),self.game1.player1)
    def test_get_winner_player2(self):
        self.game1.player1.player_deck.pop()
        self.assertTrue(len(self.game1.player2.player_deck)>len(self.game1.player1.player_deck))
        self.assertIs(self.game1.get_winner(),self.game1.player2)

    def test_get_winner_draw(self):
        self.assertTrue(len(self.game1.player2.player_deck) == len(self.game1.player1.player_deck))
        self.assertIsNone(self.game1.get_winner())

    def tearDown(self):
        print("Test ended.")