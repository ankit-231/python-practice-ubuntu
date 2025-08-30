from datetime import date, datetime
import json
import os
from nepse import Nepse
import tqdm
import tqdm.asyncio


class NepseCustom(Nepse):
    def getFloorSheetOfDate(self, date_: date | None = None, show_progress=False):

        if not date_:
            date_ = date.today()

        date_string = date_.strftime("%Y-%m-%d")

        date_string = "2025-08-12"

        url = f"{self.api_end_points['floor_sheet']}?&size={self.floor_sheet_size}&businessDate=2025-08-12&sort=contractId,desc"
        sheet = self.requestPOSTAPI(
            url=url, payload_generator=self.getPOSTPayloadIDForFloorSheet
        )
        floor_sheets = sheet["floorsheets"]["content"]
        max_page = sheet["floorsheets"]["totalPages"]
        page_range = (
            tqdm.tqdm(range(1, max_page)) if show_progress else range(1, max_page)
        )
        for page_number in page_range:
            current_sheet = self.requestPOSTAPI(
                url=f"{url}&page={page_number}",
                payload_generator=self.getPOSTPayloadIDForFloorSheet,
            )
            current_sheet_content = current_sheet["floorsheets"]["content"]
            floor_sheets.extend(current_sheet_content)
        return floor_sheets


nepse = NepseCustom()
nepse.setTLSVerification(
    False
)  # This is temporary, until nepse sorts its ssl certificate problem


# company_list = nepse.getCompanyList()

# with open("nepse_scraper/company_data.json", "w") as f:
#     company_list_json = json.dumps(company_list)
#     f.write(company_list_json)


# hrl_price_volume_history = nepse.getCompanyPriceVolumeHistory("HRL")

# with open("nepse_scraper/hrl_price_volume_history.json", "w") as f:
#     hrl_price_volume_history_json = json.dumps(hrl_price_volume_history)
#     f.write(hrl_price_volume_history_json)

# hrl_price_volume_history_filtered = nepse.getCompanyPriceVolumeHistory(
#     "HRL", start_date=date(2024, 1, 9), end_date=date(2025, 1, 1)
# )

# with open("nepse_scraper/hrl_price_volume_history_filtered.json", "w") as f:
#     hrl_price_volume_history_json = json.dumps(hrl_price_volume_history_filtered)
#     f.write(hrl_price_volume_history_json)


# hrl_full_data = nepse.requestGETAPI("/api/nots/market/security/price/9234")

# with open("nepse_scraper/hrl_full_data.json", "w") as f:
#     hrl_full_data_json = json.dumps(hrl_full_data)
#     f.write(hrl_full_data_json)


# stock_price_history = nepse.requestGETAPI(
#     f"/api/nots/market/security/price/{8066}?page=1&size=10"
# )

# with open(f"nepse_scraper/{stock_symbol}.json", "w") as f:
#     stock_price_history_json = json.dumps(stock_price_history)
#     f.write(stock_price_history_json)

# data = nepse.requestGETAPI("/api/nots/market/security/price/8066?page=1&size=100")

# print(data)
# with open(f"nepse_scraper/temp_data.json", "w") as f:
#     stock_price_history_json = json.dumps(data)
#     f.write(stock_price_history_json)

# floorsheet = nepse.getFloorSheet()

# with open("nepse_scraper/floorsheet.json", "w") as f:
#     floorsheet_json = json.dumps(floorsheet)
#     f.write(floorsheet_json)


today_date = date(2025, 8, 12)
floorsheet = nepse.getFloorSheetOfDate(date_=today_date)
floorsheet_dir = f"nepse_scraper/main_data/daily_data/{today_date}/floorsheet"
floorsheet_file = f"{floorsheet_dir}/floorsheet.json"
os.makedirs(floorsheet_dir, exist_ok=True)

with open(floorsheet_file, "w") as f:
    floorsheet_json = json.dumps(floorsheet)
    f.write(floorsheet_json)
    print(floorsheet_file, "written")
