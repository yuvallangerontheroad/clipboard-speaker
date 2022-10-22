# Clipboard Speaker.

    Want your computer
    to speak a bit?
    Mark some text
    and let it rip.

Not a fancy curiosity but an accessibility tool for people with reading
disabilities. I use it every day to read.

It basically reads whatever you mark with your mouse cursor.

## Code repositories:

Main development repository is on codeberg.org:

https://codeberg.org/yuvallangerontheroad/clipboard-speaker/

Mirrors:

* https://gitlab.com/yuvallangerontheroad/clipboard-speaker/
* https://github.com/yuvallangerontheroad/clipboard-speaker/
* https://gitlab.com/yuvallanger/clipboard-speaker/
* https://github.com/yuvallanger/clipboard-speaker/

## Changelog:

Have a look at the <a href="CHANGELOG.md">CHANGELOG.md</a> file.

## Newer Python version:

### Installation:

#### Dependencies:

* https://python.org/
* https://github.com/espeak-ng/espeak-ng/
* https://github.com/kfish/xsel

#### Install the Dependencies:

##### On Debian based systems:

`apt install espeak-ng xsel python3`

#### Install the script files:

##### Manually:

Copy the two executable scripts into your home bin directory:

```
cp clipboard_speaker/clipboard_speaker.py ~/bin/clipboard-speaker
cp clipboard_speaker/clipboard_speaker_kill.py ~/bin/clipboard-speaker-kill
```

##### pip:

```
pip install --user .
```

After which the script files are located, at least here in my system, under
`~/.local/bin/` as `~/.local/bin/clipboard-speak` and
`~/.local/bin/clipboard-speak-kill`.

#### Map your keybindings:

##### On Gnome:

Add the key bindings in (if you use Gnome. If you don't, look up how to
    assign scripts to keybindings in your own window manager):

```
Gnome Settings
    → Keyboard Shortcuts
    → All the way down and press the + button
```

### Usage:

1. Select some text. While the text is highlighted,
2. press the keybinding assigned to the `clipboard-reader` executable to start
    the reading of the highlighted text.
3. (optional, while `clipboard-speaker` is reading the text) Select some more
    text and press the keybinding that starts `clipboard-reader`. The selected
    text will be added to the text buffer and will be read right after the last
    bunch of text.
4. (optional) GOTO 3.
5. (optional) Press the other keybinding assigned to the `clipboard-reader-kill`
    script to make your computer stop speaking and clear the text buffer.

## Older shell version:

### Dependencies:

* http://software.clapper.org/daemonize/
* https://github.com/espeak-ng/espeak-ng/
* https://github.com/kfish/xsel

### Installation:

1. Install the dependencies:
    `apt install daemonize espeak-ng xsel`
2. Copy the two executable scripts into your home bin directory:
    `cp clipboard-speaker clipboard-speaker-kill ~/bin/`
3. Add the key bindings in:
    `Gnome Settings → Keyboard Shortcuts → All the way down and press the + button`

### Usage:

1. Select some text.
2. Press the keybinding to start `clipboard-reader`. Your computer is now speaking the stuff in the selection.
3. (optional) Press the other keybinding to start `clipboard-reader-kill` and make computer stop speaking.
