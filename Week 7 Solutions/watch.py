import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # iframe içinde srcyi bul
    regex = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    match = re.search(regex, s) # HTML içinde bu kalıbı ara

    if match:
        # Eşleşme varsa video idyi al ve kısa link formatında döndür
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    return None # Eşleşme yoksa


if __name__ == "__main__":
    main()
