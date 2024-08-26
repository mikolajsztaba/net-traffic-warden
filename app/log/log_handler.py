"""
TBD
"""
import logging
import os

import datetime


def setup_logging():
    """
    TBD
    """

    current_time = datetime.datetime.now()
    date_format = "%d_%m_%Y--%H-%M"
    formatted_date_format = current_time.strftime(date_format)
    print(formatted_date_format)

    logging.basicConfig(filename=f'logs/network_monitor-'
                                 f'{formatted_date_format}.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    logging.getLogger().addHandler(console_handler)


def clear_logs():
    """
    TBD
    """
    logs_dir = os.path.join(os.path.dirname(__file__), '../..', 'logs')
    for file in os.listdir(logs_dir):
        file_path = os.path.join(logs_dir, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except PermissionError:
            pass

    logging.info("All logs has been deleted.")
