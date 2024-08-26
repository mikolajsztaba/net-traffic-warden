"""
TBD
"""
import sys
import logging

import click

from language import read_prompts_from_yaml
from log.log_handler import setup_logging, clear_logs
from wifi_dir.wifi_scan import wifi_scan, wifi_scan_test
from wifi_dir.ddos_attack import ddos_execute
from api.vendor_mac import test_get_vendor
from wifi_dir.sniffing import start_sniffing
from wifi_dir.connection_locate import monitor_packages
from wifi_dir.connection_status import perform_speed_tests
# from packet_handler.packet_sniff import analyze_network_traffic
from packet_handler.host_and_network_monitoring import monitor_system_and_network
from modules.system_network_status import track_local_resources
from modules.pretty_welcome import generate_template
from modules.snmp_discover import run_snmp_discovery
from utils.read_log import get_latest_file_content
from client.email_client import send_email

# ustawienie logowania
setup_logging()


@click.command()
def main():
    """
    CLI for network monitoring tool.
    """
    # VARIABLES
    file_path = None

    # tabelka wstepna
    template = generate_template("Mikolaj Sztaba","Analysis of the process of automatic "
                                       "network monitoring using Python libraries", 2024)
    logging.info("\n%s", template)

    while True:

        # informacyjnie o 0 jako wyjściu z programu
        click.echo("In case you want to exit the program,"
                   "please enter 0 in any prompt.")

        delete_logs = click.prompt(
            "If you want to delete previous logs type [t/f]",
            type=bool)

        if delete_logs:
            clear_logs()

        while file_path is None:
            # wybór języka działania narzędzia
            click.echo("Available language options:")
            click.echo("1. English")
            click.echo("2. Polish")
            language_choice = click.prompt(
                "Choose your language (type number)", type=int)

            if language_choice == 0:
                logging.info("The script has been terminated.")
                sys.exit(0)
            elif language_choice == 1:
                file_path = 'app/language_schemas/prompts_english.yaml'
                logging.info("The user has chosen the english language.")
            elif language_choice == 2:
                file_path = 'app/language_schemas/prompts_polish.yaml'
                logging.info("The user has chosen the polish language.")
            else:
                logging.error("%s is an invalid choice. "
                              "Please try again.", language_choice)

        # wczytanie promptów
        prompts = read_prompts_from_yaml(file_path)

        # opcje podstawowe w skrypcie
        click.echo(prompts['available_options'])
        click.echo(prompts['network_info'])
        click.echo(prompts['sniff_info'])
        click.echo(prompts['scapy_prompt'])
        click.echo(prompts['wifi_scan'])
        click.echo(prompts['ddos_attack'])
        click.echo(prompts['blocking_packets_info'])
        click.echo(prompts['package_location_monitoring'])
        click.echo(prompts['local_resources'])
        click.echo(prompts['spotting_anomalies'])
        click.echo(prompts['snmp_prompt'])
        click.echo("11. Send email with last run logs!")
        click.echo(prompts['termination'])

        choice = click.prompt(prompts['mode_type'], type=int)

        if choice == 0:
            click.echo(prompts['farewell_message'])
            sys.exit(0)
        elif choice == 1:
            perform_speed_tests()
        elif choice == 2:
            analyze_network_traffic(source='live', interface='eth0', known_bad_ips={'192.168.1.1', '10.0.0.1'},
                                    sniff_time=10)
        elif choice == 3:
            wifi_scan_test()
        elif choice == 4:
            full_devices = wifi_scan(prompts)
            test_get_vendor(full_devices)
        elif choice == 5:
            ddos_execute(prompts)
        elif choice == 6:
            block_ips = click.prompt(prompts['address_list'])
            block_ips = block_ips.split(',')
            block_ips = [element.strip() for element in block_ips]
            start_sniffing(block_ips)
        elif choice == 7:
            blocks_countries = click.prompt(prompts['alert_countries'])
            monitor_packages(blocks_countries)
        elif choice == 8:
            track_local_resources()
        elif choice == 9:
            monitor_system_and_network()
        elif choice == 10:
            run_snmp_discovery()
        elif choice == 11:
            directory = 'logs'
            content = get_latest_file_content(directory)
            send_email('Temat', content, 'mikolaj25sztaba@gmail.com', 'traffic-warden@outlook.com', 'Test123!@', )
        else:
            logging.info("Wrong choice. Try again please...")



if __name__ == '__main__':
    main()
