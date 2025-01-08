#!/bin/python3

import math
import os
import random
import re
import sys
import traceback

# for some reason keeping the below condition gives:
# Error reading result file.You should use exception handling concepts. in hackerrank
# if __name__ == "__main__":

S = input().strip()

try:
    s_int = int(S)
    print(s_int)
except ValueError:
    print("Bad String")
