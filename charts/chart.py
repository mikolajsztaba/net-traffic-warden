import matplotlib.pyplot as plt
import numpy as np
import time


def example_chart():
    # Initialize an empty scatter plot
    fig, ax = plt.subplots()
    sc = ax.scatter([], [], c='b', marker='o')

    # Set the axis limits
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)


    # Function to update the scatter plot with random points
    def update_plot(num_points=10):
        x = np.random.rand(num_points) * 10
        y = np.random.rand(num_points) * 10
        sc.set_offsets(np.column_stack((x, y)))
        plt.pause(1)  # Pause for a moment to allow visualization


    # Update the plot continuously
    while True:
        update_plot()
