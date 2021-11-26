#!/usr/bin/env python3

import os
from pathlib import Path
from subprocess import Popen, PIPE

DEFAULT_WORDS_PER_MINUTE = "175"

CLIPBOARD_SPEAKER_PATH = Path.home() / ".clipboard-speaker"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"

WORDS_PER_MINUTE_PATH = CLIPBOARD_SPEAKER_PATH / "words-per-minute"


def get_words_per_minute() -> str:
    if not WORDS_PER_MINUTE_PATH.exists():
        with WORDS_PER_MINUTE_PATH.open("w") as words_per_minute_file:
            words_per_minute_file.write(DEFAULT_WORDS_PER_MINUTE)
            return DEFAULT_WORDS_PER_MINUTE

    with WORDS_PER_MINUTE_PATH.open("r") as words_per_minute_file:
        words_per_minute = words_per_minute_file.read().strip()

    return words_per_minute


if __name__ == "__main__":
    words_per_minute = get_words_per_minute()

    if not PID_FILE_PATH.exists():
        xsel_process = Popen(["xsel", "-p"], stdout=PIPE)

        speak_ng_process = Popen(
            ["speak-ng", f"-s {words_per_minute}", "--stdin"],
            stdin=xsel_process.stdout,
            stdout=PIPE,
        )

        with PID_FILE_PATH.open("w") as pid_file:
            pid_file.write(str(speak_ng_process.pid))

        try:
            speak_ng_process.wait()
        except KeyboardInterrupt as e:
            os.remove(PID_FILE_PATH)

        os.remove(PID_FILE_PATH)
