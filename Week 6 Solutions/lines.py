import sys

def main():
    check() # İşlemlere başlamadan bi kontrol
    try:
        with open(sys.argv[1], "r") as file: # Dosyayı al ve oku
            lines = file.readlines() # Satırları okuyup listele

    except FileNotFoundError:
        sys.exit("File does not exist") # Yanlış girişlere karşı mesaj

    count = 0 # Sayaç
    for line in lines: # Her satırı incele
        if is_code_line(line): # Satırların kod olup olmadığı testi
            count += 1

    print(count) # Yazdır

def check():
    if len(sys.argv) < 2: # 2 elemanlı mı?
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2: # 2'den fazla mı?
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"): # Python dosyası mı?
        sys.exit("Not a Python file")

def is_code_line(line):
    line_strip = line.lstrip() # Boşlukları sil

    if len(line_strip) == 0: # Boş satır
        return False

    if line_strip.startswith("#"): # Yorum satırı
        return False

    return True # Kod satırını yolla

if __name__ == "__main__":
    main()
