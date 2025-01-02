#!/bin/python3

import math
import os
import random
import re
import sys


def convert_decimal_int_to_binary(decimal_int: int):
    binary_str = ""

    def get_quotient_remainder(num, divider):
        return (num // divider, num % divider)

    def recursive_func(decimal_int: int):
        nonlocal binary_str
        print(decimal_int, type(decimal_int), binary_str)
        if decimal_int == 1:
            return "1" + binary_str
        elif decimal_int == 0:
            return "0" + binary_str
        else:
            quotient, remainder = get_quotient_remainder(decimal_int, 2)
            decimal_int = quotient

            binary_str = str(remainder) + binary_str

            return recursive_func(decimal_int)

    return recursive_func(decimal_int)


if __name__ == "__main__":
    n = int(input().strip())
    binary = convert_decimal_int_to_binary(n)

    print(binary)
