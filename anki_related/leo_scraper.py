# german_tools/leo_scraper.py

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://dict.leo.org/",
}


def scrape_leo(word: str):
    url = f"https://dict.leo.org/german-english/{word}"

    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")

    row = soup.select_one('tr[data-dz-ui="dictentry"]')

    if not row:
        return None

    cells = row.select("td")

    if len(cells) < 8:
        return None

    english = " ".join(cells[4].get_text(" ", strip=True).split())
    german = " ".join(cells[7].get_text(" ", strip=True).split())

    # Audio
    audio_tags = row.select("[data-dz-rel-audio]")

    audio_url = None

    if audio_tags:
        audio_id = audio_tags[-1]["data-dz-rel-audio"]
        audio_url = f"https://dict.leo.org/media/audio/{audio_id}.ogg"

    return {
        "english": english,
        "german": german,
        "audio_url": audio_url,
    }
