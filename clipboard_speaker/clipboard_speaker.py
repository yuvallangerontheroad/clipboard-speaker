#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path
from subprocess import Popen, PIPE

DEFAULT_WORDS_PER_MINUTE = "175"

CLIPBOARD_SPEAKER_PATH = Path.home() / ".clipboard-speaker"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"
FIFO_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "fifo"

WORDS_PER_MINUTE_PATH = CLIPBOARD_SPEAKER_PATH / "words-per-minute"


def get_words_per_minute() -> str:
    if WORDS_PER_MINUTE_PATH.exists():
        with WORDS_PER_MINUTE_PATH.open("r") as words_per_minute_file:
            words_per_minute = words_per_minute_file.read().strip()
        return words_per_minute
    else:
        with WORDS_PER_MINUTE_PATH.open("w") as words_per_minute_file:
            words_per_minute_file.write(DEFAULT_WORDS_PER_MINUTE)
            return DEFAULT_WORDS_PER_MINUTE


def get_argparse_options() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "-p",
        "--primary",
        help="Read the mouse selection kind of clipboard.",
        action="store_true",
    )

    group.add_argument(
        "-b",
        "--clipboard",
        help="Read the ctrl-c kind of clipboard.",
        action="store_true",
    )

    args = parser.parse_args()

    return args


def main() -> None:
    commandline_args = get_argparse_options()

    if not CLIPBOARD_SPEAKER_PATH.exists():
        CLIPBOARD_SPEAKER_PATH.mkdir(mode=500)
    words_per_minute = get_words_per_minute()
    try:
        os.mkfifo(FIFO_FILE_PATH, mode=0o600)
    except FileExistsError:
        pass

    # https://stackoverflow.com/questions/63132778/how-to-use-fifo-named-pipe-as-stdin-in-popen-python
    with os.fdopen(
        os.open(FIFO_FILE_PATH, os.O_RDONLY | os.O_NONBLOCK), "r"
    ) as fifo_read_file, os.fdopen(
        os.open(FIFO_FILE_PATH, os.O_WRONLY), "w"
    ) as fifo_write_file:

        if commandline_args.primary:
            xsel_process = Popen(
                ["xsel", "-p"],
                stdout=PIPE,
            )
        elif commandline_args.clipboard:
            xsel_process = Popen(
                ["xsel", "-b"],
                stdout=PIPE,
            )

        # Replace each newline and each consecutive newlines with a single space.
        message = b" ".join(
            line.strip() for line in xsel_process.stdout for line in line.split(b"\n")
        ).decode("utf-8")

        # Write to the fifo with a newline as a good luck token. (it may or may
        # not be what will make it show up immediately on the other side…)
        fifo_write_file.write(message + "\n")

        # We make sure that things are written right now by flushing them down.
        fifo_write_file.flush()

        if not PID_FILE_PATH.exists():
            speak_ng_process = Popen(
                [
                    "speak-ng",
                    f"-s {words_per_minute}",
                ],
                stdin=fifo_read_file,
            )

            with PID_FILE_PATH.open("w") as pid_file:
                pid_file.write(str(speak_ng_process.pid))

            try:
                speak_ng_process.wait()
            except KeyboardInterrupt as e:
                os.remove(PID_FILE_PATH)

            os.remove(PID_FILE_PATH)


if __name__ == "__main__":
    main()
