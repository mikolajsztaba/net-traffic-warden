"""
CHART DOCSTRING
"""
import csv

import matplotlib.pyplot as plt
import numpy as np


# Function to initialize the plot
def init_plot():
    """
    :return:
    """
    fig, ax = plt.subplots()
    sc = ax.scatter([], [], c='b', marker='o')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return fig, ax, sc


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
def generate_and_save_random_points(num_points, sc, csv_filename):
    """
    :param num_points:
    :param sc:
    :param csv_filename:
    :return:
    """
    x = np.random.randint(0, 11, num_points)
    y = np.random.randint(0, 11, num_points)
    sc.set_offsets(np.column_stack((x, y)))

    # Append the data to the CSV file
    with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        for i in range(num_points):
            csv_writer.writerow([x[i], y[i]])


# Main function
def example_chart():
    """

    :return:
    """
    csv_filename = 'data/random_points.csv'
    init_csv(csv_filename)
    fig, ax, sc = init_plot()

    while True:
        generate_and_save_random_points(10, sc, csv_filename)
        plt.pause(1)  # Pause for a moment to allow visualization
