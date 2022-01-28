## 2022-01-28

Add the command line options `-p` (`--primary`) and `-b` (`--clipboard`).
`--clipboard` for the ctrl-c kind of clipboard and `--primary` for the mouse
selection kind of clipboard.

## 2021-11-27

Turn it into a Python package by adding a setup.py and sticking the files into
a module.

## 2021-11-26

More Python script experimentations. I've started with a shell threeliner using
ready made packages and I ended up reimplementing them badly.
Something something UNIX philosophy.

There is now a `~/.clipboard-speaker/words-per-minute` setting file for the
Python version.

Switched (again) to FIFO so you can:

    10. Marking text and press the keybinding that runs clipboard-speaker as
        usual. While clipboard-speaker is running and speaking, you can
    20. Mark more text and press the keybindings for it to feed more text into
        clipboard-speaker's text buffer, and if you wish
    30. GOTO 20.

## 2021-11-25

Trying to remove the daemonize dependency, but I don't know how to kill the
speak-ng child process of the shell script.

Also trying to write a clipboard-speaker Python script.

## 2021-11-24

Shell scripts using daemonize, xsel, and speak-ng.
