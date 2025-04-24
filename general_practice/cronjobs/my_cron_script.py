#!/usr/bin/env python3

# my_cron_script.py

"""
Goal: Run 10 times then skip.

1st Time: Normally
2nd Time: Normally
3rd Time: Delay 2 minutes
4th Time: Normally
5th Time: Delay 5 minutes
6th Time: Normally
7th Time: Normally
8th Time: Delay 1 minute
9th Time: Normally
10th Time: Skip

Expected:
First 1 will happen, then 2, then 4, then 6, then 7, then 9, then 10, maybe then 8, then 3, then 5

"""
from datetime import datetime
import time

global_count_file = "/home/ankit/MyFiles/self_practice/python_prac/general_practice/cronjobs/global_count.txt"

with open(global_count_file, "r") as f:
    try:
        count = int(f.read())
    except ValueError:
        count = 0

count += 1

if count == 3:
    time.sleep(2 * 60)
elif count == 5:
    time.sleep(5 * 60)
elif count == 8:
    time.sleep(1 * 60)
else:
    pass

if count <= 10:
    with open(
        "/home/ankit/MyFiles/self_practice/python_prac/general_practice/cronjobs/cron_log.txt",
        "a",
    ) as f:
        f.write(f"Cron ran at: {datetime.now()} for {count} times\n\n")

    with open(global_count_file, "w") as f:
        f.write(str(count))
else:
    with open(
        "/home/ankit/MyFiles/self_practice/python_prac/general_practice/cronjobs/cron_log.txt",
        "a",
    ) as f:
        f.write(f"Cron has run for 10 times, skipping.\n\n")
# print("Cron script executed successfully.")
