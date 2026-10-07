"""
Statistical models for generating market time series data.

This module provides a set of statistical models that can be used to generate
market time series data. These models are designed to mimic the behavior of real
world financial markets, and can be used to test trading strategies or other
financial systems.
"""

import random

class GeometricBrownianMotion:
    """
    A simple implementation of geometric brownian motion.

    This model generates a time series that follows a geometric brownian motion,
    where the logarithm of the price is normally distributed. The parameters are:

    * `mu`: the drift term
    * `sigma`: the volatility

    :param mu: the drift term
    :type mu: float
    :param sigma: the volatility
    :type sigma: float
    """
    def __init__(self, mu, sigma):
        self.mu = mu
        self.sigma = sigma

    def generate(self, n_steps, initial_price=100.0):
        """
        Generate a time series of prices.

        :param n_steps: the number of steps to generate
        :type n_steps: int
        :param initial_price: the initial price (default 100.0)
        :type initial_price: float
        :return: a list of prices
        :rtype: list[float]
        """
        prices = [initial_price]
        for _ in range(n_steps):
            prices.append(prices[-1] * random.exp((self.mu - self.sigma**2 / 2) + self.sigma * random.gauss(0, 1)))
        return prices

class OrnsteinUhlenbeckProcess:
    """
    A simple implementation of an Ornstein-Uhlenbeck process.

    This model generates a time series that follows an Ornstein-Uhlenbeck process,
    where the drift term is proportional to the difference between the current value
    and a long-term mean. The parameters are:

    * `theta`: the rate at which the process returns to its mean
    * `mu`: the long-term mean
    * `sigma`: the volatility

    :param theta: the rate at which the process returns to its mean
    :type theta: float
    :param mu: the long-term mean
    :type mu: float
    :param sigma: the volatility
    :type sigma: float
    """
    def __init__(self, theta, mu, sigma):
        self.theta = theta
        self.mu = mu
        self.sigma = sigma

    def generate(self, n_steps, initial_price=100.0):
        """
        Generate a time series of prices.

        :param n_steps: the number of steps to generate
        :type n_steps: int
        :param initial_price: the initial price (default 100.0)
        :type initial_price: float
        :return: a list of prices
        :rtype: list[float]
        """
        prices = [initial_price]
        for _ in range(n_steps):
            prices.append(prices[-1] + self.theta * (self.mu - prices[-1]) + self.sigma * random.gauss(0, 1))
        return prices

class RandomWalk:
    """
    A simple implementation of a random walk.

    This model generates a time series that follows a random walk, where each step
    is either up or down by a fixed amount. The parameters are:

    * `step_size`: the size of each step
    """
    def __init__(self, step_size):
        self.step_size = step_size

    def generate(self, n_steps, initial_price=100.0):
        """
        Generate a time series of prices.

        :param n_steps: the number of steps to generate
        :type n_steps: int
        :param initial_price: the initial price (default 100.0)
        :type initial_price: float
        :return: a list of prices
        :rtype: list[float]
        """
        prices = [initial_price]
        for _ in range(n_steps):
            prices.append(prices[-1] + random.choice([-self.step_size, self.step_size]))
        return prices
