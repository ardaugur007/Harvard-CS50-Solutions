import sys
import os
from PIL import Image, ImageOps # Resim için kütüphane

def main():
    check() # Hata kontrollerini yap

    # Dosya isimlerini al
    in_file = sys.argv[1]
    out_file = sys.argv[2]

    try:
        # Gömleği aç
        shirt = Image.open("shirt.png")
        size = shirt.size

        # Girilen resmi aç
        with Image.open(in_file) as photo:
            # Resmi gömlek boyutuna göre ayarla
            new_photo = ImageOps.fit(photo, size)
            # Gömleği resmin üstüne yapıştır
            new_photo.paste(shirt, shirt)
            # Kaydet
            new_photo.save(out_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

def check():
    # Sayı kontrolü
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    # Uzantıları ayır
    ext1 = os.path.splitext(in_file)[1].lower()
    ext2 = os.path.splitext(out_file)[1].lower()

    valid = [".jpg", ".jpeg", ".png"]

    # Uzantılar geçerli mi kontrol
    if ext1 not in valid:
        sys.exit("Invalid input")
    if ext2 not in valid:
        sys.exit("Invalid output")

    # Giriş ve çıkış aynı türde mi bak
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__":
    main()
