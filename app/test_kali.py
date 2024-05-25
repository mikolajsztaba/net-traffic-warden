from scapy.all import *

# def block_ping(pkt):
#     if ICMP in pkt:
#         print("Ping packet detected from: ", pkt[IP].src)
#         # Komenda do blokowania pakietu ICMP za pomocą iptables
#         os.system("iptables -A INPUT -p icmp --icmp-type echo-request -s " + pkt[IP].src + " -j DROP")
#         print("Blocked ping packet from: ", pkt[IP].src)
#
# # Rozpoczęcie nasłuchiwania pakietów ICMP
# sniff(prn=block_ping, filter="icmp", store=0)


import psutil
import time

def monitor_packages():
    while True:
        connections = psutil.net_connections(kind='inet')
        print(connections)
        for conn in connections:
            if conn.status == 'ESTABLISHED':
                print(connections)
                print(f"Pobrane paczki: Adres IP: {conn.raddr.ip}, Port: {conn.laddr.port}")
        time.sleep(1)

if __name__ == "__main__":
    monitor_packages()



import requests

def get_location_from_ip(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    data = response.json()

    city = data.get('city', 'Unknown')
    region = data.get('region', 'Unknown')
    country = data.get('country', 'Unknown')
    loc = data.get('loc', 'Unknown')

    location_info = {
        'city': city,
        'region': region,
        'country': country,
        'loc': loc
    }

    print(f"Lokalizacja dla adresu IP {ip_address}:")
    print(f"Miasto: {location_info['city']}")
    print(f"Region: {location_info['region']}")
    print(f"Kraj: {location_info['country']}")
    print(f"Współrzędne: {location_info['loc']}")

    return location_info

# Przykładowe użycie funkcji
ip_address = "133.130.108.36"
location_info = get_location_from_ip(ip_address)

