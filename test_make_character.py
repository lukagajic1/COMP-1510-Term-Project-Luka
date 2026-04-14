from unittest import TestCase
from game import make_character

class Test(TestCase):
    def test_make_character_x_coordinate(self):
        actual = make_character("Luka")["X-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_y_coordinate(self):
        actual = make_character("Luka")["Y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_current_hp(self):
        actual = make_character("Luka")["Current HP"]
        expected = 8
        self.assertEqual(expected, actual)

    def test_make_character_max_hp(self):
        actual = make_character("Luka")["Max HP"]
        expected = 8
        self.assertEqual(expected, actual)

    def test_make_character_luck(self):
        actual = make_character("Luka")["Luck"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_make_character_level(self):
        actual = make_character("Luka")["Level"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_make_character_exp(self):
        actual = make_character("Luka")["EXP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_make_character_name(self):
        actual = make_character("Luka")["Name"]
        expected = "Luka"
        self.assertEqual(expected, actual)

    def test_make_character_level_name(self):
        actual = make_character("Luka")["Level Name"]
        expected = "Beginner"
        self.assertEqual(expected, actual)
