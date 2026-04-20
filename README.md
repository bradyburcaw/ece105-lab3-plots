<!-- Create a README.md with these sections:
     1. Project title and one-sentence description
     2. Installation (activate ece105 conda env, pip install numpy matplotlib)
     3. Usage (python generate_plots.py)
     4. Example output (describe the three plots briefly)
     5. AI tools used and disclosure -->

# ECE105 Lab 3: Sensor Data Plots

A Python script that generates synthetic temperature sensor data and creates publication-quality visualizations including scatter plots, histograms, and box plots.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install the required dependencies using conda or mamba:
   ```
   conda install numpy matplotlib
   ```
   or
   ```
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

## Example Output

The script generates a single PNG file named `sensor_analysis.png` containing three subplots:

1. **Scatter Plot**: Displays temperature readings from Sensor A (blue) and Sensor B (orange) over time (0-10 seconds), showing the temporal distribution of the data points.
2. **Overlaid Histogram**: Shows the frequency distribution of temperature readings for both sensors using 30 bins, with transparent overlays and vertical lines indicating each sensor's mean temperature.
3. **Side-by-Side Box Plot**: Compares the statistical distributions of Sensor A and Sensor B temperatures, including medians, quartiles, and an overall mean line across both datasets.

The figure is saved at 150 DPI with a tight bounding box for high-quality output.

## AI Tools Used and Disclosure

GitHub Copilot was used to assist with code generation, documentation, and project setup.
     