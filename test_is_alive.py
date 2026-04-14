from unittest import TestCase
from game import make_character, is_alive

class Test(TestCase):
    def test_is_alive_with_full_hp_is_true(self):
        character = make_character("Luka")
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_with_one_hp_is_true(self):
        character = make_character("Luka")
        character["Current HP"] = 1
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_with_zero_hp_is_false(self):
        character = make_character("Luka")
        character["Current HP"] = 0
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_with_negative_hp_is_false(self):
        character = make_character("Luka")
        character["Current HP"] = -1
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)