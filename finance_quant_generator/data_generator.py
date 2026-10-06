"""
Module: finance_quant_generator.data_generator

Main entry point for the synthetic data generator.

This module generates statistically-plausible fake market time series and risk metrics.
"""

import random
from datetime import timedelta, date

def generate_random_date(start_date):
    """
    Generate a random date within a given range.

    Args:
        start_date (date): The start of the date range.

    Returns:
        date: A random date within the range [start_date, current date].
    """
    today = date.today()
    days_diff = (today - start_date).days
    return start_date + timedelta(days=random.randint(0, days_diff))

def generate_random_price(base_price):
    """
    Generate a random price around a given base price.

    Args:
        base_price (float): The base price to vary from.

    Returns:
        float: A random price within 10% of the base price.
    """
    return base_price * (1 + random.uniform(-0.1, 0.1))

def generate_time_series(start_date, end_date):
    """
    Generate a synthetic time series between two dates.

    Args:
        start_date (date): The start of the date range.
        end_date (date): The end of the date range.

    Returns:
        list: A list of tuples containing random prices and dates.
    """
    prices = []
    current_date = generate_random_date(start_date)
    while current_date <= end_date:
        price = generate_random_price(100.0)  # arbitrary base price
        prices.append((current_date, price))
        current_date += timedelta(days=random.randint(1, 30))  # random days between 1-30
    return prices

def generate_risk_metrics(prices):
    """
    Generate synthetic risk metrics from a given time series.

    Args:
        prices (list): A list of tuples containing dates and prices.

    Returns:
        dict: A dictionary containing mean, median, max, min, and standard deviation.
    """
    values = [price[1] for price in prices]
    return {
        'mean': sum(values) / len(values),
        'median': sorted(values)[len(values) // 2],
        'max': max(values),
        'min': min(values),
        'stddev': (sum((x - mean) ** 2 for x in values) / len(values)) ** 0.5
    }

def main():
    start_date = date(2020, 1, 1)
    end_date = date.today()
    time_series = generate_time_series(start_date, end_date)
    risk_metrics = generate_risk_metrics(time_series)
    print('Time Series:')
    for date, price in time_series:
        print(f'{date}: {price}')
    print('\nRisk Metrics:')
    for metric, value in risk_metrics.items():
        print(f'{metric}: {value}')

if __name__ == '__main__':
    main()
