#!/usr/bin/python3
def print_last_digit(number):
    # Get last digit
    last = abs(number) % 10
    print(last, end="")
    return last
