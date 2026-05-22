from bs4 import BeautifulSoup

HTML_FILE = "general/university_modules/files/modules_table.html"


def main():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    table = soup.find("table")
    if not table:
        print("No table found")
        return

    modules = []

    for row in table.select("tbody tr"):
        td = row.find("td")
        if not td:
            continue

        # Extract code + title
        title_div = td.find("div", class_="studip-course-title")
        if title_div:
            link = title_div.find("a")
            full_text = (
                link.get_text(strip=True) if link else title_div.get_text(strip=True)
            )

            # Usually the code is at the beginning, like "5487UE AI-Driven Software Development"
            parts = full_text.split(maxsplit=1)
            code = parts[0] if parts else ""
            name = parts[1] if len(parts) > 1 else full_text
        else:
            code = name = ""

        # Extract dates
        dates_div = td.find("div", class_="studip-course-dates")
        dates = dates_div.get_text(strip=True) if dates_div else ""

        # Extract lecturers
        lecturers = []
        for lec in td.select("div.studip-course-lecturer a"):
            lecturers.append(lec.get_text(strip=True))

        modules.append(
            {
                "code": code,
                "name": name,
                "dates": dates,
                "lecturers": lecturers,
                "raw_title": full_text,
            }
        )

    print(f"Total modules found: {len(modules)}\n")
    for m in modules[:5]:  # print first 5 as example
        print(m)


if __name__ == "__main__":
    main()
