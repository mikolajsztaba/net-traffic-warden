"""
TBD
"""
import sys

import click
import logging

from language import read_prompts_from_yaml

# logowanie ustawienia
logging.basicConfig(filename='network_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a handler for console output
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the root logger
logging.getLogger().addHandler(console_handler)


@click.command()
def main():
    """CLI for network monitoring tool."""

    # VARIABLES
    file_path = None

    while True:

        logging.info("AAAAAAAAAAAAAAAA")

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
                click.echo("Koniec programu.")
                sys.exit(0)
            elif language_choice == 1:
                file_path = 'app/language_schemas/prompts_english.yaml'
            elif language_choice == 2:
                file_path = 'app/language_schemas/prompts_polish.yaml'
            else:
                print(f"{language_choice} is an invalid choice."
                      f"Please try again.")

        # wczytanie promptów
        prompts = read_prompts_from_yaml(file_path)
        print(prompts)
        print(prompts["prompt-imie"])

        # opcje podstawowe w skrypcie
        click.echo("Dostępne opcje:")
        click.echo("1. Powitanie")
        click.echo("2. Kalkulator")
        click.echo("0. Zakończ")

        choice = click.prompt("Wybierz tryb (wpisz numer)", type=int)

        if choice == 0:
            click.echo("Koniec programu.")
            sys.exit(0)
        elif choice == 1:
            greet()
        elif choice == 2:
            calculate()
        else:
            click.echo("Nieprawidłowy wybór. Spróbuj ponownie.")


def greet():
    """Funkcja obsługująca tryb powitania."""
    name = click.prompt("Podaj imię", type=str)
    age = click.prompt("Podaj wiek", type=int)
    greet_option = click.confirm("Pokazać powitanie?", default=True)

    if greet_option:
        click.echo(f'Witaj, {name}!')

    click.echo(f'Twój wiek to {age} lat.')


def calculate():
    """Funkcja obsługująca tryb kalkulatora."""
    number1 = click.prompt("Podaj pierwszą liczbę", type=float)
    operator = click.prompt("Podaj operator (+, -, *, /)",
                            type=click.Choice(['+', '-', '*', '/']))
    number2 = click.prompt("Podaj drugą liczbę", type=float)

    result = None
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        if number2 != 0:
            result = number1 / number2
        else:
            click.echo("Błąd: Nie można dzielić przez zero.")
            return

    click.echo(f'Wynik: {result}')


if __name__ == '__main__':
    main()
