"""
Finance Quant Synthetic Data Generator configuration module.

This module defines default configurations and parameters for the data generator.
These can be overridden by passing keyword arguments when creating a generator instance.
"""

class Config:
    """
    Default configuration settings for the synthetic data generator.
    """

    def __init__(self):
        self.seed = 42
        """Random seed for reproducibility."""
        
        self.start_date = '2020-01-01'
        """Starting date for the generated time series (inclusive)."""
        
        self.end_date = '2022-12-31'
        """Ending date for the generated time series (exclusive)."""
        
        self.time_step = 'D'
        """Time step granularity (e.g., D, W, M, Q, Y)."""
        
        self.num_steps = 1000
        """Number of time steps to generate."""
        
        self.asset_classes = ['stock', 'bond']
        """List of asset classes to simulate."""
        
        self.risk_metrics = ['return', 'volatility']
        """List of risk metrics to calculate."""

    def __repr__(self):
        return f"Config(seed={self.seed}, start_date='{self.start_date}', end_date='{self.end_date}')"


def get_config(**kwargs):
    """
    Returns a Config instance with overridden settings.

    Args:
        **kwargs: Keyword arguments overriding default configuration settings.
    """
    config = Config()
    for key, value in kwargs.items():
        setattr(config, key, value)
    return config
