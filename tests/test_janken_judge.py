import unittest
from source.janken_judge import judge

class TestJudge(unittest.TestCase):
    def test_judge(self):
        patterns = [('グー', 'グー', 'draw'), ('グー', 'チョキ', 'computer_win'), ('グー', 'パー', 'player_win'), ('チョキ', 'グー', 'player_win'), ('チョキ', 'チョキ', 'draw'), ('チョキ', 'パー', 'computer_win'), ('パー', 'グー', 'computer_win'), ('パー', 'チョキ', 'player_win'), ('パー', 'パー', 'draw')]
        for computer, player, expected in patterns:
            with self.subTest(computer=computer, player=player):
                self.assertEqual(judge(computer, player), expected)