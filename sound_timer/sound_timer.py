import time
import sys


try:
    import playsound
except ImportError:
    raise ImportError(
        "playsound is not installed in this virtual environment. "
        "Install it with: pip install playsound"
    )

MINUTES = 10
SECONDS = 0

PLAY_SOUND_FOR_X_TIMES = 1
PAUSE_BETWEEN_SOUNDS = 1  # Seconds

SOUND_PATH = "sound_timer/sound.wav"


total_seconds = MINUTES * 60 + SECONDS

try:
    for remaining in range(total_seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        # print(f"\r⏳ {mins:02d}:{secs:02d} remaining", end="", flush=True)
        print(f"\r⏳ {mins:02d}:{secs:02d} remaining", end="", flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\n❌ Timer cancelled")
    exit(0)


for _ in range(PLAY_SOUND_FOR_X_TIMES):
    playsound.playsound(sound=SOUND_PATH, block=True)
    time.sleep(PAUSE_BETWEEN_SOUNDS)


# CREDITS FOR MUSIC: https://freesound.org/people/owstu/sounds/508321/
