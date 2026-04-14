from unittest import TestCase
from unittest.mock import patch
from game import choose_challenge

class Test(TestCase):
    @patch('random.choice', return_value="enemy")
    def test_choose_challenge_returns_enemy(self, _):
        actual = choose_challenge()
        expected = "enemy"
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="potion")
    def test_choose_challenge_returns_potion(self, _):
        actual = choose_challenge()
        expected = "potion"
        self.assertEqual(expected, actual)
