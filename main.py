#!/usr/bin/env python3
"""Write one funny one-star cat review to entry.txt (make.fun, stdlib only)."""

import os


def main() -> None:
    # Revised line: "his plant" instead of "the plant" — the sting is now
    # revenge, not random damage. The cat ate the human's own plant because
    # the human was six hours late; the ownership twist is the joke's second
    # read, and it makes the voice unmistakably feline (punish the human's
    # things, on cat time). Deadpan shape kept, punch word ("plant") last.
    line = (
        "One star. He left for 'five minutes.' I counted. "
        "It was six hours. I have eaten his plant."
    )
    assert 1 <= len(line) <= 200, "entry must be 1-200 characters"
    assert "\n" not in line, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
