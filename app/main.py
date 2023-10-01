"""
MAIN DOCSTRING
"""

# Main function
import argparse
import logging

from config.log_config import setup_logging

from datetime import datetime

from charts.chart import example_chart
from charts.data import calculate_average
from ssh.ssh_connection import (connect_to_ssh,
                                execute_ssh_command,
                                close_ssh_connection)
from monitoring.link_monitor import monitor_network_and_save_to_csv
from system_check.system_requirements import check_req


# current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# log_filename = f'app/logs/{current_datetime}.log'
#
# # Configure the logger
# logging.basicConfig(
#     filename=log_filename,  # Use the generated log file name
#     level=logging.DEBUG,
#     format='%(asctime)s - %(levelname)s - %(message)s'
# )

# Create a logger instance
# logger = logging.getLogger()

logger = logging.getLogger(__name__)

def test_function(test):
    """
    :param test:
    :return:
    """
    print(test)
    example_chart()


def main():
    """
    :return:
    """

    setup_logging()

    parser = argparse.ArgumentParser("CLI for net-traffic-warden project")
    parser.add_argument("-e", "--email",
                        type=str, help="The user's email")
    parser.add_argument("-p", "--phone",
                        type=str, help="The user's phone number")
    # PARSING CLI ARGUMENTS
    args = parser.parse_args()

    logger.info(args)

    # CHECK OS REQUIRIMENTS
    check_req()

    # SSH TESTS
    ssh_client = connect_to_ssh('###', 22,
                                '###', '###')
    return_code = execute_ssh_command(ssh_client, 'ls')
    logger.info(return_code)
    close_ssh_connection(ssh_client)

    monitor_network_and_save_to_csv(csv_file='app/link_data/test.csv',
                                    duration=5)

    test_function(test=args.email)
    calculate_average()


if __name__ == "__main__":
    main()
