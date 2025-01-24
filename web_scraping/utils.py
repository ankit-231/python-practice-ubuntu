import requests
from bs4 import BeautifulSoup

SAVE_HTML_TO_FILE = False
LOAD_HTML_FROM_FILE = True

FIRST_ROW = [
    "product_name",
    "product_description",
    "brand",
    "product_subcategory",
    "pieces",
    "product_image",
    "unit_measure",
    "minimum_qty",
    "maximum_qty",
    "PRDWeight",
    "PRDPrice",
    "sku",
    "threshold_limit",
    "available",
    "is_featured",
    "variants",
    "nepali_name",
    "nepali_description",
    "extra_description",
]


def create_new_csv_file(unique_name: str):
    file_name = f"web_scraping/nepalgramproducts/{unique_name}.csv"
    with open(file_name, "w") as f:
        f.write(get_csv_first_row())


def set_values(
    file_name,
    product_name,
    product_description,
    PRDPrice,
    brand="",
    product_subcategory="",
    pieces=1,
    product_image="",
    unit_measure="gm",
    minimum_qty=1,
    maximum_qty=10,
    PRDWeight=10,
    sku="",
    threshold_limit=5,
    available=10,
    variants="",
    is_featured=False,
    nepali_name="",
    nepali_description="",
    extra_description="",
):
    final_li = [
        product_name,
        product_description,
        brand,
        product_subcategory,
        pieces,
        product_image,
        unit_measure,
        minimum_qty,
        maximum_qty,
        PRDWeight,
        PRDPrice,
        sku,
        threshold_limit,
        available,
        is_featured,
        variants,
        nepali_name,
        nepali_description,
        extra_description,
    ]
    final_li = map(str, final_li)
    with open(file_name, "a") as f:
        f.write(",".join(final_li) + "\n")


def get_app_product_attributes_as_string():
    return ",".join(FIRST_ROW)


def get_csv_first_row():
    return get_app_product_attributes_as_string() + "\n"


def get_relevant_data_from_beautiful_soup(soup: BeautifulSoup):
    main_content = soup.find("div", {"class": "main_content"})
    container = main_content.find("div", {"class": "container"})
    product_description_div = container.find("div", {"class": "product_description"})
    # print(product_description_div)
    product_name = (
        product_description_div.find("h4", {"class": "product_title"}).find("a").text
    )
    PRDPrice = product_description_div.find("span", {"class": "price"}).text
    product_description = (
        product_description_div.find("div", {"class": "pr_desc"}).find("p").text
    )
    product_meta = container.find("ul", {"class": "product-meta"})
    product_meta_list = [li.text for li in product_meta.find_all("li")]

    # required data
    product_name = product_name.strip()
    PRDPrice = PRDPrice.split(" ")[1].strip()
    brand = get_brand(product_description)
    sku = get_sku(product_meta_list)
    main_prod_description_div = container.find("div", {"id": "Description"})
    main_prod_description = main_prod_description_div.find("p").text
    main_prod_description = (
        main_prod_description.strip().replace("\n", " ").replace(",", "")
    )
    print("product_name: ", product_name)
    print("PRDPrice: ", PRDPrice)
    print("brand: ", brand)
    print("sku: ", sku)
    print("main_prod_description: ", main_prod_description)
    return {
        "product_name": product_name,
        "PRDPrice": PRDPrice,
        "brand": brand,
        "sku": sku,
        "product_description": main_prod_description,
    }


def get_sku(product_meta_list: list[str]) -> str:
    for item in product_meta_list:
        if "SKU" in item:
            return item.split(":")[1].strip()
    return ""


def get_brand(product_description: str) -> str:
    for line in product_description.split("\n"):
        if "Mfg" in line:
            return line.split(":")[1].strip()
    return ""


# create_new_csv_file("nepalgramproducts")


def get_data_from_web(file_name: str, url: str):
    # url = "https://nepalgramodhyog.store/productdetails/152/wai-wai-100%25-veg-instant-noodles-75-gm/"
    # url = (
    #     "https://nepalgramodhyog.store/productdetails/5237/better-mansion-water-bottle/"
    # )

    soup = None

    if LOAD_HTML_FROM_FILE:
        with open("web_scraping/product_soup.html", "r") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
    else:
        # Create a session to manage cookies automatically
        session = requests.Session()

        # Define headers to mimic a web browser (you can customize this)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
        }

        # Set these headers in the session, so they are automatically used in all requests
        session.headers.update(headers)

        # Make a request to a page
        response = session.get(url)
        # response = session.post(url, data={})

        # Check if the request was successful
        if response.status_code == 200:

            if SAVE_HTML_TO_FILE:
                with open("web_scraping/product_soup.html", "w", encoding="utf-8") as f:
                    f.write(response.text)

            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")

            # Example: Print the title of the page
            # print(soup.title.text)

        else:
            # print(response.text)
            print(f"Request failed with status code {response.status_code}")

    if soup is None:
        print("No soup found")
        return

    relevant_data = get_relevant_data_from_beautiful_soup(soup)

    set_values(file_name=file_name, **relevant_data)
