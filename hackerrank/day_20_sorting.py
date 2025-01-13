#!/bin/python3

import math
import os
import random
import re
import sys


def swap(arr: list[int], i1: int, i2: int):
    """
    Note: changes the original array, as when you pass the list as a parameter in python, you're actually
    passing its reference
    """
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp
    # Or
    # arr[i1], arr[i2] = arr[i2], arr[i1]
    return arr


def bubble_sort(arr: list[int]):
    len_arr = len(arr)
    actualNumberOfSwaps = 0
    for i in range(len_arr):
        numberOfSwaps = 0
        for j in range(len_arr - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                numberOfSwaps += 1
        actualNumberOfSwaps += numberOfSwaps
        if numberOfSwaps == 0:
            break
    return arr, actualNumberOfSwaps


if __name__ == "__main__":
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    # a = list(map(int, "1 2 3".rstrip().split()))
    # a = list(map(int, "3 2 1".rstrip().split()))
    arr, actualNumberOfSwaps = bubble_sort(a)
    print(f"Array is sorted in {actualNumberOfSwaps} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")
    # Write your code here
