"""
This script works with https://dict.leo.org/german-english/der%20Tag this website flawlessly.
"""

import base64
import os
import time

import requests

# BASE_FILE_DIR = "files/german-audio"
BASE_FILE_DIR = "/home/ankit/MyFiles/Germany/German/Words and Phrases"

session = requests.Session()

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)",
    "Referer": "https://dict.leo.org/german-english/",
}


def prepare_session(word):
    """Visit LEO page first to set cookies"""
    url = f"https://dict.leo.org/german-english/{word}"
    session.get(url, headers=HEADERS, timeout=10)


def download_audio(url, filename, retries=2):
    for attempt in range(retries):
        response = session.get(url, headers=HEADERS, stream=True, timeout=15)
        response.raise_for_status()

        total = 0
        with open(filename, "wb") as f:
            for chunk in response.iter_content(8192):
                if chunk:
                    total += len(chunk)
                    f.write(chunk)

        if total > 0:
            print("Downloaded:", filename)
            return

        print("Empty file, retrying...")
        time.sleep(1)

    raise Exception("Download failed after retries")


MUSIC_FILE_EXTENSIONS = [
    # Lossy
    "mp3",
    "aac",
    "m4a",
    "ogg",
    "opus",
    "wma",
    "mpc",
    "amr",
    "ra",
    "rm",
    "ac3",
    "dts",
    # Lossless
    "wav",
    "aiff",
    "aif",
    "flac",
    "alac",
    "ape",
    "wv",
    "tta",
    "tak",
    "m4a",
    # Uncompressed
    "pcm",
    "bwf",
    # MIDI
    "mid",
    "midi",
    "kar",
    "rmi",
    # Tracker / Module
    "mod",
    "xm",
    "it",
    "s3m",
    "mtm",
    "umx",
    # Playlists
    "m3u",
    "m3u8",
    "pls",
    "wpl",
    "xspf",
    # Containers
    "mp4",
    "mkv",
    "avi",
    "mov",
    "webm",
    # Game / Specialized
    "vgm",
    "nsf",
    "spc",
    "psf",
    "adx",
    # Other
    "caf",
    "au",
    "snd",
    "8svx",
    "voc",
    "qcp",
    "gsm",
]


def guess_filetype_from_url(url: str):
    extension = url.split(".")[-1]
    # print("ogg" in MUSIC_FILE_EXTENSIONS)
    if extension.lower() in MUSIC_FILE_EXTENSIONS:
        return extension.lower()
    return None


def generate_full_path_with_extension(filename: str, url: str):
    extension = guess_filetype_from_url(url)
    if extension is None:
        raise ValueError("Extension could not be guessed")
    return f"{BASE_FILE_DIR}/{filename}.{extension}"


if __name__ == "__main__":
    # english_name = "To Live"
    # german_name = "wohin"
    # url = "https://dict.leo.org/media/audio/7DgsnY51kPJU7Dcl6ulASw.ogg"
    german_name = input("German Name: ")
    url = input("URL: ")
    full_path = generate_full_path_with_extension(german_name, url)
    download_audio(url, full_path)

    print("saved to:\n", full_path)
    # print("english name", english_name)
    print("german name:\n", german_name)

# /home/ankit/MyFiles/self_practice/python_prac/.venv/bin/python /home/ankit/MyFiles/self_practice/python_prac/general/download_german_audio.py
