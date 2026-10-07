"""
Tests for the synthetic data generator.
"""

import unittest
from datetime import date, timedelta
from decimal import Decimal, ROUND_HALF_UP
from random import randint, uniform, choice

class TestDataGenerator(unittest.TestCase):

    def test_generate_date(self):
        start_date = date(2020, 1, 1)
        end_date = date(2022, 12, 31)
        generated_dates = [date for date in self.generate_dates(start_date, end_date)]
        self.assertEqual(len(generated_dates), (end_date - start_date).days + 1)

    def test_generate_random_number(self):
        num = self.generate_random_number()
        self.assertIsInstance(num, Decimal)
        self.assertGreaterEqual(num, 0)
        self.assertLessEqual(num, 1000000)

    def test_generate_random_choice(self):
        choices = ['A', 'B', 'C']
        choice = self.generate_random_choice(choices)
        self.assertIn(choice, choices)

    def generate_dates(self, start_date, end_date):
        current_date = start_date
        while current_date <= end_date:
            yield current_date
            current_date += timedelta(days=1)

    def generate_random_number(self):
        return Decimal(uniform(0, 1000000)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    def generate_random_choice(self, choices):
        return choice(choices)


if __name__ == '__main__':
    unittest.main()
