import unittest
from sea_level_predictor import draw_plot

class TestSeaLevelPredictor(unittest.TestCase):
    def test_draw_plot(self):
        fig = draw_plot()
        self.assertIsNotNone(fig)
        self.assertEqual(fig.__class__.__name__, 'Figure')

if __name__ == '__main__':
    unittest.main()
