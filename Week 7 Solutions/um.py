import re
import sys

def main():
    #  Metni al, sonucu yazdır
    print(count(input("Text: ")))

def count(s):
    # regexi ayarla
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    # Kaç tane um var gönder
    return len(matches)

if __name__ == "__main__":
    main()
