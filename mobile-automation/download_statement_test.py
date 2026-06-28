import subprocess
import time

# ==========================
# CONFIGURATION
# ==========================

FROM_DATE = "4/1/2026"
TO_DATE = "4/30/2026"

# Coordinates
FILTER_BTN = (744, 287)

FROM_DATE_FIELD = (330, 2037)
TO_DATE_FIELD = (806, 2055)

PENCIL_ICON = (875, 775)

DATE_INPUT_FIELD = (496, 557)

KEYBOARD_CLOSE_BTN = (1003, 2259)  # optional

OK_BTN = (860, 1813)

APPLY_BTN = (562, 2211)

DOWNLOAD_BTN = (1010, 148)

# Delays (increase if phone is slower)
SHORT = 2
MEDIUM = 3
LONG = 4
VERY_LONG = 12


# ==========================
# HELPERS
# ==========================


def adb(*args):
    cmd = ["adb"] + list(args)

    print(">", " ".join(cmd))

    result = subprocess.run(cmd, capture_output=True, text=True)

    return result


def tap(x, y):
    print(f"Tapping ({x}, {y})")
    adb("shell", "input", "tap", str(x), str(y))
    time.sleep(SHORT)


def back():
    print("Pressing BACK")
    adb("shell", "input", "keyevent", "4")
    time.sleep(SHORT)


def input_text(text):
    # Escape slashes for adb
    # escaped = text.replace("/", "%2F")

    print(f"Typing: {text}")

    adb("shell", "input", "text", text)

    time.sleep(SHORT)


def clear_date_field():
    # Tap the input field first so it has focus
    tap(*DATE_INPUT_FIELD)

    # Delete more characters than necessary
    for _ in range(15):
        adb("shell", "input", "keyevent", "67")  # KEYCODE_DEL
        time.sleep(0.05)


# ==========================
# MAIN FLOW
# ==========================

print("\nStarting in 5 seconds...")
print("Make sure:")
print("- Phone is unlocked")
print("- Banking app is open")
print("- You are already on the statement page\n")

time.sleep(5)

# Open filter drawer
tap(*FILTER_BTN)

time.sleep(MEDIUM)

# --------------------------
# FROM DATE
# --------------------------

tap(*FROM_DATE_FIELD)

time.sleep(MEDIUM)

tap(*PENCIL_ICON)

time.sleep(MEDIUM)

tap(*DATE_INPUT_FIELD)


time.sleep(SHORT)

clear_date_field()

input_text(FROM_DATE)

# Hide keyboard
back()

time.sleep(SHORT)

tap(*OK_BTN)

time.sleep(MEDIUM)

# --------------------------
# TO DATE
# --------------------------

tap(*TO_DATE_FIELD)

time.sleep(MEDIUM)

tap(*PENCIL_ICON)

time.sleep(MEDIUM)

tap(*DATE_INPUT_FIELD)

time.sleep(SHORT)

clear_date_field()

input_text(TO_DATE)

# Hide keyboard
back()

time.sleep(SHORT)

tap(*OK_BTN)

time.sleep(MEDIUM)

# --------------------------
# APPLY FILTER
# --------------------------

tap(*APPLY_BTN)

print("Waiting for statement to load...")
time.sleep(VERY_LONG)

# --------------------------
# DOWNLOAD PDF
# --------------------------

print("Attempting download...")

tap(*DOWNLOAD_BTN)

print("\nWaiting for PDF to open...")
time.sleep(VERY_LONG)

print("\nDone.")
print("If everything worked, the PDF should now be open.")
