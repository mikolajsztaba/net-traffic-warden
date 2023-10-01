import logging
import datetime


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set the root logger's level to DEBUG

    # Create a log file with a timestamp
    current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"mylog_{current_datetime}.log"

    # Create a file handler and specify the log file with timestamp
    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.INFO)  # Set the file handler's level to INFO

    # Create a console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set the console handler's level to DEBUG

    # Create a formatter and attach it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
