#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)
    avg = 0
    weight = 0
    for x in my_list:
        avg += x[0] * x[1]
        weight += x[1]
    return (avg / weight)
