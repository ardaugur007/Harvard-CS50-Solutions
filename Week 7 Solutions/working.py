import re
import sys

def main():
    # Saati al ve çevir
    try:
        print(convert(input("Hours: ")))

    except ValueError:
        print("ValueError")
        sys.exit("ValueError")

def convert(s):
    # Regexi ayarla
    regex = r"^([0-9]+)(?::([0-9]{2}))? (AM|PM) to ([0-9]+)(?::([0-9]{2}))? (AM|PM)$"

    match = re.search(regex, s)

    if not match:
        raise ValueError

    # Grupları değişkenlere ata
    h1, m1, p1 = match.group(1), match.group(2), match.group(3)
    h2, m2, p2 = match.group(4), match.group(5), match.group(6)

    # Dakikalar yoksa "00" olarak ayarla
    if m1 is None: m1 = "00"
    if m2 is None: m2 = "00"

    # Saatleri dönüştür
    time1 = convert_to_24(h1, m1, p1)
    time2 = convert_to_24(h2, m2, p2)

    return f"{time1} to {time2}"

def convert_to_24(hour, minute, period):
    h = int(hour)
    m = int(minute)

    if h > 12 or m >= 60: # Geçersiz giriş kontrolü
        raise ValueError

    if period == "AM":
        if h == 12: # 12 AM ==> 00 yapılır
            h = 0
    else:
        if h != 12: # 12 PM dışındakilere 12 ekle
            h += 12

    return f"{h:02}:{m:02}" # Tek haneli sayıların başına sıfır koy

if __name__ == "__main__":
    main()

