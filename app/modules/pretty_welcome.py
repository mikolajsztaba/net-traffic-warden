from prettytable import PrettyTable
import logging


def generate_template(author, title, year):
    table = PrettyTable()
    table.field_names = ["Author", "Title of the thesis", "Year"]
    table.add_row([author, title, year])

    # Ustawienia stylu tabeli
    table.align = "l"
    table.border = True
    table.header = True
    table.padding_width = 1

    return table

