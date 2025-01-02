import csv

file_path = "module-results.csv"

with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    scores = []
    for row in reader:
        # print(row)
        scores.append(int(row[4]))  # score is the 5th column

    avg_score = sum(scores) / len(scores)
    print(f"Average score: {avg_score}")

# import os

# print("Files in current directory:")
# for file in os.listdir():
#     print(file)
