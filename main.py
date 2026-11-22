"""make.fun quick-fire entry: "Somebody Has Written Back".

Writes the entry text to ``entry.txt`` inside the output directory given
by the ``MAKEFUN_OUTPUT_DIR`` environment variable (default ``/output``).
"""

import os
from pathlib import Path

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
ENTRY_PATH = OUTPUT_DIR / "entry.txt"

TEXT = (
    "Every night at 3:17, the lighthouse keeper climbs the stairs, lights a "
    "lamp no ship has needed for forty years, and writes one line in a "
    "logbook nobody reads. Tonight, for the first time, somebody has "
    "written back."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry text must be 1-280 code points, got {len(TEXT)}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
