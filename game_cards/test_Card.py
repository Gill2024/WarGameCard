from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        """Set up the test case environment"""
        self.card_low=Card(2,1) #[2♦️]
        self.card_big=Card(1,4) #[A♣️]
        self.card_op3=Card(5,2) #[5♠️]
        self.card_op4=Card(11,3)#[J♥️]

        print('Test Started.')

    def test_init_valid_value(self):
        """Test the initialization of a card with a valid value."""
        self.assertEqual(self.card_low.value,2)
    def test_init_valid_suit(self):
        """Test the initialization of a card with a valid suit."""
        self.assertEqual(self.card_big.suit,4)

    def test_init_valid_value_dict(self):
        """Test the initialization of the value dictionary."""
        self.assertEqual(self.card_op4.values_dict[11],'J')


    def test_init_valid_suit_dict(self):
        """Test the initialization of the suit dictionary."""
        self.assertEqual(self.card_op3.suits_dict[2],'♠️')

    def test_init_invalid_value(self):
        """Test the initialization of a card with an invalid value."""
        with self.assertRaises(TypeError):
            Card('J',4)
        with self.assertRaises(ValueError):
            Card(14,1)
        with self.assertRaises(ValueError):
            Card(0, 2)
    def test_init_invalid_suit(self):
        """Test the initialization of a card with an invalid suit."""
        with self.assertRaises(TypeError):
            Card(10, '♥️')
        with self.assertRaises(ValueError):
            Card(4, 0)
        with self.assertRaises(ValueError):
            Card(4, 5)

    def test_gt_same_value(self):
        """Test the greater than comparison for cards with the same value but different suits."""
        card_5_1=Card(5,1)
        self.assertTrue(self.card_op3 > card_5_1)              # [5♠️]>[5♦️]

    def test_gt_ace_self(self):
        """Test the greater than comparison when the first card is an Ace."""
        self.assertTrue(self.card_big>self.card_low)           # [A♣️]>[2♦️]

    def test_gt_ace_other(self):
        """Test the greater than comparison when the second card is an Ace."""
        self.assertFalse(self.card_op4>self.card_big)          # [J♥️]>[A♣️]

    def test_gt_regular_case(self):
        """ Test the greater than comparison for regular cards."""
        self.assertTrue(self.card_op4>self.card_op3)           # [J♥️]>[5♠️]

    def test_eq_True(self):
        """Test the equality comparison for cards that are the same."""
        card_same_op3=Card(5, 2)
        self.assertTrue(self.card_op3==card_same_op3)          #[5♠️]==[5♠️]

    def test_eq_False(self):
        """Test the equality comparison for cards that are different."""
        self.assertFalse(self.card_op3==self.card_op4)          #[5♠️]==[J♥️]

    def tearDown(self):
        """Tear down the test case environment."""
        print('Test ended.')
