from bs4 import BeautifulSoup

HTML_TABLE_FILE = "rsi/nepsealpha_rsi_table.html"


def extract_rsi_from_nepsealpha_html_table(html_table_file):
    with open(html_table_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    results = []

    table = soup.find("table")
    for row in table.find_all("tr"):
        cells = row.find_all("td")

        # skip rows without enough columns (headers, empty rows, etc.)
        if len(cells) < 10:
            continue

        # 1st column: Symbol
        symbol = cells[0].get_text(strip=True)

        # 10th column: RSI 14
        rsi_14 = cells[9].get_text(strip=True)

        results.append({"symbol": symbol, "rsi_14_daily": rsi_14})

    return results
