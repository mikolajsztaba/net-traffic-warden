"""
TBD
"""
import sys
import logging

import click

from language import read_prompts_from_yaml
from log.log_handler import setup_logging
from wifi_dir.wifi_scan import wifi_scan, wifi_scan_test

# ustawienie logowania
setup_logging()


@click.command()
def main():
    """
    CLI for network monitoring tool.
    """
    # VARIABLES
    file_path = None

    while True:

        # informacyjnie o 0 jako wyjściu z programu
        click.echo("In case you want to exit the program,"
                   "please enter 0 in any prompt.")

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
        click.echo("1. Powitanie")
        click.echo("2. Kalkulator")
        click.echo("3. Scapy testowe")
        click.echo(prompts['wifi_scan'])
        click.echo(prompts['termination'])

        choice = click.prompt(prompts['mode_type'], type=int)

        if choice == 0:
            click.echo(prompts['farewell_message'])
            sys.exit(0)
        elif choice == 1:
            logging.info("FUNKCJA NUMER 1")
        elif choice == 2:
            logging.info("FUNKCJA NUMER 2")
        elif choice == 3:
            logging.info("The user has chosen the 3rd option.")
            wifi_scan_test()
        elif choice == 4:
            logging.info("The user has chosen the wifi scan option. ")
            wifi_scan(prompts)
        else:
            logging.info("Wrong choice. Try again please...")


if __name__ == '__main__':
    main()
