"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


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

# Create plot_histogram(data, bins, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, bins, ax):
    """Draw overlaid histograms for Sensor A and Sensor B on the specified Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings to plot.
    sensor_b : numpy.ndarray
        Sensor B temperature readings to plot.
    bins : int
        Number of bins to use for each histogram.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the histograms.

    Returns
    -------
    None
        The function modifies ``ax`` in place.
    """
    ax.hist(sensor_a, bins=bins, alpha=0.5, color='tab:blue', label='Sensor A')
    ax.hist(sensor_b, bins=bins, alpha=0.5, color='tab:orange', label='Sensor B')
    for values, color, label in [(sensor_a, 'tab:blue', 'Sensor A mean'), (sensor_b, 'tab:orange', 'Sensor B mean')]:
        mean_value = np.mean(values)
        ax.axvline(mean_value, color=color, linestyle='--', linewidth=1.5, label=label)
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Count')
    ax.set_title('Overlaid Temperature Distribution for Sensor A and Sensor B')
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.4)

# Create plot_boxplot(data, labels, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(data, labels, ax):
    """Draw a side-by-side box plot for the given datasets on the provided Axes.

    Parameters
    ----------
    data : list of numpy.ndarray
        List of data arrays to visualize in separate box plots.
    labels : list of str
        Labels for each dataset shown on the x-axis.
    ax : matplotlib.axes.Axes
        Axes object on which to draw the box plot.

    Returns
    -------
    None
        The function modifies ``ax`` in place.
    """
    box = ax.boxplot(
        data,
        labels=labels,
        patch_artist=True,
        showmeans=True,
        boxprops=dict(facecolor='lightgray', edgecolor='black'),
        medianprops=dict(color='red'),
        whiskerprops=dict(color='black'),
        capprops=dict(color='black'),
        meanprops=dict(marker='o', markerfacecolor='black', markeredgecolor='black')
    )
    colors = ['tab:blue', 'tab:orange']
    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)

    overall_mean = np.mean(np.concatenate(data))
    ax.axhline(overall_mean, color='blue', linestyle='--', linewidth=1.5,
               label=f'Overall mean = {overall_mean:.2f} °C')
    ax.set_ylabel('Temperature (deg C)')
    ax.set_title('Sensor A vs Sensor B Temperature Distributions')
    ax.legend()
    ax.grid(True, axis='y', linestyle='--', alpha=0.4)

# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.
def main():
    """Generate sensor data, create plots, and save the figure.

    The function generates synthetic temperature readings for two sensors,
    creates a 1x3 subplot figure, draws the scatter plot, histogram, and
    box plot on separate Axes, adjusts the layout, and saves the result
    as ``sensor_analysis.png`` with 150 DPI and a tight bounding box.

    Returns
    -------
    None
        The function saves the figure to disk and does not return a value.
    """
    seed = 8265
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, bins=30, ax=axes[1])
    plot_boxplot([sensor_a, sensor_b], labels=['Sensor A', 'Sensor B'], ax=axes[2])

    fig.tight_layout()
    fig.savefig('sensor_analysis.png', dpi=150, bbox_inches='tight')


if __name__ == '__main__':
    main()
