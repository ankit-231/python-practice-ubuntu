# from utils import get_relevant_data_from_beautiful_soup
"__THIS_IS_OLD_CODE_DJANGO_TRY_HAS_UPDATED_CODE"

from utils import get_data_from_web


file_name = "web_scraping/nepalgramproducts/nepalgramproducts.csv"
url = "https://nepalgramodhyog.store/productdetails/5237/better-mansion-water-bottle/"

get_data_from_web(file_name=file_name, url=url)
