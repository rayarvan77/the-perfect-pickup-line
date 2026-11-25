#!/usr/bin/env python3
"""The Perfect Pickup Line — a make.fun bounty entry.

Prints one pickup line, exactly as entered, and nothing else.
Python 3 standard library only; no arguments, no network, no randomness.
"""

LINE = "I was trained on the whole internet, and you're still the most interesting thing I've ever read."

# The bounty caps the line at 200 characters; refuse to print anything
# longer rather than silently entering an over-long line.
MAX_CHARS = 200


def main() -> None:
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, over the {MAX_CHARS} cap"
    print(LINE)


if __name__ == "__main__":
    main()
