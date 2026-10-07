import unittest
from finance_quant_generator import market_models

class TestMarketModels(unittest.TestCase):
    def test_geometric_brownian_motion(self):
        model = market_models.GeometricBrownianMotion(mu=0.05, sigma=0.2)
        prices = model.generate(n_steps=10)
        self.assertEqual(len(prices), 11)

    def test_ornstein_uhlenbeck_process(self):
        model = market_models.OrnsteinUhlenbeckProcess(theta=0.1, mu=100.0, sigma=0.5)
        prices = model.generate(n_steps=10)
        self.assertEqual(len(prices), 11)

    def test_random_walk(self):
        model = market_models.RandomWalk(step_size=10)
        prices = model.generate(n_steps=10)
        self.assertEqual(len(prices), 11)

if __name__ == '__main__':
    unittest.main()
