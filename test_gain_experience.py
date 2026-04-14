from unittest import TestCase
from game import make_character, gain_experience

class Test(TestCase):
    def test_gain_experience_increases_exp_by_one(self):
        character = make_character("Luka")
        gain_experience(character)
        actual = character["EXP"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_gain_experience_accumulates(self):
        character = make_character("Luka")
        gain_experience(character)
        gain_experience(character)
        actual = character["EXP"]
        expected = 2
        self.assertEqual(expected, actual)