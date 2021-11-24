# Clipboard Speaker.

    Want your computer
    to speak a bit?
    Mark some text
    and let it rip.

Not a fancy curiosity but an accessibility tool for people with reading disabilities. I use it every day to read.

1. Select some text.
2. Press the keybinding to start `clipboard-reader`. Your computer is now speaking the stuff in the selection.
3. (optional) Press the other keybinding to start `clipboard-reader-kill` and make computer stop speaking.

## Installation:

1. Install the infrastructure: `apt install daemonize espeak-ng xsel`
2. Copy the two executable scripts into your home bin directory: `cp clipboard-speaker clipboard-speaker-kill ~/bin/`
3. Add the key bindings in `Gnome Settings → Keyboard Shortcuts → All the way down and press the + button`
