import requests
from bs4 import BeautifulSoup, ResultSet, Tag

# Base URL with search query
# url = "https://www.daraz.com.np/catalog/?q=sugar"
q = "salt"
url = f"https://www.daraz.com.np/catalog/?ajax=true&isFirstRequest=true&page=1&q={q}"

# Send a GET request to the website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.121 Safari/537.36"
}

# headers = {
#     ":authority": "www.daraz.com.np",
#     ":method": "GET",
#     ":path": "/catalog/?ajax=true&isFirstRequest=true&page=1&q=sugar",
#     ":scheme": "https",
#     "accept": "application/json, text/plain, */*",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "en-GB,en;q=0.9,ne-NP;q=0.8,ne;q=0.7,en-US;q=0.6",
#     "bx-v": "2.5.28",
#     "cache-control": "no-cache",
#     "cookie": "__wpkreporterwid_=cc158c60-beaf-4997-3c56-87696604731c; lzd_cid=b3bc75c8-0be0-4a41-df66-5669be58f8e7; t_uid=b3bc75c8-0be0-4a41-df66-5669be58f8e7; t_fv=1715925528067; lwrid=AQGPhSGvC1eFUQjx64tr2RoAAAAA; cna=GeDNHvnztnoCASb9Q8TgFTGU; cto_bundle=ncHzuV96NGdSTnolMkZsV3F2MllIcjFjUzlUbVRKRHlGb2VrRjZ4JTJCJTJCdUp0eUZVa0x2c0dkTW84NmxTQWh2UUklMkI3SzNzTTE2UTVkVDcxQ3VFWVI5a3piaW9leG9PNGc2c0glMkJESnNUTnVqclBtRTNkMmYlMkJHOHNHWGpQQnlRM2olMkY2blF1SzVySE1XYjZjU0tKNjl1RUp0MGhTeUhEUSUzRCUzRA; G_ENABLED_IDPS=google; __itrace_wid=7b572ddd-6344-46ef-217f-f8689e237bd3; _gcl_au=1.1.211716096.1733813751; _ga=GA1.3.1879525450.1715925531; isg=BF1dbG-M5pTvHoOWfch8d4mDbDBXepHMDMURLh8jzbSi1nUI48m6nPeFANJQUamE; _ga_GEHLHHEXPG=GS1.1.1734927381.17.1.1734927424.17.0.0; hng=NP|en-NP|NPR|524; hng.sig=CpTPf0oy-Ji7yHXlTqu1ZBr2yy4DEw3ATHLSHmIgtyk; xlly_s=1; t_sid=2xdmy1nKhxsk7Uyzsy2SM7sifxtnd3iF; utm_channel=NA; lzd_sid=1a85877415f4cf32f936377eff3142d8; _tb_token_=7e7ebe1e5055e; _m_h5_tk=76ff9bbdc5b20fbc413d76ff2b53eda7_1737100328943; _m_h5_tk_enc=7987a05eeb23247b5ee37caf7650c8f0; lwrtk=AAEEZ4pcUAsi7entPM+WGsVDcJjD8U1n/rvFVM3Fdhdh1pI/Q1snFgU=; epssw=7*3Udss6Mx9s2s0sdjGw8vssEjJpeLOXsSlabxe8W70mFLvIFarRM02vIb1OxvZJWj76ss7BmIsE3sGU6f46uKhs3Wv_1Kssssssssss3usz6sdr4A-l36jNfvSpGYsRVv9Imvssp66keBPK3Jr-cXQQrRoDk5f08ZMjr5f_tfeMfHCUsPUCwgIdHqVbG6h31pJrnt6xjuSj_OOWf-PPxtIijkI6uJb2nauEIf-4qkckzuaijdS00JS2hsOJfP-aDuusRhY-9QG74CORaZ3x1VugdyfPdyovpPVLS43_6hiOJXO-HXJRrVEKeT81YhLvCXXVayZuBygRrbE3OF62ou1sIQSxjhua0I6xjwsh6sSxUG3KVJGZ0N3K6sLs3FOdfbRiqhalfy; tfstk=fgJMlkM-g7qjQx4GVXXsNne5nOhd1P6foEeAktQqTw7QWPe90iXDmEqAgV69nBYH0NJt1ZBmme857Exjfi72uEbv6XHJfh6f34LmeYKsnHbGpdX4kH8lodgtyYHJbfS1HHuJBBXar_sV3G5V79oh4iW4QZ8V86SP2PWV33StpXdSULiGwa4eO_5NkW5Ozh7HkEpFjzQybw2439IGsfKN--y2LBOQwEQmLzbXLEXP3_q-Sh6hJUjJWvyMrn-Wg6v08qbwBh8hwC0uIUY10H5HWmFfxIx2FO6oaS6DvpfJitDQANRW9FSHvoNHAsSztWPPn5efYmpUGS1NAMbRWKjWoQlq5Uonx7G1_MstyDm3GS1NAMb-xDV7j1SCX4C..",
#     "pragma": "no-cache",
#     "priority": "u=1, i",
#     "referer": "https://www.daraz.com.np/",
#     "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": '"Linux"',
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin",
#     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
#     "x-csrf-token": "7e7ebe1e5055e",
# }


response = requests.get(url, headers=headers)
print("HI", response.status_code)
# Check if the request was successful
if response.status_code == 200:
    json_value = response.json()
    products = json_value["mods"]["listItems"]
    print("Total Products", len(products))
    for product in products:
        with open("web_scraping/products.csv", "a") as f:
            name = product["name"]
            price = product["price"]
            originalPrice = product["originalPrice"] if "originalPrice" in product else "No Original Price"
            image = product["image"]
            itemUrl = product["itemUrl"]
            f.write(f"{name},{price},{originalPrice},{image}\n")

    # Parse the HTML content
    # soup = BeautifulSoup(response.content, "html.parser")
    # with open("web_scraping/output.html", "w", encoding="utf-8") as f:
    #     f.write(soup.prettify())

    # Find all product listings
    # products = soup.find_all("div", class_="Ms6aG")

    # if not products:
    #     print("No products found.")
    #     exit()

    # for product in products:
    #     # Extract the product name
    #     product_name_div = product.find("div", class_="RfADt")
    #     product_name_anchor = product_name_div.find("a")
    #     name = (
    #         product_name_anchor.get_text(strip=True)
    #         if product_name_div
    #         else "No name found"
    #     )

    #     # Extract the product image
    #     image_tag = product.find("img", type="product")
    #     image_url = image_tag["src"] if image_tag else "No image URL found"

    # print(f"Name: {name}")
    # print(f"Image URL: {image_url}")
    # print("-" * 50)
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")
