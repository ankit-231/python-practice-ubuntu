"""
anki.py
This file contains functions to interact with Anki using AnkiConnect.
"""

import requests

import os
import base64

ANKI_CONNECT_URL = "http://localhost:8765"


def invoke(action, **params):
    return requests.post(
        ANKI_CONNECT_URL, json={"action": action, "version": 6, "params": params}
    ).json()


def add_note(deck_name, model_name, front, back, back_extra="", audio_filename=""):
    if back_extra:
        back_extra = "<br>" + back_extra
    note = {
        "deckName": deck_name,
        "modelName": model_name,
        "fields": {
            "Front": front,
            "Back": back + back_extra + f"<br>[sound:{audio_filename}]",
        },
        "options": {"allowDuplicate": False},
        "tags": ["german"],
    }

    result = invoke("addNote", note=note)
    return result["result"]  # <-- note ID


def store_audio_in_anki(full_path):
    filename = os.path.basename(full_path)

    with open(full_path, "rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    invoke("storeMediaFile", filename=filename, data=data)

    return filename
