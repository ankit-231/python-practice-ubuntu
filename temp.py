from datetime import datetime


def temp():
    utc_time = "2025-10-19 12:48:10.047 +0545"
    # local_time =


def remove_all_occurrences(lst: list, value: object) -> list:
    """
    removes in place from the list all occurrences of the value
    """
    while value in lst:
        lst.remove(value)


def shares():
    all_shares = [
        "SYPNL",
        "SAGAR",
        "SYPNL",
        "BANDIPUR",
        "DHEL",
        "BANDIPUR",
        "SAGAR",
        "DHEL",
        "RNLI",
        "BHDC",
        "KBLPO",
        "KBL",
        "RNLI",
        "HRL",
        "VLUCL",
        "RNLI",
        "BHDC",
        "MBJC",
    ]

    remove_all_occurrences(all_shares, "KBLPO")
    remove_all_occurrences(all_shares, "KBL")

    unique_shares = list(set(all_shares))
    print(unique_shares)
    print(len(unique_shares))
    # ['RNLI', 'DHEL', 'BHDC', 'BANDIPUR', 'SYPNL', 'SAGAR', 'VLUCL', 'MBJC', 'HRL']


if __name__ == "__main__":
    shares()
