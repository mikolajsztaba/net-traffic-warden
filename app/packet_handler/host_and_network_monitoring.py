import psutil
from scapy.all import *
from tabulate import tabulate
import time


# Funkcja sprawdzająca procesy systemowe
def check_system_processes():
    anomalies = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
        try:
            # Pobranie informacji o procesie
            process_info = proc.info
            # Sprawdzenie anomalii (np. wysokie użycie CPU i RAM)
            if process_info['cpu_percent'] > 80:
                anomalies.append(
                    f"High CPU usage by {process_info['name']} (PID: {process_info['pid']}): {process_info['cpu_percent']}%")
            if process_info['memory_percent'] > 80:
                anomalies.append(
                    f"High Memory usage by {process_info['name']} (PID: {process_info['pid']}): {process_info['memory_percent']}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return anomalies


# Funkcja sprawdzająca ruch sieciowy
def check_network_traffic():
    anomalies = []
    packet_count = {}

    def packet_callback(packet):
        packet_info = {}
        try:
            if Ether in packet:
                eth_layer = packet[Ether]
                packet_info['Ethernet_dst'] = eth_layer.dst
                packet_info['Ethernet_src'] = eth_layer.src
                packet_info['Ethernet_type'] = eth_layer.type

            if IP in packet:
                ip_layer = packet[IP]
                packet_info['IP_src'] = ip_layer.src
                packet_info['IP_dst'] = ip_layer.dst
                packet_info['IP_proto'] = ip_layer.proto

            if TCP in packet:
                tcp_layer = packet[TCP]
                packet_info['TCP_sport'] = tcp_layer.sport
                packet_info['TCP_dport'] = tcp_layer.dport
                packet_info['TCP_flags'] = tcp_layer.flags

            if UDP in packet:
                udp_layer = packet[UDP]
                packet_info['UDP_sport'] = udp_layer.sport
                packet_info['UDP_dport'] = udp_layer.dport

            if ICMP in packet:
                icmp_layer = packet[ICMP]
                packet_info['ICMP_type'] = icmp_layer.type
                packet_info['ICMP_code'] = icmp_layer.code

            # Zamiana słownika na krotkę (dzięki czemu możemy używać jako klucz w słowniku)
            packet_key = tuple(packet_info.items())

            if packet_key in packet_count:
                packet_count[packet_key] += 1
            else:
                packet_count[packet_key] = 1

        except Exception as e:
            anomalies.append(f"Error processing packet: {e}")

    # Przechwytywanie ruchu sieciowego (przez 10 sekund)
    sniff(prn=packet_callback, timeout=10)

    # Konwersja liczników pakietów do listy słowników
    packet_data = []
    for packet_key, count in packet_count.items():
        packet_info = dict(packet_key)
        packet_info['Count'] = count
        packet_data.append(packet_info)

    return anomalies, packet_data


# Funkcja monitorująca
def monitor_system_and_network():
    while True:
        print("Scanning for anomalies...")

        # Monitorowanie procesów
        process_anomalies = check_system_processes()
        for anomaly in process_anomalies:
            print(f"Process anomaly detected: {anomaly}")

        # Monitorowanie ruchu sieciowego
        network_anomalies, packet_data = check_network_traffic()
        for anomaly in network_anomalies:
            print(f"Network anomaly detected: {anomaly}")

        if packet_data:
            print("\nCaptured Packets:")
            print(tabulate(packet_data, headers="keys", tablefmt="pretty"))

        # Odczekaj przed kolejnym skanowaniem
        time.sleep(5)  # 60 sekund przerwy