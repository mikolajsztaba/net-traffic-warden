import pyshark
import pandas as pd
import matplotlib.pyplot as plt
import time


def analyze_network_traffic(source='live', interface='eth0', pcap_file=None, known_bad_ips=set(), sniff_time=10,
                            packet_count=100):
    """
    Funkcja analizująca ruch sieciowy z wykorzystaniem PySharka.

    :param source: 'live' dla przechwytywania na żywo lub 'file' dla wczytania z pliku
    :param interface: Nazwa interfejsu sieciowego do przechwytywania na żywo
    :param pcap_file: Ścieżka do pliku .pcap (używane, gdy source='file')
    :param known_bad_ips: Zestaw znanych złośliwych adresów IP do wykrywania podejrzanych pakietów
    :param sniff_time: Czas przechwytywania w sekundach (używane, gdy source='live')
    :param packet_count: Liczba pakietów do analizy (używane, gdy source='live')
    """

    start_time = time.time()  # Początkowy czas przechwytywania
    end_time = start_time + sniff_time  # Czas końcowy przechwytywania
    packet_counter = 0

    # Przechwytywanie pakietów
    if source == 'live':
        capture = pyshark.LiveCapture(interface=interface)
    elif source == 'file' and pcap_file:
        capture = pyshark.FileCapture(pcap_file)
    else:
        raise ValueError("Invalid source or missing pcap_file for 'file' source.")

    data = {'src_ip': [], 'dst_ip': [], 'protocol': [], 'src_port': [], 'dst_port': []}
    suspicious_ips = set()

    # Analiza pakietów
    for packet in capture.sniff_continuously(packet_count=packet_count):
        if 'IP' in packet:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            protocol = packet.transport_layer
            src_port = getattr(packet[packet.transport_layer], 'srcport', 'Unknown')
            dst_port = getattr(packet[packet.transport_layer], 'dstport', 'Unknown')

            data['src_ip'].append(src_ip)
            data['dst_ip'].append(dst_ip)
            data['protocol'].append(protocol)
            data['src_port'].append(src_port)
            data['dst_port'].append(dst_port)

            if src_ip in known_bad_ips or dst_ip in known_bad_ips:
                suspicious_ips.add(src_ip)
                suspicious_ips.add(dst_ip)

            packet_counter += 1

            # Przerwanie przechwytywania po osiągnięciu żądanej liczby pakietów lub po upływie czasu
            if packet_counter >= packet_count or time.time() >= end_time:
                break

    # Tworzenie DataFrame
    df = pd.DataFrame(data)

    # Wizualizacja
    grouped_data = df.groupby(['src_ip', 'dst_ip', 'protocol']).size().reset_index(name='count')

    # Tworzenie wykresu
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_data.index, grouped_data['count'], color='skyblue')
    plt.xlabel('Source IP - Destination IP - Protocol')
    plt.ylabel('Count')
    plt.title('Network Traffic Analysis')
    plt.xticks(grouped_data.index,
               grouped_data.apply(lambda x: f"{x['src_ip']} - {x['dst_ip']} - {x['protocol']}", axis=1), rotation=90)
    plt.tight_layout()
    plt.show()

    # Wyświetlanie potencjalnych portów źródłowych i docelowych
    print("Potential Source Ports:")
    print(df['src_port'].value_counts())
    print("\nPotential Destination Ports:")
    print(df['dst_port'].value_counts())

    print(f"\nSuspicious IPs: {suspicious_ips}")
    print("Summary of Traffic Analysis:")
    print(df.describe())

    # Zapis danych do pliku CSV
    df.to_csv('network_traffic_analysis.csv', index=False)
    print("Data saved to 'network_traffic_analysis.csv'")

