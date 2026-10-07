import unittest
from finance_quant_generator import risk_metrics

class TestRiskMetrics(unittest.TestCase):

    def test_var(self):
        population = [1, 2, 3, 4, 5]
        confidence_level = 0.95
        self.assertGreaterEqual(risk_metrics.var(population, confidence_level), min(population))

    def test_es(self):
        population = [1, 2, 3, 4, 5]
        confidence_level = 0.95
        self.assertGreaterEqual(risk_metrics.es(population, confidence_level), risk_metrics.var(population, confidence_level))

    def test_cvar(self):
        population = [1, 2, 3, 4, 5]
        confidence_level = 0.95
        self.assertEqual(risk_metrics.cvar(population, confidence_level), risk_metrics.es(population, confidence_level))

    def test_quantile(self):
        population = [1, 2, 3, 4, 5]
        prob = 0.75
        self.assertGreaterEqual(risk_metrics.quantile(population, prob), sorted(population)[int(len(population) * prob)])

if __name__ == '__main__':
    unittest.main()
