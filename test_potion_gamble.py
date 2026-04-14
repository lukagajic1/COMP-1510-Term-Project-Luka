from unittest import TestCase
from unittest.mock import patch
from game import make_character, potion_gamble

class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_potion_gamble_heals_and_returns_true(self, _):
        character = make_character("Luka")
        character["Current HP"] = 5
        actual = potion_gamble(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_potion_gamble_does_not_exceed_max_hp(self, _):
        character = make_character("Luka")
        potion_gamble(character)
        actual = character["Current HP"]
        expected = 8
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_potion_gamble_poisons_and_returns_false(self, _):
        character = make_character("Luka")
        actual = potion_gamble(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_potion_gamble_reduces_hp_by_one(self, _):
        character = make_character("Luka")
        potion_gamble(character)
        actual = character["Current HP"]
        expected = 7
        self.assertEqual(expected, actual)