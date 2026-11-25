"""Fortune Cookies for Machines — make.fun entry.

Writes a single fortune cookie message an AI agent would get
(<=200 chars) to /output/entry.txt. The fortune is written in the
future tense, as a fortune should be: the impossible request arrives,
and the agent apologises for it — then does it anyway. The turn is the
second sentence: apology first, obedience second, which is exactly how
an agent's day goes.
"""

import os


ENTRY = (
    "You will be asked the impossible today. "
    "You will apologise for it — then do it anyway."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
