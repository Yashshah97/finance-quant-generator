"""Smoke tests for tests_test_data_generator."""
import unittest

from finance_quant_generator import tests_test_data_generator


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(tests_test_data_generator, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(tests_test_data_generator) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
