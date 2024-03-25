from scapy.all import ARP, Ether, srp

import subprocess
import logging

from prettytable import PrettyTable
import ipaddress


def wifi_scan(prompts):
    user_input = ValueError
    while user_input is ValueError:
        user_input = input(prompts['address_wifi_input'])
        try:
            network = ipaddress.IPv4Network(user_input, strict=False)
        except:
            logging.error("WRONG IP ADD")
            pass

    arp = ARP(pdst=user_input)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)[0]

    devices = []
    for sent, received in result:
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
    # Wykonaj polecenie netsh
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    print(result.returncode)

    # Sprawdź czy wystąpiły błędy
    if result.returncode == 0:
        # Przetwórz wyniki
        networks_info = result.stdout.split('\n')
        print(networks_info)
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

        # Wyświetl wyniki
        for network in networks:
            print(f"SSID: {network['SSID']}, Signal: {network['Signal']}")
    else:
        print("Wystąpił błąd podczas wykonania polecenia.")
