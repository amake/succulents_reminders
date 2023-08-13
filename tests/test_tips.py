import unittest
import succs


class TestTips(unittest.TestCase):
    def test_tip(self):
        dates = set((tip.month, tip.day) for tip in succs.tips)
        self.assertEqual(len(dates), len(succs.tips))
