from unittest import TestCase
from unittest.mock import patch
from game import make_character, guessing_game

class Test(TestCase):
    @patch('builtins.input', return_value="3")
    @patch('random.randint', return_value=3)
    def test_guessing_game_correct_guess_returns_true(self, _, __):
        character = make_character("Luka")
        actual = guessing_game(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1")
    @patch('random.randint', return_value=5)
    def test_guessing_game_too_low_returns_false(self, _, __):
        character = make_character("Luka")
        actual = guessing_game(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1")
    @patch('random.randint', return_value=5)
    def test_guessing_game_wrong_guess_reduces_hp(self, _, __):
        character = make_character("Luka")
        guessing_game(character)
        actual = character["Current HP"]
        expected = 7
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="5")
    @patch('random.randint', return_value=1)
    def test_guessing_game_too_high_returns_false(self, _, __):
        character = make_character("Luka")
        actual = guessing_game(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('random.randint', return_value=3)
    def test_guessing_game_correct_guess_does_not_reduce_hp(self, _, __):
        character = make_character("Luka")
        guessing_game(character)
        actual = character["Current HP"]
        expected = 8
        self.assertEqual(expected, actual)