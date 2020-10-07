#!/usr/bin/python3
"""Module for pascal_triangle"""


def pascal_triangle(n):
    """Returns list of lists of integers represnting
       Pascal's triangle of n
    """
    return_list = []
    if n <= 0:
        return (return_list)
    for i in range(n):
        row = [1]
        if return_list:
            last_row = return_list[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        return_list.append(row)
    return (return_list)
