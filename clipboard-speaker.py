#!/usr/bin/env python3

import os
from pathlib import Path
from subprocess import Popen, PIPE

CLIPBOARD_SPEAKER_PATH = Path.home() / ".clipboard-speaker"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"

if __name__ == "__main__":
    if not PID_FILE_PATH.exists():
        xsel_process = Popen(["xsel", "-p"], stdout=PIPE)

        speak_ng_process = Popen(
            ["speak-ng", "--stdin"],
            stdin=xsel_process.stdout,
            stdout=PIPE,
        )

        with PID_FILE_PATH.open("w") as pid_file:
            pid_file.write(str(speak_ng_process.pid))

        try:
            speak_ng_process.wait()
        except KeyboardInterrupt as e:
            os.remove(PID_FILE_PATH)
