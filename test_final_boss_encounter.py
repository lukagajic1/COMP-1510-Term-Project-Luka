from unittest import TestCase
from unittest.mock import patch
from game import make_character, final_boss_encounter

class Test(TestCase):
    @patch('builtins.input', return_value="2")
    def test_final_boss_correct_answer_returns_true(self, _):
        character = make_character("Luka")
        actual = final_boss_encounter(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "2"])
    def test_final_boss_wrong_then_correct_returns_true(self, _):
        character = make_character("Luka")
        actual = final_boss_encounter(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "2"])
    def test_final_boss_wrong_answer_reduces_hp_by_two(self, _):
        character = make_character("Luka")
        final_boss_encounter(character)
        actual = character["Current HP"]
        expected = 6
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "3", "4"])
    def test_final_boss_dies_from_wrong_answers_returns_false(self, _):
        character = make_character("Luka")
        character["Current HP"] = 4
        actual = final_boss_encounter(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    def test_final_boss_correct_answer_does_not_reduce_hp(self, _):
        character = make_character("Luka")
        final_boss_encounter(character)
        actual = character["Current HP"]
        expected = 8
        self.assertEqual(expected, actual)