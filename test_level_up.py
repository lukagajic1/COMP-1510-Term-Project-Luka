from unittest import TestCase
from game import make_character, level_up

class Test(TestCase):
    def test_level_up_increments_level(self):
        character = make_character("Luka")
        level_up(character)
        actual = character["Level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_level_up_increases_max_hp(self):
        character = make_character("Luka")
        level_up(character)
        actual = character["Max HP"]
        expected = 10
        self.assertEqual(expected, actual)

    def test_level_up_restores_current_hp_to_max(self):
        character = make_character("Luka")
        character["Current HP"] = 3
        level_up(character)
        actual = character["Current HP"]
        expected = character["Max HP"]
        self.assertEqual(expected, actual)

    def test_level_up_increases_luck(self):
        character = make_character("Luka")
        level_up(character)
        actual = character["Luck"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_level_up_updates_level_name(self):
        character = make_character("Luka")
        level_up(character)
        actual = character["Level Name"]
        expected = "Intermediate"
        self.assertEqual(expected, actual)