#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    ld = number[-1]
    ld = int(ld)
    print(ld, end="")
    return(ld)
