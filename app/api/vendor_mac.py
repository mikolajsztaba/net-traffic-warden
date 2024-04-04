"""
TBD
"""
import logging
import time

import requests


def get_vendor(mac_address):
    """
    TBD
    """
    api_url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        return (f"Failed to find vendor for the provided MAC address."
                f"Status code: {response.status_code}")
    except requests.exceptions.RequestException as error:
        return f"Error: {error}"


def test_get_vendor(devices):
    """
    TBD
    """
    mac_addresses = [device['mac'] for device in devices]

    # defining empty list to be fulfilled with unknown mac addresses
    unknown_addresses = []

    unknown_addresses.append('ez')

    for mac_address in mac_addresses:
        print(f"Analyzing MAC address: {mac_address}")
        vendor = get_vendor(mac_address)
        if 'Failed to find' in vendor:
            unknown_addresses.append(mac_address)
        print("Vendor:", vendor)
        print("-" * 50)
        time.sleep(1)

    logging.warning("Unknown MAC addresses %s.", unknown_addresses)
