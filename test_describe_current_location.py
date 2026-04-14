from unittest import TestCase
from unittest.mock import patch
from game import make_board, make_character, describe_current_location

class Test(TestCase):
    @patch('builtins.print')
    def test_describe_current_location_prints_coordinates(self, mock_print):
        board = make_board(5, 5)
        character = make_character("Luka")
        describe_current_location(board, character)
        actual = any("(0, 0)" in str(call) for call in mock_print.call_args_list)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_describe_current_location_prints_description(self, mock_print):
        board = {(0, 0): "A foggy forest clearing"}
        character = make_character("Luka")
        describe_current_location(board, character)
        actual = any("A foggy forest clearing" in str(call) for call in mock_print.call_args_list)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_describe_current_location_invalid_location_prints_error(self, mock_print):
        board = make_board(5, 5)
        character = make_character("Luka")
        character["X-coordinate"] = 99
        character["Y-coordinate"] = 99
        describe_current_location(board, character)
        actual = any("Invalid location" in str(call) for call in mock_print.call_args_list)
        expected = True
        self.assertEqual(expected, actual)

    @patch('builtins.print')
    def test_describe_current_location_updated_position(self, mock_print):
        board = make_board(5, 5)
        character = make_character("Luka")
        character["X-coordinate"] = 2
        character["Y-coordinate"] = 3
        describe_current_location(board, character)
        actual = any("(2, 3)" in str(call) for call in mock_print.call_args_list)
        expected = True
        self.assertEqual(expected, actual)