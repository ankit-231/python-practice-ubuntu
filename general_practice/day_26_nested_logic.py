from datetime import date

# 31 8 2004
# 20 1 2004
# 3500

# 24 12 1898
# 18 9 1898
# 1500


def get_returned_date():
    returned_date = input().strip()
    # returned_date = "24 12 1898".strip()
    d, m, y = map(int, returned_date.split(" "))
    return date(y, m, d)


def get_due_date():
    due_date = input().strip()
    # due_date = "18 9 1898".strip()
    d, m, y = map(int, due_date.split(" "))
    return date(y, m, d)


def get_fine(returned_date: date, due_date: date):
    days_late = get_days_late(returned_date, due_date)
    months_late = get_months_late(returned_date, due_date)
    if returned_date <= due_date:
        return 0
    # if the first condition is false, returned_date is always greater than due_date so days_late >= 1
    if returned_date.month == due_date.month and returned_date.year == due_date.year:
        return days_late * 15
    if returned_date.year == due_date.year:
        return months_late * 500
    return 10000


def get_days_late(returned_date: date, due_date: date):
    sub = returned_date - due_date
    return sub.days


def get_months_late(returned_date: date, due_date: date):
    days = get_days_late(returned_date, due_date)
    return days // 30


if __name__ == "__main__":
    returned_date = get_returned_date()
    due_date = get_due_date()
    fine = get_fine(returned_date, due_date)
    print(fine)
