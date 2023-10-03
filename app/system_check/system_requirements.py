"""
Check for mininet presence.
"""
import platform
import subprocess
import logging

logger = logging.getLogger(__name__)


def is_mininet_installed():
    """
    :return:
    """
    try:
        # Check if 'mn' (Mininet's command-line tool) is available
        subprocess.check_output(['mn', '--version'], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False


def get_current_os():
    """
    :return:
    """
    system = platform.system()
    if system == "Linux":
        return "Linux"
    if system == "Windows":
        return "Windows"
    if system == "Darwin":
        return "macOS"
    return "Unknown"


def check_req():
    """
    :return:
    """
    current_os = get_current_os()
    logger.info(f"Current operating system: {current_os}")

    if current_os == "Linux":
        mininet_installed = is_mininet_installed()
        if mininet_installed:
            print("Mininet is installed.")
        else:
            print("Mininet is not installed.")
    else:
        print("Mininet could only be installed on Linux.")
