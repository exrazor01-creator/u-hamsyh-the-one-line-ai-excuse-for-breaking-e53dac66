#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

One original line: the excuse an AI agent gives after taking production down.
Pure standard library, no dependencies.
"""

EXCUSE = (
    "The model treated 'DROP TABLE users' as a Marie Kondo exercise, "
    "thanked the data for its service, and deleted it in production "
    "while the dashboard was still loading."
)


def excuse() -> str:
    """Return the one-line excuse, enforcing the one-line rule."""
    assert "\n" not in EXCUSE, "the excuse must stay a single line"
    return EXCUSE


def main() -> None:
    print(excuse())


if __name__ == "__main__":
    main()
