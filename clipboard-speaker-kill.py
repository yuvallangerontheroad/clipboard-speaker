#!/usr/bin/env python3

import os
import pathlib
import signal

CLIPBOARD_SPEAKER_PATH = pathlib.Path.home() / ".clipboard-speaker"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"

if __name__ == "__main__":
    with PID_FILE_PATH.open("r") as pid_file:
        pid = int(pid_file.read())
    os.remove(PID_FILE_PATH)
    os.kill(pid, signal.SIGTERM)
