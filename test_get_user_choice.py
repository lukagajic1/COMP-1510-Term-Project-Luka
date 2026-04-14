from unittest import TestCase
from unittest.mock import patch
from game import get_user_choice

class Test(TestCase):
    @patch('builtins.input', return_value="1")
    def test_get_user_choice_one_returns_north(self, _):
        actual = get_user_choice()
        expected = "North"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    def test_get_user_choice_two_returns_south(self, _):
        actual = get_user_choice()
        expected = "South"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    def test_get_user_choice_three_returns_west(self, _):
        actual = get_user_choice()
        expected = "West"
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="4")
    def test_get_user_choice_four_returns_east(self, _):
        actual = get_user_choice()
        expected = "East"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["9", "1"])
    def test_get_user_choice_invalid_integer_reprompts(self, _):
        actual = get_user_choice()
        expected = "North"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "2"])
    def test_get_user_choice_non_integer_reprompts(self, _):
        actual = get_user_choice()
        expected = "South"
        self.assertEqual(expected, actual)
