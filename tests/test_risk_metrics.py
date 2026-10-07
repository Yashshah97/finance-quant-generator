"""Smoke tests for risk_metrics."""
import unittest

from finance_quant_generator import risk_metrics


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(risk_metrics, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(risk_metrics) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
