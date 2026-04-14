from unittest import TestCase
from game import make_character, has_leveled_up

class Test(TestCase):
    def test_has_leveled_up_below_threshold_is_false(self):
        character = make_character("Luka")
        character["EXP"] = 2
        actual = has_leveled_up(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_has_leveled_up_at_threshold_is_true(self):
        character = make_character("Luka")
        character["EXP"] = 3
        actual = has_leveled_up(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_has_leveled_up_above_threshold_is_true(self):
        character = make_character("Luka")
        character["EXP"] = 5
        actual = has_leveled_up(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_has_leveled_up_level_two_below_threshold_is_false(self):
        character = make_character("Luka")
        character["Level"] = 2
        character["EXP"] = 5
        actual = has_leveled_up(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_has_leveled_up_level_two_at_threshold_is_true(self):
        character = make_character("Luka")
        character["Level"] = 2
        character["EXP"] = 6
        actual = has_leveled_up(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_has_leveled_up_max_level_is_false(self):
        character = make_character("Luka")
        character["Level"] = 3
        character["EXP"] = 99
        actual = has_leveled_up(character)
        expected = False
        self.assertEqual(expected, actual)