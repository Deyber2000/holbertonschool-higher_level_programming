#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    if (i % 2 == 1):
        i -= 32
    print("{:c}".format(i), end="")
