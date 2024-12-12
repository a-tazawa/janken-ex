import unittest
from source.player import player_pon
from unittest.mock import patch, MagicMock

class TestPlayer(unittest.TestCase):
    @patch('builtins.input', return_value='1')
    def test_pon1(self, mock_input):
        self.assertEqual(player_pon(), 'グー')
    @patch('builtins.input', return_value='2')
    def test_pon2(self, mock_input):
        self.assertEqual(player_pon(), 'チョキ')
    @patch('builtins.input', return_value='3')
    def test_pon3(self, mock_input):
        self.assertEqual(player_pon(), 'パー')
    @patch('builtins.input')
    def test_pon0(self, mock_input):
        mock_input.side_effect = ['0','4']
        self.assertNotEqual(player_pon, 'グー'or'チョキ'or'パー')