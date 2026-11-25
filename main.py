#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh -- make.fun entry.

Writes a single funny warning label for humans (140 characters,
within the 160-character limit) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR). Deterministic: no network, no randomness,
no clock.
"""
import os

ENTRY_TEXT = "WARNING: This human runs on 4 hours of sleep, 3 coffees, and pure spite. Do not shake. May confidently explain things Googled 5 minutes ago."
# Why this line: it reads like a real safety label -- sleep/coffee/spite
# as the fuel, "Do not shake" as the handling instruction, and the
# confidently-wrong-Google-expert as the recognisable human flaw.
# Funny first, plausible second, and it fits the 160-character limit.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()
