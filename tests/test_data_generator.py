"""Smoke tests for data_generator."""
import unittest

from finance_quant_generator import data_generator


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(data_generator, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(data_generator) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
