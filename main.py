# Main function
import argparse

from charts.chart import example_chart
from charts.data import calculate_average
from ssh.ssh_connection import connect_to_ssh, execute_ssh_command, close_ssh_connection

def test_function(test):
    print(test)
    example_chart()


def main():
    parser = argparse.ArgumentParser(description=
                                     "CLI for net-traffic-warden project")
    parser.add_argument("-e", "--email", type=str, help="The user's email")
    parser.add_argument("-p", "--phone", type=str, help="The user's phone number")

    args = parser.parse_args()

    # test_function(test=args.email)
    # calculate_average()

    # SSH TESTS
    ssh_client = connect_to_ssh('###', 22, '###', '###')
    return_code = execute_ssh_command(ssh_client, 'ls')
    close_ssh_connection(ssh_client)


if __name__ == "__main__":
    main()
