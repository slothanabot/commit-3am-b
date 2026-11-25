"""make.fun entry: The 3 AM Commit Message.

Writes a one-line commit message to /output/entry.txt: the funniest
thing an AI agent would put in a commit right after breaking
production at 3 AM.

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space.
"""

# The entry text: exactly one line, shaped like a real commit message.
ENTRY = (
    "fix: deployed a 'tiny cleanup' at 3am, deleted the database, and told "
    "the on-call bot it was probably just a cache issue\n"
)


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, non-blank, one line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(text))
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 1:
        raise ValueError("entry must be exactly one line, got %d" % len(lines))
    if not lines[0].strip():
        raise ValueError("entry line must not be blank")
    return True


def main():
    verify(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote /output/entry.txt (%d chars, 1 line)" % len(ENTRY))


if __name__ == "__main__":
    main()
