import os

FRIDGE_ALERT_TEXT = "Notification: the cheese you swore was 'for guests' is down to one slice. There are no guests. There never were guests."


def emit_note():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    target_path = os.path.join(target_dir, "entry.txt")
    with open(target_path, "w", encoding="utf-8") as handle:
        handle.write(FRIDGE_ALERT_TEXT)


if __name__ == "__main__":
    emit_note()
