from unittest import TestCase
from game import make_character, get_exp_threshold

class Test(TestCase):
    def test_get_exp_threshold_level_one(self):
        character = make_character("Luka")
        actual = get_exp_threshold(character)
        expected = 3
        self.assertEqual(expected, actual)

    def test_get_exp_threshold_level_two(self):
        character = make_character("Luka")
        character["Level"] = 2
        actual = get_exp_threshold(character)
        expected = 6
        self.assertEqual(expected, actual)

    def test_get_exp_threshold_level_three_is_none(self):
        character = make_character("Luka")
        character["Level"] = 3
        actual = get_exp_threshold(character)
        expected = None
        self.assertEqual(expected, actual)