#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_num = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000
               }

    if roman_string is None or type(roman_string) is not str:
        return 0

    converted = 0
    length = len(roman_string)

    for i in range(length):
        if i is (length - 1):
            converted += rom_num[roman_string[i]]
        else:
            if rom_num[roman_string[i]] >= rom_num[roman_string[i + 1]]:
                converted += rom_num[roman_string[i]]
            else:
                converted -= rom_num[roman_string[i]]
    return (converted)
