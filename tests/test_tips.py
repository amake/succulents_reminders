import unittest
import succs


class TestTips(unittest.TestCase):
    def test_tips_on_distinct_dates(self):
        dates = set((tip.month, tip.day) for tip in succs.tips)
        self.assertEqual(len(dates), len(succs.tips))

    def test_get_images(self):
        for tip in succs.tips:
            images = succs.get_images(tip, 4)
            self.assertEqual(len(images), 4)
