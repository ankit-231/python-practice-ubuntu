import os
import requests
from bs4 import BeautifulSoup, ResultSet, Tag

# Base URL with search query
# url = "https://www.daraz.com.np/catalog/?q=sugar"
queries = ["salt", "sugar", "mustard+oil"]

for q in queries:
    # q = "salt"
    url = (
        f"https://www.daraz.com.np/catalog/?ajax=true&isFirstRequest=true&page=1&q={q}"
    )

    # Send a GET request to the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.121 Safari/537.36"
    }
    file_name = f"web_scraping/products/{q}.csv"
    # reset the file
    with open(file_name, "w") as f:
        f.write("name,price,originalPrice,brandName,image,itemUrl\n")

    response = requests.get(url, headers=headers)
    print("HI", response.status_code)
    # Check if the request was successful
    if response.status_code == 200:
        json_value = response.json()
        products = json_value["mods"]["listItems"]
        print("Total Products", len(products))
        for product in products:
            with open(file_name, "a") as f:
                name = product["name"]
                price = product["price"]
                originalPrice = (
                    product["originalPrice"]
                    if "originalPrice" in product
                    else "No Original Price"
                )
                brandName = product["brandName"]
                image = product["image"]
                itemUrl = "https:" + product["itemUrl"]
                f.write(
                    f"{name},{price},{originalPrice},{brandName},{image},{itemUrl}\n"
                )

    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")
