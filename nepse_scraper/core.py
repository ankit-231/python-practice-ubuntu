from nepse_scraper import Nepse_scraper


request_obj = Nepse_scraper()
# get last trading date's price
value = request_obj.get_today_price()

# print(value)


with open("nepse_scraper/nepse_data.json", "w") as f:
    f.write(str(value))
## or
# get's price of provided date
# Note: nepse only gives access data from today date and one year prior
## example: if today date is '2023-05-07' you can scrape data from '2022-05-07 to '2023-05-07'
# value = request_obj.get_today_price("2023-05-07")
