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

# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a scatter plot of temperature readings versus time on the given Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Array of Sensor A temperature readings.
    sensor_b : numpy.ndarray
        Array of Sensor B temperature readings.
    timestamps : numpy.ndarray
        Array of timestamps corresponding to each reading.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the scatter plot.

    Returns
    -------
    None
        The function modifies ``ax`` in place.
    """
    ax.scatter(timestamps, sensor_a, color='tab:blue', alpha=0.7, label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='tab:orange', alpha=0.7, label='Sensor B')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Temperature (°C)')
    ax.set_title('Simulated Sensor Temperature Readings')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.4)
