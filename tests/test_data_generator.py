import unittest
from finance_quant_generator import data_generator

class TestDataGenerator(unittest.TestCase):
    def test_generate_random_date(self):
        start_date = date(2020, 1, 1)
        random_date = data_generator.generate_random_date(start_date)
        self.assertGreaterEqual(random_date, start_date)
        self.assertLessEqual(random_date, date.today())

    def test_generate_random_price(self):
        base_price = 100.0
        price = data_generator.generate_random_price(base_price)
        self.assertAlmostEqual(price, base_price * (1 + random.uniform(-0.1, 0.1)), places=2)

    def test_generate_time_series(self):
        start_date = date(2020, 1, 1)
        end_date = date.today()
        time_series = data_generator.generate_time_series(start_date, end_date)
        self.assertIsInstance(time_series, list)
        self.assertGreater(len(time_series), 0)

    def test_generate_risk_metrics(self):
        prices = [(date(2020, 1, 1), 100.0)]
        risk_metrics = data_generator.generate_risk_metrics(prices)
        self.assertIn('mean', risk_metrics)
        self.assertIn('median', risk_metrics)
        self.assertIn('max', risk_metrics)
        self.assertIn('min', risk_metrics)
        self.assertIn('stddev', risk_metrics)

if __name__ == '__main__':
    unittest.main()
