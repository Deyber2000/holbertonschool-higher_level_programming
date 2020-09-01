#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
ld = number[len(number) - 1]
ld = int(ld)
if ld > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, ld))
elif ld == 0:
    print("Last digit of {} is {} and is 0".format(number, ld))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, ld))
