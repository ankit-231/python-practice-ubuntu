marks = [
    68,
    70,
    81,
    90,
    94,
    75,
    78,
    70,
    67,
    68,
    75,
    83,
    70,
    55,
    77,
    67,
    68,
]

credits = [
    15,
    30,
    15,
    30,
    30,
    15,
    15,
    30,
    15,
    15,
    15,
    15,
    30,
    30,
    30,
    15,
    15,
]

# print(len(marks) == len(credits))
# mark_credit_li = []
# for mark, credit in zip(marks, credits):
#     mark_credit_di = {}
#     mark_credit_di["mark"] = mark
#     mark_credit_di["credit"] = credit
#     mark_credit_li.append(mark_credit_di.copy())

# print(mark_credit_li)

mark_credit_di = [
    {"mark": 68, "credit": 15},
    {"mark": 70, "credit": 30},
    {"mark": 81, "credit": 15},
    {"mark": 90, "credit": 30},
    {"mark": 94, "credit": 30},
    {"mark": 75, "credit": 15},
    {"mark": 78, "credit": 15},
    {"mark": 70, "credit": 30},
    {"mark": 67, "credit": 15},
    {"mark": 68, "credit": 15},
    {"mark": 75, "credit": 15},
    {"mark": 83, "credit": 15},
    {"mark": 70, "credit": 30},
    {"mark": 55, "credit": 30},
    {"mark": 77, "credit": 30},
    {"mark": 67, "credit": 15},
    {"mark": 68, "credit": 15},
]

cum_mark_times_credit = 0
cum_credit = 0
for mark_credit in mark_credit_di:
    mark_times_credit = mark_credit["mark"] * mark_credit["credit"]
    cum_mark_times_credit += mark_times_credit
    cum_credit += mark_credit["credit"]

weighted_percentage_average = cum_mark_times_credit / cum_credit


print("weighted_percentage_average", weighted_percentage_average)
