"""
TBD
"""

import subprocess
import logging

import ipaddress

from scapy.all import ARP, Ether, srp

from prettytable import PrettyTable


def wifi_scan(prompts):
    """
    TBD
    """
    user_input = ValueError
    while user_input is ValueError:
        user_input = input(prompts['address_wifi_input'])
        try:
            ipaddress.IPv4Network(user_input, strict=False)
            run_flag = True
        except ipaddress.AddressValueError as error:
            logging.error(error)
            run_flag = False

    devices = []

    if run_flag:
        arp = ARP(pdst=user_input)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp
        result = srp(packet, timeout=3, verbose=False)[0]

        for _, received in result:
            devices.append({'ip': received.psrc, 'mac': received.hwsrc})

        # creating table for the results
        table = PrettyTable()
        table.title = "Wifi scanning"
        table.field_names = ["IP address", "MAC address"]

        for device in devices:
            table.add_row([device['ip'], device['mac']])

        logging.info("\n%s", table)

    return devices


def wifi_scan_test():
    """
    TBD
    """
    command = ['netsh', 'wlan', 'show', 'interfaces']

    result = subprocess.run(command,
                            capture_output=True, text=True, check=False)

    if result.returncode == 0:
        logging.info("The command has been executed %s.",
                     ' '.join(command))

        # creating table
        networks_info = result.stdout.split('\n')
        networks_table = PrettyTable(["Property", "Value"])
        networks_table.title = "Basic info about connected wifi network"

        for line in networks_info[2:]:
            if ":" in line:
                property_name, value = line.split(":", 1)
                networks_table.add_row([property_name.strip(), value.strip()])

        logging.info("\n%s", networks_table)

        networks = []
        current_network = {}

        for line in networks_info:
            if "SSID" in line:
                current_network["SSID"] = line.split(":")[1].strip()
            elif "Signal" in line:
                current_network["Signal"] = line.split(":")[1].strip()
                networks.append(current_network)

        # tutaj beda alarmy do innych funkcji tez
        if int(current_network["Signal"][:-1]) < 95:
            print("AAAAAAAAAAAAAAA")


        # creating table for the results
        table = PrettyTable()
        table.title = "Wifi raport"
        table.field_names = ["SSID", "SIGNAL"]

        for network in networks:
            table.add_row([network['SSID'], network['Signal']])

        logging.info("\n%s", table)
    else:
        logging.error("There was an error while executing: %s",
                      ' '.join(command))
