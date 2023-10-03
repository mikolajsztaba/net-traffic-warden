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


# Logger configuration
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
    # ssh_client = connect_to_ssh('###', 22,
    #                             '###', '###')
    # return_code = execute_ssh_command(ssh_client, 'ls')
    logger.info(2)
    # logger.info(return_code)
    # close_ssh_connection(ssh_client)

    monitor_network_and_save_to_csv(csv_file='app/link_data/test.csv',
                                    duration=5)

    test_function(test=args.email)
    calculate_average()


if __name__ == "__main__":
    main()
