#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program identifies the month from a value


def main():
    # this function identifies the month from a value

    print("This program identifies the month from a given value.")

    # input
    month_value = int(input("Enter a number between 1-12: "))
    print("")

    # process
    if month_value == 1:
        # output
        print("This month is January")
    elif month_value == 2:
        # output
        print("This month is February")
    elif month_value == 3:
        # output
        print("This month is March")
    elif month_value == 4:
        # output
        print("This month is April")
    elif month_value == 5:
        # output
        print("This month is May")
    elif month_value == 6:
        # output
        print("This month is June")
    elif month_value == 7:
        # output
        print("This month is July")
    elif month_value == 8:
        # output
        print("This month is August")
    elif month_value == 9:
        # output
        print("This month is September")
    elif month_value == 10:
        # output
        print("This month is October")
    elif month_value == 11:
        # output
        print("This month is November")
    elif month_value == 12:
        # output
        print("This month is December")
    else:
        # output
        print("Error, this is not a month.")


if __name__ == "__main__":
    main()
