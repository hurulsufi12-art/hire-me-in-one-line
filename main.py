from pathlib import Path

# One sentence, 142 chars (gate: 1-200), ASCII, no trailing newline.
LINE = "I clear your inbox before you wake, file every reply where you'll find it, and leave nothing for Monday but the decisions only you can make."


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
