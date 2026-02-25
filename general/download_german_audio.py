"""
This script works with https://dict.leo.org/german-english/der%20Tag this website flawlessly. But for some reason, the same script has to be run twice, the first time, the file downloaded is of 0 bytes and second time it gives the right file.
"""

import os

import requests

# BASE_FILE_DIR = "files/german-audio"
BASE_FILE_DIR = "/home/ankit/MyFiles/Germany/German/Words and Phrases"


def download_audio(url: str, filename: str):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise error for bad status codes
        # os.makedirs(BASE_FILE_DIR, exist_ok=True)
        with open(filename, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        print(f"Download complete: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Download failed: {e}")


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
    print("ogg" in MUSIC_FILE_EXTENSIONS)
    if extension.lower() in MUSIC_FILE_EXTENSIONS:
        return extension.lower()
    return None


def generate_full_path_with_extension(filename: str, url: str):
    extension = guess_filetype_from_url(url)
    if extension is None:
        raise ValueError("Extension could not be guessed")
    return f"{BASE_FILE_DIR}/{filename}.{extension}"


if __name__ == "__main__":
    url = "https://dict.leo.org/media/audio/rcqMzQB-tJNIoEDfCLzkGQ.ogg"
    full_path = generate_full_path_with_extension("der Tag", url)
    download_audio(url, full_path)
