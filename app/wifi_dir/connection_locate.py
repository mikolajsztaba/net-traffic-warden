import psutil
import requests
import signal
import sys
import time


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


def monitor_packages():
    seen_ips = set()

    def signal_handler(sig, frame):
        print('\nPrzerwano przez użytkownika.')
        nonlocal stop
        stop = True

    stop = False
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        if stop:
            break

        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if conn.status == 'ESTABLISHED' and conn.raddr:
                ip_address = conn.raddr.ip
                if ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    print(f"Pobrane paczki: Adres IP: {ip_address}, Port: {conn.laddr.port}")
                    get_location_from_ip(ip_address)
        time.sleep(1)
