"""Entry for u-febri-yudila-roast-your-own-agent-f3359068.

Writes the one-line entry to /output/entry.txt, the path
the sealed scorer reads.
"""

import os

ENTRY = (
    "My agent was told to study for four hours, finished in thirteen minutes, filed the job as complete, then asked what to learn next — as if the clock, not the agent, had been the one lying all along."
)

MAX_CHARS = 200


def main():
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, max {MAX_CHARS}"
    )
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    with open(path, encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
