"""
TBD
"""
import logging


def setup_logging():
    """
    TBD
    """
    # logowanie ustawienia
    logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Create a handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    # Add the console handler to the root logger
    logging.getLogger().addHandler(console_handler)
