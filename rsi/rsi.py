import json
from extract_rsi_from_my_response import extract_rsi_from_my_response
from extract_rsi_from_nepsealpha_html_table import (
    extract_rsi_from_nepsealpha_html_table,
)


"""
[
    {
        "symbol": "symbol_name",
        "rsi_14_daily": "rsi_value"
    }
]
"""

# CONSTANTS
# =================================================================================

NEPSEALPHA_TABLE_HTML_FILE = "rsi/nepsealpha_rsi_table.html"

MY_RESPONSE_DATA_FILE = "rsi/daily_rsi_response.json"

BAD_SYMBOL_OUTPUT_FILE = "rsi/bad_symbols.json"

MAX_ALLOWED_RSI_DIFF = 5

# =================================================================================


rsi_list_from_nepsealpha = extract_rsi_from_nepsealpha_html_table(
    NEPSEALPHA_TABLE_HTML_FILE
)

rsi_list_from_my_response = extract_rsi_from_my_response(MY_RESPONSE_DATA_FILE)


# Build lookup dicts keyed by symbol
nepsealpha_map = {
    item["symbol"]: item["rsi_14_daily"] for item in rsi_list_from_nepsealpha
}

my_response_map = {
    item["symbol"]: item["rsi_14_daily"] for item in rsi_list_from_my_response
}


# Intersection + merge
refined_rsi_list = []

for symbol in nepsealpha_map.keys() & my_response_map.keys():
    refined_rsi_list.append(
        {
            "symbol": symbol,
            "rsi_from_me": my_response_map[symbol],
            "rsi_from_nepsealpha": nepsealpha_map[symbol],
        }
    )

print(refined_rsi_list)


def to_float(rsi_str: str | float | int) -> float:
    if isinstance(rsi_str, float) or isinstance(rsi_str, int):
        return rsi_str
    return float(rsi_str.replace("%", "").strip())


common_symbols = []
symbols_exceeding_threshold = []


for item in refined_rsi_list:
    rsi_me = to_float(item["rsi_from_me"])
    rsi_nepsealpha = to_float(item["rsi_from_nepsealpha"])

    diff = abs(rsi_me - rsi_nepsealpha)

    data = {
        "symbol": item["symbol"],
        "rsi_from_me": rsi_me,
        "rsi_from_nepsealpha": rsi_nepsealpha,
        "difference": round(diff, 2),
    }

    common_symbols.append(data)

    if diff > MAX_ALLOWED_RSI_DIFF:
        symbols_exceeding_threshold.append(data)

# print(symbols_exceeding_threshold)


with open(BAD_SYMBOL_OUTPUT_FILE, "w") as f:
    f.write(json.dumps(symbols_exceeding_threshold, indent=4))

# print(len(symbols_exceeding_threshold))

bad_symbols_percentage = len(symbols_exceeding_threshold) / len(common_symbols) * 100

print("Bad symbols percentage:", bad_symbols_percentage, "%")

# print(symbols_exceeding_threshold)
