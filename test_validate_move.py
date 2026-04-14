from unittest import TestCase
from game import validate_move, make_board, make_character

class Test(TestCase):
    def test_validate_move_north_from_origin_is_false(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        actual = validate_move(board, character, "North")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_west_from_origin_is_false(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        actual = validate_move(board, character, "West")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_east_from_origin_is_true(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        actual = validate_move(board, character, "East")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_south_from_origin_is_true(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        actual = validate_move(board, character, "South")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_south_from_bottom_edge_is_false(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        character["X-coordinate"] = 4
        actual = validate_move(board, character, "South")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_east_from_right_edge_is_false(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        character["Y-coordinate"] = 4
        actual = validate_move(board, character, "East")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_invalid_direction_is_false(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        actual = validate_move(board, character, "Up")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_does_not_mutate_character(self):
        board = make_board(5, 5)
        character = make_character("Luka")
        validate_move(board, character, "East")
        actual = character["Y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)