"""
DATA DOCSTRING
"""
import csv
import logging

logger = logging.getLogger(__name__)


def calculate_average():
    """
    :return:
    """
    # Initialize variables to store the sum and count for each column
    sum_column1 = 0
    sum_column2 = 0
    count = 0

    # Open and read the CSV file
    with open('data/random_points.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header row if it exists

        # Iterate through each row in the CSV
        for row in reader:
            try:
                # Extract values from the two columns as integers
                value1 = int(row[0])
                value2 = int(row[1])

                # Update the sum for each column and increment the count
                sum_column1 += value1
                sum_column2 += value2
                count += 1
            except ValueError:
                # Handle non-integer values if they exist in the CSV
                print(f"Skipping row with non-integer values: {row}")

    # Calculate the average for each column
    average_column1 = sum_column1 / count
    average_column2 = sum_column2 / count

    # Display the averages
    print(f"Average of Column1: {average_column1}")
    print(f"Average of Column2: {average_column2}")
