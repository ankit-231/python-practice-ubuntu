# german_tools/auto_add_from_leo.py

from .leo_scraper import scrape_leo
from .anki import add_note, invoke, store_audio_in_anki

from .download_german_audio import download_audio, generate_full_path_with_extension

DECK_NAME = "Learning German"
MODEL_NAME = "Basic"


def main():

    word = input("Enter Word: ")

    print("\nsearching...\n")

    result = scrape_leo(word)

    if not result:
        print("Word not found on LEO.")
        return

    english = result["english"]
    german = result["german"]
    audio_url = result["audio_url"]

    print("Word found:")
    print("english name:", english)
    print("german name:", german)
    print("audio_url:", audio_url)

    print("\nWhat do you want to do next:")
    print("1 → add directly to anki (enter)")
    print("2 → add back_extra then add")
    print("3 → edit manually then add")

    choice = input("> ").strip()

    back_extra = ""

    if choice == "2":
        back_extra = input("Back Extra: ")

    elif choice == "3":

        english = input(f"English [{english}]: ") or english
        german = input(f"German [{german}]: ") or german
        back_extra = input("Back Extra: ")

    audio_filename = ""

    if audio_url:
        full_path = generate_full_path_with_extension(german, audio_url)
        print(full_path)
        download_audio(audio_url, full_path)
        audio_filename = store_audio_in_anki(full_path)
        print(audio_filename)

    note_id = add_note(
        deck_name=DECK_NAME,
        model_name=MODEL_NAME,
        front=english,
        back=german,
        back_extra=back_extra,
        audio_filename=audio_filename,
    )

    print("\nNote added.")
    print("Note ID:", note_id)


if __name__ == "__main__":
    main()
