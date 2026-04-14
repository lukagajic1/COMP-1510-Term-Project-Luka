from unittest import TestCase
from game import make_character, move_character

class Test(TestCase):
    def test_move_character_north_decrements_x(self):
        character = make_character("Luka")
        character["X-coordinate"] = 1
        move_character(character, "North")
        actual = character["X-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_move_character_south_increments_x(self):
        character = make_character("Luka")
        move_character(character, "South")
        actual = character["X-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_move_character_east_increments_y(self):
        character = make_character("Luka")
        move_character(character, "East")
        actual = character["Y-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_move_character_west_decrements_y(self):
        character = make_character("Luka")
        character["Y-coordinate"] = 1
        move_character(character, "West")
        actual = character["Y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_move_character_invalid_direction_raises_value_error(self):
        character = make_character("Luka")
        with self.assertRaises(ValueError):
            move_character(character, "Up")