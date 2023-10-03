"""
LINK MONITOR DOCSTRING
"""
import csv
import time

import psutil
import logging

logger = logging.getLogger(__name__)


# Funkcja do monitorowania łącza na danym PC i zapisywania wyników do pliku CSV
def monitor_network_and_save_to_csv(csv_file, duration):
    """
    :param csv_file:
    :param duration:
    :return:
    """
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        header = ['Time', 'Upload (B/s)', 'Download (B/s)']
        writer = csv.writer(file)
        writer.writerow(header)

        end_time = time.time() + duration

        while time.time() < end_time:
            current_time = time.strftime('%Y-%m-%d %H:%M:%S')
            net_stats = psutil.net_io_counters()
            upload = net_stats.bytes_sent
            download = net_stats.bytes_recv

            writer.writerow([current_time, upload, download])
            print(f'{current_time}: Upload: {upload} B/s,'
                  f'Download: {download} B/s')

            time.sleep(1)

# if __name__ == '__main__':
#     csv_file = 'network_stats.csv'
#     duration = 5  # Czas monitorowania w sekundach
#
#     try:
#         monitor_network_and_save_to_csv(csv_file, duration)
#     except KeyboardInterrupt:
#         print("Zakończono monitorowanie łącza.")
