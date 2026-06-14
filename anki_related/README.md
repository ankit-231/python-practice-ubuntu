# Anki related

## `auto_add_from_leo.py`

This is the main file that asks for a word and adds it to anki. You can enter english or german word, if it is found in leo, an option menu will be provided.

Note: `back_extra` means anything you want to add extra to the note other than the definition.

Note:

- Install AnkiConnect addon for anki first
- Anki needs to be running for this code to work
- Change deck name from `DECK_NAME` variable in `auto_add_from_leo.py`
- Also, change BASE_FILE_DIR in `download_german_audio.py` (make sure that python has permission to write to it, audio files will be downloaded there)

Run:

```sh
py -m anki_related.auto_add_from_leo
```
