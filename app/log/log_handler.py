"""
TBD
"""
import logging

import datetime


def setup_logging():
    """
    TBD
    """

    # calculating datetime
    current_time = datetime.datetime.now()
    date_format = "%d_%m_%Y--%H-%M"
    formatted_date_format = current_time.strftime(date_format)

    # logging settings
    logging.basicConfig(filename=f'logs/network_monitor-'
                                 f'{formatted_date_format}.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Create a handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the root logger
    logging.getLogger().addHandler(console_handler)
