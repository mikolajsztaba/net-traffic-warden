"""
TBD
"""
import sys

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
                click.echo("The script is terminated.")
                sys.exit(0)
            elif language_choice == 1:
                file_path = 'app/language_schemas/prompts_english.yaml'
            elif language_choice == 2:
                file_path = 'app/language_schemas/prompts_polish.yaml'
            else:
                print(f"{language_choice} is an invalid choice. "
                      f"Please try again.")

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
            print("AAA")
        elif choice == 2:
            print("BBBB")
        elif choice == 3:
            wifi_scan_test()
        elif choice == 4:
            wifi_scan(prompts)
        else:
            click.echo("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == '__main__':
    main()
