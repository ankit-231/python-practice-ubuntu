from datetime import datetime
import json
import os
import time
from nepse import Nepse

# Constants
REQUEST_WAIT_TIME = 10  # seconds between API calls
DATA_DIR = "nepse_scraper/main_data"
LOG_DIR = "nepse_scraper/main_data/logs"
LOG_FILE = os.path.join(LOG_DIR, "data_fetching.log")
PAGE_SIZE = 100
TOTAL_PAGES_TO_FETCH = 2  # pages: 0 and 1

# Setup Nepse API
nepse = Nepse()
nepse.setTLSVerification(False)

# Ensure output directories exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# Load stock list
with open("nepse_scraper/company_data.json", "r") as f:
    all_stocks = json.load(f)

# Filter only active stocks
active_stocks = [stock for stock in all_stocks if stock.get("status") == "A"]

# Limit for testing
stocks_to_process = active_stocks[:3]


# Logging helper
def log_message(message: str):
    with open(LOG_FILE, "a") as log_f:
        log_f.write(message + "\n")


# Processing loop
for stock in stocks_to_process:
    stock_id = stock["id"]
    stock_symbol = stock["symbol"]
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Stock folder
    stock_dir = os.path.join(DATA_DIR, stock_symbol)
    os.makedirs(stock_dir, exist_ok=True)

    log_message(
        f"--------------- Starting to fetch data for {stock_symbol} at {start_time} ---------------"
    )
    log_message(f"symbol: {stock_symbol}")
    log_message(f"id: {stock_id}")

    all_dates = []

    for page_num in range(TOTAL_PAGES_TO_FETCH):
        try:
            stock_price_history = nepse.requestGETAPI(
                f"/api/nots/market/security/price/{stock_id}?page={page_num}&size={PAGE_SIZE}"
            )

            content = stock_price_history.get("content", [])

            if not content:
                log_message(f"start_date_for_page_{page_num}: null")
                log_message(f"end_date_for_page_{page_num}: null")
                log_message(f"file_path_for_page_{page_num}: null")
                log_message(
                    f"data_fetch_status_for_page_{page_num}: not fetched - page does not exist for this stock"
                )
                continue

            # Extract dates
            dates = [
                entry["businessDate"] for entry in content if "businessDate" in entry
            ]
            page_start_date = min(dates)
            page_end_date = max(dates)

            log_message(f"start_date_for_page_{page_num}: {page_start_date}")
            log_message(f"end_date_for_page_{page_num}: {page_end_date}")

            # Keep track for overall range
            all_dates.extend(dates)

            # Save page file
            output_path = os.path.join(stock_dir, f"page_{page_num}.json")
            with open(output_path, "w") as f:
                json.dump(stock_price_history, f, indent=4)

            log_message(f"file_path_for_page_{page_num}: {output_path}")
            log_message(f"data_fetch_status_for_page_{page_num}: success")

        except Exception as e:
            log_message(f"start_date_for_page_{page_num}: null")
            log_message(f"end_date_for_page_{page_num}: null")
            log_message(f"file_path_for_page_{page_num}: null")
            log_message(
                f"data_fetch_status_for_page_{page_num}: failed with exception - {str(e)}"
            )

    # Overall date range
    if all_dates:
        log_message(f"overall_start_date: {min(all_dates)}")
        log_message(f"overall_end_date: {max(all_dates)}")
    else:
        log_message(f"overall_start_date: null")
        log_message(f"overall_end_date: null")

    end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message(
        f"--------------- Finished fetching data for {stock_symbol} at {end_time} ---------------\n"
    )

    time.sleep(REQUEST_WAIT_TIME)
