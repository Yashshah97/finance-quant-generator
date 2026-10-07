import unittest
from finance_quant_generator import tests_test_data_generator

class TestDataGeneratorTests(unittest.TestCase):

    def test_generate_dates(self):
        start_date = date(2020, 1, 1)
        end_date = date(2022, 12, 31)
        generator = tests_test_data_generator.TestDataGenerator()
        generated_dates = list(generator.generate_dates(start_date, end_date))
        self.assertEqual(len(generated_dates), (end_date - start_date).days + 1)

    def test_generate_random_number(self):
        generator = tests_test_data_generator.TestDataGenerator()
        num = generator.generate_random_number()
        self.assertIsInstance(num, float)
        self.assertGreaterEqual(num, 0)
        self.assertLessEqual(num, 1000000)

    def test_generate_random_choice(self):
        choices = ['A', 'B', 'C']
        generator = tests_test_data_generator.TestDataGenerator()
        choice = generator.generate_random_choice(choices)
        self.assertIn(choice, choices)

if __name__ == '__main__':
    unittest.main()
