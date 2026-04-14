from unittest import TestCase
from game import check_for_foes
from unittest.mock import patch

class Test(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_check_for_foes_returns_true_on_one(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_check_for_foes_returns_false_on_two(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3])
    def test_check_for_foes_returns_false_on_three(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[4])
    def test_check_for_foes_returns_false_on_four(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)