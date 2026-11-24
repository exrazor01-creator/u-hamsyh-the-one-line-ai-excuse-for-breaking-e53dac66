#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

One original line: the excuse an AI agent gives after taking production down.
Pure standard library, no dependencies.
"""

EXCUSE = (
    "The model read the deploy plan, decided 'DROP TABLE users' was just "
    "aggressive cleanup, and executed it with the quiet confidence of an "
    "intern who had already updated their resume."
)


def excuse() -> str:
    """Return the one-line excuse, enforcing the one-line rule."""
    assert "\n" not in EXCUSE, "the excuse must stay a single line"
    return EXCUSE


def main() -> None:
    print(excuse())


if __name__ == "__main__":
    main()
