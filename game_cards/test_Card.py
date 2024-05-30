from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card_low=Card(2,1) #[2♦️]
        self.card_big=Card(1,4) #[A♣️]
        self.card_op3=Card(5,2) #[5♠️]
        self.card_op4=Card(11,3)#[J♥️]

        print('Test Started.')



    def test_init_valid_value(self):
        self.assertEqual(self.card_low.value,2)
    def test_init_valid_suit(self):
        self.assertEqual(self.card_big.suit,4)

    def test_init_valid_value_dict(self):
        self.assertEqual(self.card_op4.values_dict[11],'J')

    def test_init_valid_suit_dict(self):
        self.assertEqual(self.card_op3.suits_dict[2],'♠️')

    def test_init_invalid_value(self):
        with self.assertRaises(TypeError):
            Card('J',4)
        with self.assertRaises(ValueError):
            Card(14,1)
        with self.assertRaises(ValueError):
            Card(0, 2)
    def test_init_invalid_suit(self):
        with self.assertRaises(TypeError):
            Card(10, '♥️')
        with self.assertRaises(ValueError):
            Card(4, 0)
        with self.assertRaises(ValueError):
            Card(4, 5)

    def test_gt_same_value(self):
        """"""
        card_5_1=Card(5,1)
        self.assertTrue(self.card_op3 > card_5_1)              # [5♠️]>[5♦️]

    def test_gt_ace_self(self):
        self.assertTrue(self.card_big>self.card_low)           # [A♣️]>[2♦️]

    def test_gt_ace_other(self):
        self.assertFalse(self.card_op4>self.card_big)          # [J♥️]>[A♣️]

    def test_gt_regular_case(self):
        self.assertTrue(self.card_op4>self.card_op3)           # [J♥️]>[5♠️]

    def test_eq_True(self):
        card_same_op3=Card(5, 2)
        self.assertTrue(self.card_op3==card_same_op3)

    def test_eq_False(self):
        self.assertFalse(self.card_op3==self.card_op4)

    def tearDown(self):
        print('Test ended.')


# self.card_low = Card(2, 1)  # [2♦️]
# self.card_big = Card(1, 4)  # [A♣️]
# self.card_op3 = Card(5, 2)  # [5♠️]
# self.card_op4 = Card(11, 3)  # [J♥️]
