import re
import sys

def main():
    print(validate(input("IPv4 Address: "))) # Kullanıcıdan IP'yi al

def validate(ip):
    # Sayı.sayı.sayı.sayı olması için gerekli kodlamayı gir
    regex = r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$"
    # Kalıba uyuyo mu bak
    matches = re.search(regex, ip)

    if not matches:
        return False
    # 4 grubu da kontrol et
    for i in range(1, 5):
        # Grubu sayıya çevir ki aralık kontrolü yapabilesin
        num = int(matches.group(i))

        if num < 0 or num > 255:
            return False
        # Sayı 0 değilse ve 0 ile başlıyorsa hata ver
        if matches.group(i).startswith("0") and len(matches.group(i)) > 1:
            return False

    return True

if __name__ == "__main__":
    main()
