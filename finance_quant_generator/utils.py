"""
Utility functions for finance quant synthetic data generator.
"""

def check_probability(p):
    """
    Check if a value is within the valid probability range [0, 1].
    
    Args:
        p (float): The value to be checked.
    
    Raises:
        ValueError: If the value is not in the valid range.
    """
    if not isinstance(p, float) or p < 0 or p > 1:
        raise ValueError("Probability must be a float within [0, 1]")

def check_positive(n):
    """
    Check if a value is positive.
    
    Args:
        n (float): The value to be checked.
    
    Raises:
        ValueError: If the value is not positive.
    """
    if not isinstance(n, (int, float)) or n <= 0:
        raise ValueError("Value must be a positive number")

def check_power_of_two(n):
    """
    Check if a value is a power of two.
    
    Args:
        n (int): The value to be checked.
    
    Returns:
        bool: True if the value is a power of two, False otherwise.
    """
    return (n & (n - 1)) == 0

def check_random_state(seed):
    """
    Turn seed into a np.random.RandomState instance.
    
    Args:
        seed (int or None): Seed for random number generation.
    
    Returns:
        np.random.RandomState: A RandomState instance.
    """
    if seed is None:
        seed = 0
    if not isinstance(seed, int):
        raise ValueError("Seed must be an integer")
    return np.random.RandomState(seed)

import numpy as np

def generate_normal(size, mean=0.0, std_dev=1.0):
    """
    Generate a normal distribution.
    
    Args:
        size (int): The number of samples to generate.
        mean (float, optional): Mean of the distribution. Defaults to 0.0.
        std_dev (float, optional): Standard deviation of the distribution. Defaults to 1.0.
    
    Returns:
        np.ndarray: A numpy array containing the generated normal distribution.
    """
    return np.random.normal(loc=mean, scale=std_dev, size=size)
