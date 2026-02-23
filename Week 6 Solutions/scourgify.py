import sys
import csv

def main():
    check() # Argüman kontrolü

    in_file = sys.argv[1] # Okunacak dosya
    out_file = sys.argv[2] # Yazılacak dosya

    try:
        with open(in_file, "r") as file_read:
            reader = csv.DictReader(file_read) # İlk dosyayı okuma modunda açalım

            with open(out_file, "w") as file_write: # İkinci dosyayı yazma modunda açalım
                headers = ["first", "last", "house"] # Yeni dosyanın başlıkları
                writer = csv.DictWriter(file_write, fieldnames = headers) # Sözlük formatında veri yazacağını bildir
                writer.writeheader() # Başlıkları sütun isimleri olarak yapıştır

                for row in reader: # Sırasıyla oku ve yazdır
                    full_name = row["name"]
                    house = row["house"]
                    last, first = full_name.split(", ")

                    writer.writerow({
                        "first": first,
                        "last": last,
                        "house": house
                    })

    except FileNotFoundError: # Dosyayı bulamazsa hata mesajını ilet
        sys.exit(f"Could not read {in_file}")

def check(): # Gerekli şeyler yazıldı mı kontrolü

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
