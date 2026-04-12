from .leo_scraper import scrape_leo
import json
import time

words = [
    "anfangen",
    "anziehen",
    "aufhören",
    "aufmachen",
    "aufräumen",
    "aufstehen",
    "bedienen",
    "beschreiben",
    "bringen",
    "dürfen",
    "duschen",
    "einkaufen",
    "einladen",
    "feiern",
    "fernsehen",
    "fotografieren",
    "frühstücken",
    "holen",
    "kontrollieren",
    "können",
    "messen",
    "mitbringen",
    "mitkommen",
    "müssen",
    "ordnen",
    "Rad fahren",
    "rauchen",
    "schlafen",
    "schneiden",
    "schwimmen",
    "sehen",
    "spazieren gehen",
    "stattfinden",
    "stören",
    "tanzen",
    "treffen",
    "vergessen",
    "vergleichen",
    "vorbereiten",
    "vorhaben",
    "zeichnen",
    "zuhören",
    "Abend",
    "Ansichtskarte",
    "Arbeit",
    "Ausflug",
    "Bäcker",
    "Bank",
    "Bar",
    "Bibliothek",
    "Buch",
    "Café",
    "Diskothek",
    "Donnerstag",
    "Dusche",
    "Eintritt",
    "Essen",
    "Fernsehen",
    "Fieber",
    "Film",
    "Freitag",
    "Freizeit",
    "Friseurin",
    "Friseur",
    "Gast",
    "Gruß",
    "Juli",
    "Kellnerin",
    "Kellner",
    "Kino",
    "Kleid",
    "Konzert",
    "Krankenhaus",
    "Krankenschwester",
    "Lehrerin",
    "Lehrer",
    "Mannschaft",
    "Maschine",
    "Meer",
    "Mensch",
    "Mittag",
    "Mittagessen",
    "Mittwoch",
    "Montag",
    "Musik",
    "Passagier",
    "Pause",
    "Restaurant",
    "Samstag",
    "Satz",
    "Schild",
    "Schwimmbad",
    "Situation",
    "Sonnabend",
    "Sonnenbad",
    "Sonntag",
    "Spaziergang",
    "Tanz",
    "Torte",
    "Uhrzeit",
    "Verband",
    "Viertel",
    "Vortrag",
    "Wohnung",
    "Zeitung",
    "Zigarette",
    "früh",
    "geöffnet",
    "geschlossen",
    "herrlich",
    "herzlich",
    "leise",
    "lieb",
    "nächst",
    "nett",
    "obligatorisch",
    "spät",
    "verboten",
]

data = []

for w in words:
    print("Scraping:", w)
    result = scrape_leo(w)

    if result:
        data.append(result)

    time.sleep(1)  # avoid blocking

    # save to temporary file just in case something goes wrong
    with open("temp_german_words.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


with open("german_words.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved german_words.json")

# JUST RUN THE index.html file with Go Live Server extension in VS Code to see the result in browser.
