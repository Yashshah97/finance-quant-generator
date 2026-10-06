import unittest
from finance_quant_generator import utils
import numpy as np

class TestUtils(unittest.TestCase):

    def test_check_probability(self):
        with self.assertRaises(ValueError):
            utils.check_probability(-1)
        with self.assertRaises(ValueError):
            utils.check_probability(2)
        with self.assertRaises(ValueError):
            utils.check_probability('a')
        self.assertEqual(utils.check_probability(0.5), None)

    def test_check_positive(self):
        with self.assertRaises(ValueError):
            utils.check_positive(-1)
        with self.assertRaises(ValueError):
            utils.check_positive(0)
        with self.assertRaises(ValueError):
            utils.check_positive('a')
        self.assertEqual(utils.check_positive(1), None)

    def test_check_power_of_two(self):
        self.assertTrue(utils.check_power_of_two(8))
        self.assertFalse(utils.check_power_of_two(10))

    def test_check_random_state(self):
        rs = utils.check_random_state(None)
        self.assertIsInstance(rs, np.random.RandomState)
        with self.assertRaises(ValueError):
            utils.check_random_state('a')

    def test_generate_normal(self):
        arr = utils.generate_normal(size=1000)
        self.assertEqual(arr.shape, (1000,))
        self.assertTrue(np.allclose(np.mean(arr), 0))
        self.assertTrue(np.allclose(np.std(arr), 1))

if __name__ == '__main__':
    unittest.main()
