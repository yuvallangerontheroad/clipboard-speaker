#!/usr/bin/env python3

import signal
import os
from pathlib import Path
from subprocess import Popen, PIPE

CLIPBOARD_SPEAKER_PATH = Path.home() / ".clipboard-speaker"
FIFO_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "fifo"
PID_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "pid"
LOCK_FILE_PATH = CLIPBOARD_SPEAKER_PATH / "lock"

if __name__ == "__main__":
    clipboard_speaker_pid = os.getpid()
    with open(PID_FILE_PATH, 'w') as pid_file:
        pid_file.write(str(clipboard_speaker_pid))
    #with open(FIFO_FILE_PATH, "w") as fifo:
    #    xsel_process = Popen(["xsel", "-p"], stdout=fifo)
    xsel_process = Popen(["xsel", "-p"], stdout=PIPE)
    speak_ng_process = Popen(
        [
            "speak-ng",
            '--stdin'
        ], 
        stdin=xsel_process.stdout,
        stdout=PIPE ,
    )
    def kill(*a):
        print('kill:', a)
        speak_ng_process.terminate()
    signal.signal(signal.SIGHUP, kill)
    signal.signal(signal.SIGTERM, kill)
    speak_ng_process.wait()
