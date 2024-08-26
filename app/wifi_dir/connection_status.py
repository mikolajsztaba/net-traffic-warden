import time
import requests
from prettytable import PrettyTable
import logging

# Ustal URL i rozmiar pliku do testowania
DOWNLOAD_URL = "http://ipv4.download.thinkbroadband.com/5MB.zip"
UPLOAD_URL = "https://httpbin.org/post"
FILE_SIZE_MB = 10  # Rozmiar pliku do testowania (MB)


def perform_speed_tests():
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

    # Wykonanie testów
    download_speed = measure_download_speed(DOWNLOAD_URL, FILE_SIZE_MB)
    upload_speed = measure_upload_speed(UPLOAD_URL, FILE_SIZE_MB)

    # Utworzenie tabeli
    table = PrettyTable()
    table.field_names = ["Metryka", "Wynik"]
    table.add_row(["Średnia prędkość pobierania (Mbps)", round(download_speed, 2)])
    table.add_row(["Średnia prędkość wysyłania (Mbps)", round(upload_speed, 2)])

    logging.info(table)

