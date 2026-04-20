"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np


def generate_data(seed):
    """Generate synthetic sensor temperature readings and timestamps.

    Parameters
    ----------
    seed : int
        Seed value for the NumPy random number generator.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of 200 synthetic temperature readings for Sensor A sampled
        from a normal distribution with mean 25°C and standard deviation 3°C.
    sensor_b : numpy.ndarray
        Array of 200 synthetic temperature readings for Sensor B sampled
        from a normal distribution with mean 27°C and standard deviation 4.5°C.
    timestamps : numpy.ndarray
        Array of 200 timestamps uniformly sampled between 0 and 10 seconds.
    """
    rng = np.random.default_rng(seed=seed)
    timestamps = rng.uniform(0, 10, 200)
    sensor_a = rng.normal(25, 3, 200)
    sensor_b = rng.normal(27, 4.5, 200)
    return sensor_a, sensor_b, timestamps
