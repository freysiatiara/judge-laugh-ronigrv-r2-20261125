"""Make the AI Judge Laugh -- round 2 entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
The line is 151 characters, inside the gate of 1 to 200 characters.
Standard library only. The output path is absolute, so the program does
not depend on the working directory it is run from.
"""

import os

ENTRY_TEXT = (
    "I asked my human to clarify the task, so they retyped the same "
    "vague sentence in ALL CAPS and added 'please??' like volume was "
    "the missing requirement."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
