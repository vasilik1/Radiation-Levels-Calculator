import math
import numpy as np

# Data organisation.
rd_data = {
    'Downtown': [25, 18, 22, 21, 26],
    'City_Center': [22, 19, 20, 31, 28],
    'Industrial_Zone': [35, 32, 30, 37, 40],
    'Residential_DC': [15, 12, 18, 20, 14],
    'Rural_Outskirts': [9, 13, 16, 14, 7],
}

# Average Calculation.
def calculate_average(rd_data):
    return sum(rd_data) / len(rd_data)

# Standard Deviation.
def clc_std_deviation(rd_data):
    average = calculate_average(rd_data)
    variance = sum((x - average) ** 2 for x in rd_data) / len(rd_data)
    std_deviation = math.sqrt(variance)
    return std_deviation

# Range Calculation.
def clc_range(rd_data):
    return max(rd_data) - min(rd_data)

# Correlation Calculation.
def calculate_correlation(levels1, levels2):
    return np.corrcoef(levels1, levels2)[0, 1]

# New Data input.
def new_rd_data():
    location = input("Enter location (type 'stop' to exit the program): ")

    # Check if the user wants to exit.
    if location.lower() == 'stop':
        return None

    if location in rd_data:
        print(f"Levels for {location} already entered. Copying existing data.")
        rd_levels = rd_data[location].copy()
    else:
        # Enter radiation.
        rd_levels = [float(x) for x in input("Enter radiation levels: ").split(',')]
        rd_data[location] = rd_levels

    return location, rd_levels

# Loop for new data input.
while True:
    new_location, levels = new_rd_data()
    if new_location is None:
        break

    # Calculation and print of statistical insights for each location.
    avg = calculate_average(levels)
    print(f"Average radiation in {new_location}: {avg}")

    # Add a line break
    print()

    # Standard deviation
    std_dev = clc_std_deviation(levels)
    print(f"Standard deviation in {new_location}: {std_dev}")

    # Add a line break
    print()

    # Range, provides an idea of how spread out the values are in the dataset.
    data_range = clc_range(levels)

    print(f"\nLocation: {new_location}")
    print(f" Average radiation: {avg}")
    print(f" Standard deviation: {std_dev}")
    print(f" Range of radiation levels: {data_range}")

    # Calculate and print correlation with other locations.
    for location2, levels2 in rd_data.items():
        if new_location != location2:  # Skip self-comparisons to avoid redundant calculations and printing the same location.
            correlation = calculate_correlation(levels, levels2)
            print(f"Correlation between {new_location} and {location2}: {correlation}")

    # Add a line break
    print()
