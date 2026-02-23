import json

DATA_FILE = "rsi/daily_rsi_response.json"


def extract_rsi_from_my_response(json_file):

    all_data = json.load(open(json_file, "r"))

    print(all_data["results"])

    results_from_response = all_data["results"]

    results = []

    for key, value in results_from_response.items():
        results.append({"symbol": key, "rsi_14_daily": value["rsi"]})

    return results
