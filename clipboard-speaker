#!/usr/bin/env python3

import os
from pathlib import Path
from subprocess import Popen, PIPE

DEFAULT_WORDS_PER_MINUTE = "175"

CLIPBOARD_SPEAKER_PATH = Path.home() / ".clipboard-speaker"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"
FIFO_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "fifo"

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
    try:
        os.mkfifo(FIFO_FILE_PATH, mode=0o600)
    except FileExistsError:
        pass

    # https://stackoverflow.com/questions/63132778/how-to-use-fifo-named-pipe-as-stdin-in-popen-python
    fifo_read_file = os.open(FIFO_FILE_PATH, os.O_RDONLY | os.O_NONBLOCK)
    fifo_write_file = os.open(FIFO_FILE_PATH, os.O_WRONLY)

    Popen(
        ["xsel", "-p"],
        stdout=fifo_write_file,
    )
    os.close(fifo_write_file)

    if not PID_FILE_PATH.exists():
        speak_ng_process = Popen(
            [
                "speak-ng",
                f"-s {words_per_minute}",
            ],
            stdin=fifo_read_file,
        )
        os.close(fifo_read_file)

        with PID_FILE_PATH.open("w") as pid_file:
            pid_file.write(str(speak_ng_process.pid))

        try:
            speak_ng_process.wait()
        except KeyboardInterrupt as e:
            os.remove(PID_FILE_PATH)

        os.remove(PID_FILE_PATH)
