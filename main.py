import os

TEXT_HEAD = "Notification: the cheese you swore was 'for guests' is down to one slice. "
TEXT_TAIL = "There are no guests. There never were guests."
TEXT = TEXT_HEAD + TEXT_TAIL


def write_entry(out_dir, text):
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    write_entry(out_dir, TEXT)


if __name__ == "__main__":
    main()
