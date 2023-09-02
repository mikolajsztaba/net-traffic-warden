# Main function
import argparse

from charts.chart import example_chart


def test_function(test):
    print(test)
    example_chart()


def main():
    parser = argparse.ArgumentParser(description=
                                     "CLI for net-traffic-warden project")
    parser.add_argument("-e", "--email", type=str, help="The user's email")
    parser.add_argument("-p", "--phone", type=str, help="The user's phone number")

    args = parser.parse_args()

    test_function(test=args.email)


if __name__ == "__main__":
    main()
