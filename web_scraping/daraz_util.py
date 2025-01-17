from bs4 import BeautifulSoup
import requests


def get_brand_from_url(url):
    # Send a GET request to the website
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.121 Safari/537.36"
    }
    # url = "https://www.daraz.com.np/products/wood-pepper-grinder-20-cm-1-pc-i108727407.html"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    with open("web_scraping/soup.html", "w") as f:
        f.write(str(soup))


url = "https://www.daraz.com.np/products/wood-pepper-grinder-20-cm-1-pc-i108727407.html"
get_brand_from_url(url)
