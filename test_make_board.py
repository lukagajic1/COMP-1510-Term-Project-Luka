from unittest import TestCase
from game import make_board

class Test(TestCase):
    def test_make_board_correct_number_of_keys(self):
        actual = len(make_board(2, 2))
        expected = 4
        self.assertEqual(expected, actual)

    def test_make_board_correct_number_of_keys_rectangle(self):
        actual = len(make_board(3, 5))
        expected = 15
        self.assertEqual(expected, actual)

    def test_make_board_contains_tuple_keys(self):
        board = make_board(2, 2)
        actual = all(isinstance(k, tuple) for k in board)
        expected = True
        self.assertEqual(expected, actual)

    def test_make_board_contains_string_values(self):
        board = make_board(2, 2)
        actual = all(isinstance(v, str) for v in board.values())
        expected = True
        self.assertEqual(expected, actual)

    def test_make_board_raises_value_error_for_non_int_rows(self):
        with self.assertRaises(ValueError):
            make_board("a", 5)

    def test_make_board_raises_value_error_for_non_int_columns(self):
        with self.assertRaises(ValueError):
            make_board(5, "a")

    def test_make_board_raises_value_error_for_zero_rows(self):
        with self.assertRaises(ValueError):
            make_board(0, 5)

    def test_make_board_raises_value_error_for_zero_columns(self):
        with self.assertRaises(ValueError):
            make_board(5, 0)

    def test_make_board_raises_value_error_for_negative_rows(self):
        with self.assertRaises(ValueError):
            make_board(-1, 5)

    def test_make_board_top_left_key_exists(self):
        board = make_board(3, 3)
        actual = (0, 0) in board
        expected = True
        self.assertEqual(expected, actual)

    def test_make_board_bottom_right_key_exists(self):
        board = make_board(3, 3)
        actual = (2, 2) in board
        expected = True
        self.assertEqual(expected, actual)