import psutil
import requests
import signal
import sys
import time
import logging


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


def monitor_packages(alert_countries):
    seen_ips = set()

    def signal_handler(sig, frame):
        print('\nPrzerwano przez użytkownika.')
        nonlocal stop
        stop = True

    stop = False
    signal.signal(signal.SIGINT, signal_handler)

    while True:
        logging.info("If you want to leave the sniffing mode, type ctrl+c")
        if stop:
            break

        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if conn.status == 'ESTABLISHED' and conn.raddr:
                ip_address = conn.raddr.ip
                if ip_address not in seen_ips:
                    seen_ips.add(ip_address)
                    logging.info(f"Pobrane paczki: Adres IP: {ip_address}, Port: {conn.laddr.port}")
                    location_info = get_location_from_ip(ip_address)
                    country = location_info['country']
                    if country in alert_countries:
                        logging.warning("Traffic from country specified as alert detected: %s", country)
        time.sleep(1)
