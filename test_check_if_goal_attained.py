from unittest import TestCase
from game import make_character, check_if_goal_attained

class Test(TestCase):
    def test_check_if_goal_attained_at_origin_is_false(self):
        character = make_character("Luka")
        actual = check_if_goal_attained(5, 5, character)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_at_bottom_right_is_true(self):
        character = make_character("Luka")
        character["X-coordinate"] = 4
        character["Y-coordinate"] = 4
        actual = check_if_goal_attained(5, 5, character)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_only_x_matches_is_false(self):
        character = make_character("Luka")
        character["X-coordinate"] = 4
        actual = check_if_goal_attained(5, 5, character)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_only_y_matches_is_false(self):
        character = make_character("Luka")
        character["Y-coordinate"] = 4
        actual = check_if_goal_attained(5, 5, character)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_one_by_one_board(self):
        character = make_character("Luka")
        actual = check_if_goal_attained(1, 1, character)
        expected = True
        self.assertEqual(expected, actual)