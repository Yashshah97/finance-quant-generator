import unittest
from finance_quant_generator import config

class TestConfig(unittest.TestCase):
    def test_config_init(self):
        config_instance = config.Config()
        self.assertEqual(config_instance.seed, 42)
        self.assertEqual(config_instance.start_date, '2020-01-01')
        self.assertEqual(config_instance.end_date, '2022-12-31')
        self.assertEqual(config_instance.time_step, 'D')
        self.assertEqual(config_instance.num_steps, 1000)
        self.assertEqual(config_instance.asset_classes, ['stock', 'bond'])
        self.assertEqual(config_instance.risk_metrics, ['return', 'volatility'])

    def test_get_config(self):
        config_instance = config.get_config(seed=24, start_date='2021-01-01')
        self.assertEqual(config_instance.seed, 24)
        self.assertEqual(config_instance.start_date, '2021-01-01')

    def test_repr(self):
        config_instance = config.Config()
        self.assertEqual(str(config_instance), "Config(seed=42, start_date='2020-01-01', end_date='2022-12-31')")

if __name__ == '__main__':
    unittest.main()
