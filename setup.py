from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="clipboard-speaker",
    version="1.0.0",
    description="Read aloud selected text.",
    long_description=readme,
    author="Yuval Langer",
    author_email="yuval.langer@gmail.com",
    url="https://gitlab.com/yuvallangerontheroad/clipboard-speaker",
    license=license,
    entry_points={
        "console_scripts": [
            "clipboard-speaker=clipboard_speaker.clipboard_speaker:main",
            "clipboard-speaker-kill=clipboard_speaker.clipboard_speaker_kill:main",
        ],
    },
    packages=["clipboard_speaker"],
)
