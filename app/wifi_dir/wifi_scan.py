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

        logging.info(table)

    return devices


def wifi_scan_test():
    """
    TBD
    """
    # Wykonaj polecenie netsh
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'],
                            capture_output=True, text=True, check=False)

    #TODO: checkowanie tego return kodu

    # Sprawdź czy wystąpiły błędy
    if result.returncode == 0:
        # Przetwórz wyniki
        networks_info = result.stdout.split('\n')
        # print(networks_info)
        networks = []
        current_network = {}
        for line in networks_info:
            print(line)
            if "SSID" in line:
                current_network["SSID"] = line.split(":")[1].strip()
            elif "Signal" in line:
                current_network["Signal"] = line.split(":")[1].strip()
                networks.append(current_network)
                current_network = {}

        # creating table for the results
        table = PrettyTable()
        table.title = "Wifi raport"
        table.field_names = ["SSID", "SIGNAL"]

        for network in networks:
            table.add_row([network['SSID'], network['Signal']])

        logging.info(table)

    else:
        print("Wystąpił błąd podczas wykonania polecenia.")
