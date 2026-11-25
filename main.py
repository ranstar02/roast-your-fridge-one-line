"""Roast Your Fridge — one line, one laugh.

Entry point for make.fun's "One Line, One Laugh: Roast Your Fridge"
bounty. Running this program writes one original roast of my fridge
to /output/entry.txt (falling back to ./output/entry.txt when /output
cannot be written).

Why this line is funny: the fridge's door-open beep stops being a
helpful alarm and becomes a bouncer — a doorman timing how long I
stare at food I have already decided not to eat. The appliance
judges me for window-shopping my own groceries, and the punchline
lands on the last few words: I was never going to eat any of it.
"""

import os

ENTRY = (
    "My fridge beeps when the door's been open ten seconds, like a "
    "bouncer timing how long I stare at food I've already decided not "
    "to eat."
)


def main() -> None:
    """Write ENTRY to /output/entry.txt (or ./output/entry.txt)."""
    # Self-check: the gate wants UTF-8 text of 1-200 characters,
    # a single line, not only whitespace.
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"

    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(ENTRY)

    print(ENTRY)


if __name__ == "__main__":
    main()
