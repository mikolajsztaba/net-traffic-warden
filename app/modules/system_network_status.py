import psutil
import time
from prettytable import PrettyTable

def get_network_usage():
    """
    Funkcja zwraca ilość przesłanych i otrzymanych bajtów w sieci w ciągu sekundy.
    """
    net_io_1 = psutil.net_io_counters()
    time.sleep(1)  # Odczekaj 1 sekundę
    net_io_2 = psutil.net_io_counters()

    # Oblicz różnicę bajtów przesłanych i otrzymanych
    bytes_sent_per_sec = net_io_2.bytes_sent - net_io_1.bytes_sent
    bytes_recv_per_sec = net_io_2.bytes_recv - net_io_1.bytes_recv

    return bytes_sent_per_sec, bytes_recv_per_sec

def format_bytes(bytes):
    """
    Funkcja formatuje bajty na bardziej czytelne jednostki (KB/s, MB/s).
    """
    for unit in ['B/s', 'KB/s', 'MB/s', 'GB/s']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0

def track_local_resources():
    """
    Funkcja służy do śledzenia lokalnych zasobów systemowych i wyświetlania ich w formie tabeli.
    """
    # Tworzenie tabeli
    table = PrettyTable()
    table.field_names = ["Zasób", "Wartość"]

    # Śledzenie użycia procesora
    cpu_usage = psutil.cpu_percent(interval=1)
    table.add_row(["Użycie CPU", f"{cpu_usage}%"])

    # Śledzenie użycia pamięci
    memory_info = psutil.virtual_memory()
    table.add_row(["Użycie pamięci", f"{memory_info.percent}%"])

    # Śledzenie użycia dysku
    disk_usage = psutil.disk_usage('/')
    table.add_row(["Użycie dysku", f"{disk_usage.percent}%"])

    # Śledzenie aktywności sieciowej
    bytes_sent_per_sec, bytes_recv_per_sec = get_network_usage()
    table.add_row(["Sieć - Wysyłanie", format_bytes(bytes_sent_per_sec)])
    table.add_row(["Sieć - Odbieranie", format_bytes(bytes_recv_per_sec)])

    # Śledzenie aktywnych procesów
    processes = [(proc.info['pid'], proc.info['name']) for proc in psutil.process_iter(['pid', 'name'])]
    table.add_row(["Liczba aktywnych procesów", len(processes)])

    # Wyświetlanie tabeli
    print(table)