#!/bin/python3

# BELOW IS MY SOLUTION (Done with no reference)

import math
import os
import random
import re
import sys
from typing import Dict, List, Tuple

"""
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
"""

"""
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) (0, 5)
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) (1, 5)
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) (2, 5)
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) (3, 5)
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) (4, 5)
(5, 0) (5, 1) (5, 2) (5, 3) (5, 4) (5, 5)
"""

# First we extract all possible 3x3
# Take the first row
# Take the third row
# Take the intersection of second row and second column
# Sum first row
# Sum second row
# Add (sum of first row) + (sum of second row) + (intersection of second row and second column)
#


# Let me start with extracting First row

two_d_arr = List[List[int]]


def extract_first_row(arr: two_d_arr):
    return arr[0]


def extract_second_row(arr: two_d_arr):
    return arr[1]


def extract_third_row(arr: two_d_arr):
    return arr[2]


def extract_intersection(arr: two_d_arr):
    return arr[1][1]


def sum_array(arr: List[int]):
    return sum(arr)


def get_row_length(arr: two_d_arr):
    return len(arr[0])


def get_column_length(arr: two_d_arr):
    return len(arr)


def get_hourglass_coordinate_from_i_j(i: int, j: int):
    """
    Get upto i+2 and j+2 and return all the tuples of (i,j) for hourglass
    """
    i_j_array: List[Tuple[int, int]] = []
    # i_j_array.append((i, j))
    i_array = []
    j_array = []

    for n in range(3):
        i_array.append(i + n)
        j_array.append(j + n)
    # print(i_array, "i_array")
    # print(j_array, "j_array")
    row_count = 0
    # NOTE: row_count and column_count start from 1 to 3
    for item_i in i_array:
        row_count += 1
        column_count = 0
        for item_j in j_array:
            column_count += 1
            if row_count == 2 and column_count != 2:
                continue
            i_j_array.append((item_i, item_j))

    return i_j_array


def get_hourglass_dict(arr: two_d_arr):
    """
    (0, 0) (0, 1) (0, 2)
    (1, 0) (1, 1) (1, 2)
    (2, 0) (2, 1) (2, 2)
    """
    # arr = [
    #     [5, 2, 3, 6, 5, 4],
    #     [5, 2, 3, 6, 5, 4],
    #     [5, 2, 3, 6, 5, 4],
    #     [5, 2, 3, 6, 5, 4],
    #     [5, 2, 3, 6, 5, 4],
    #     [5, 2, 3, 6, 5, 4],
    # ]
    # first_arr = [
    #     [arr[0][0], arr[0][1], arr[0][2]],
    #     [arr[1][0], arr[1][1], arr[1][2]],
    #     [arr[2][0], arr[2][1], arr[2][2]],
    # ]

    temp_arr: List[Tuple[int, int]] = []
    # NOTE: hourglass can only be formed upto 4th row that is (row length)/2 + 1
    # NOTE: hourglass can only be formed upto 4th column that is (column length)/2 + 1
    for i in range(get_row_length(arr) // 2 + 1):
        for j in range(get_column_length(arr) // 2 + 1):
            temp_arr.append((i, j))

    hourglasses = {}
    no_of_hourglass = 0
    for el in temp_arr:
        hourglass_items = []
        no_of_hourglass += 1
        i, j = el
        hour_glass_coordinates = get_hourglass_coordinate_from_i_j(i, j)
        for coordinate in hour_glass_coordinates:
            c_x, c_y = coordinate
            hourglass_item = arr[c_x][c_y]
            hourglass_items.append(hourglass_item)
        hourglasses[no_of_hourglass] = hourglass_items

    return hourglasses


def calculate_sum_of_hourglass(hourglass_dict: Dict[int, List[int]]):
    di = {}
    for key, value in hourglass_dict.items():
        di[key] = sum(value)
    return di


def get_max_hourglass(hourglass_sum_di: Dict[int, int]):
    # print(hourglass_sum_di, "hourglass_sum_di", type(hourglass_sum_di))
    max_sum = 0
    for key, value in hourglass_sum_di.items():
        if value > max_sum:
            max_sum = value
    return max_sum


def hourglass_factory(arr: two_d_arr):
    hourglass_dict = get_hourglass_dict(arr)
    # print(hourglass_dict)
    hourglass_sum_dict = calculate_sum_of_hourglass(hourglass_dict)
    return get_max_hourglass(hourglass_sum_dict)


if __name__ == "__main__":
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # arr = [
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0],
    #     [1, 1, 1, 0, 0, 0],
    #     [0, 0, 2, 4, 4, 0],
    #     [0, 0, 0, 2, 0, 0],
    #     [0, 0, 1, 2, 4, 0],
    # ]
    print(hourglass_factory(arr))
    # print(get_hourglass_coordinate_from_i_j(0, 0))

# BELOW IS LINK TO THE CODE I FOUND IN GITHUB:
# https://github.com/nathan-abela/HackerRank-Solutions/blob/master/30%20Days%20of%20Code/Python/12%20-%20Day%2011%20-%202D%20Arrays.py
