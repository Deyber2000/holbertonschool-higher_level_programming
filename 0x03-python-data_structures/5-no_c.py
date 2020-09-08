#!/usr/bin/python3
def no_c(my_string):
    our_string = ""
    for i in my_string:
        if (i != "c" and i != "C"):
            our_string += i
    return our_string
