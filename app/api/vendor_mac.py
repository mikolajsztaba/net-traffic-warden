"""
TBD
"""
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


def test_get_vendor():
    """
    TBD
    """
    test_addresses = ['18:34:af:a4:45:df',
                      '38:ba:f8:77:de:09',
                      '60:3e:5f:07:34:ff',
                      'e6:77:d3:10:57:c1',
                      'XYZ']

    for mac_address in test_addresses:
        print(f"Analyzing MAC address: {mac_address}")
        vendor = get_vendor(mac_address)
        print("Vendor:", vendor)
        print("-" * 50)
        time.sleep(1)
