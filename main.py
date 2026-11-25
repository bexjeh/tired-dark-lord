"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback ".").
Deterministic: the text is a fixed string, no randomness, no network.
"""

import os

MONOLOGUE = (
    "Come in, come in. Mind the kettle \u2014 the imps broke the third one this week, "
    "and the spares are... somewhere.\n\n"
    "Your name is in my ledger. Page forty-one, line nine: one soul a year, signed "
    "in blood. Or ink. Blood, probably. You are three years late, and the interest \u2014 "
    "well, the interest has interest now.\n\n"
    "The ritual is at midnight. Candles lit, circle drawn, the goat has gone home \u2014 "
    "rota mix-up, do not ask.\n\n"
    "So kneel, or do not. I will collect tomorrow. Bring biscuits.\n\n"
    "The debt is not going anywhere. Neither, it turns out, am I."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
