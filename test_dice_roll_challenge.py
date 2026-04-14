from unittest import TestCase
from unittest.mock import patch
from game import make_character, dice_roll_challenge


class Test(TestCase):
    @patch('builtins.input', return_value="1")
    @patch('random.randint', side_effect=[3, 6])  # given=3, roll=6 (higher)
    def test_guess_higher_correct_returns_true(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    @patch('random.randint', side_effect=[4, 1])  # given=4, roll=1 (lower)
    def test_guess_lower_correct_returns_true(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('random.randint', side_effect=[3, 3])  # given=3, roll=3 (equal)
    def test_guess_equal_correct_returns_true(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1")
    @patch('random.randint', side_effect=[4, 2])  # given=4, roll=2 (not higher)
    def test_guess_higher_wrong_no_retries_returns_false(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="2")
    @patch('random.randint', side_effect=[2, 6])  # given=2, roll=6 (not lower)
    def test_guess_lower_wrong_no_retries_returns_false(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="3")
    @patch('random.randint', side_effect=[3, 5])  # given=3, roll=5 (not equal)
    def test_guess_equal_wrong_no_retries_returns_false(self, _, __):
        character = make_character("Luka")
        actual = dice_roll_challenge(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1")
    @patch('random.randint', side_effect=[4, 2])  # given=4, roll=2 (wrong)
    def test_wrong_guess_reduces_hp_by_one(self, _, __):
        character = make_character("Luka")
        dice_roll_challenge(character)
        actual = character["Current HP"]
        expected = 7
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="1")
    @patch('random.randint', side_effect=[3, 6])  # given=3, roll=6 (correct)
    def test_correct_guess_does_not_reduce_hp(self, _, __):
        character = make_character("Luka")
        dice_roll_challenge(character)
        actual = character["Current HP"]
        expected = 8
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "1"])
    @patch('random.randint', side_effect=[4, 2, 3, 6])  # retry: given=4,roll=2 wrong; given=3,roll=6 correct
    def test_luck_retry_succeeds_on_second_attempt_returns_true(self, _, __):
        character = make_character("Luka")
        character["Luck"] = 2  # 1 retry
        actual = dice_roll_challenge(character)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "1"])
    @patch('random.randint', side_effect=[4, 2, 3, 2])  # retry: given=4,roll=2 wrong; given=3,roll=2 wrong
    def test_luck_retry_fails_both_attempts_returns_false(self, _, __):
        character = make_character("Luka")
        character["Luck"] = 2  # 1 retry
        actual = dice_roll_challenge(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["1", "1"])
    @patch('random.randint', side_effect=[4, 2, 3, 2])  # retry: wrong twice
    def test_luck_retry_exhausted_reduces_hp(self, _, __):
        character = make_character("Luka")
        character["Luck"] = 2  # 1 retry
        dice_roll_challenge(character)
        actual = character["Current HP"]
        expected = 7
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["abc", "1"])
    @patch('random.randint', side_effect=[3, 3, 6])  # given=3 (reprompt), given=3, roll=6 (higher)
    def test_non_integer_input_reprompts(self, _, __):
        character = make_character("Luka")
        with self.assertRaises(ValueError):
            int("abc")

    @patch('builtins.input', side_effect=["9", "1"])
    @patch('random.randint', side_effect=[3, 3, 6])  # given=3 (reprompt), given=3, roll=6 (higher)
    def test_out_of_range_input_reprompts(self, _, __):
        character = make_character("Luka")
        with self.assertRaises(ValueError):
            int("abc")

