"""
CHART DOCSTRING
"""
import csv

import matplotlib.pyplot as plt
import numpy as np
import logging

logger = logging.getLogger(__name__)


# Function to initialize the plot
def init_plot():
    """
    :return:
    """
    fig, axis = plt.subplots()
    scatter_plot = axis.scatter([], [], c='b', marker='o')
    axis.set_xlim(0, 10)
    axis.set_ylim(0, 10)
    return fig, axis, scatter_plot


# Function to initialize the CSV file
def init_csv(filename):
    """
    :param filename:
    :return:
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['x', 'y'])  # Write header row


# Function to generate and save random points
def generate_and_save_random_points(num_points, scatter_plot, csv_filename):
    """
    :param num_points:
    :param sc:
    :param csv_filename:
    :return:
    """
    x_value = np.random.randint(0, 11, num_points)
    y_value = np.random.randint(0, 11, num_points)
    scatter_plot.set_offsets(np.column_stack((x_value, y_value)))

    # Append the data to the CSV file
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for i in range(num_points):
            csv_writer.writerow([x_value[i], y_value[i]])


# Main function
def example_chart():
    """

    :return:
    """
    csv_filename = 'app/data/random_points.csv'
    init_csv(csv_filename)
    fig, axis, scatter_plot = init_plot()

    print(fig, axis)

    while True:
        generate_and_save_random_points(10, scatter_plot, csv_filename)
        plt.pause(1)  # Pause for a moment to allow visualization
