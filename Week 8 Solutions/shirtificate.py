from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Yazı tipi helvetica, bold, 50 puan
        self.set_font("helvetica", "B", 50)

        # Başlığı yazdır
        self.cell(0, 60, "CS50 Shirtificate", align = "C")

        # Satır atla
        self.ln(20)

def main():
    # İsim al
    name = input("Name: ")
    create_shirtificate(name)

def create_shirtificate(name):
    # PDF oluştur
    pdf = PDF()
    # Sayfa ekle
    pdf.add_page()
    # Resim ekle
    pdf.image("shirtificate.png", w = pdf.epw, y = 70)
    # İsim yazdırma
    pdf.set_text_color(255, 255, 255)
    # Yazı boyutunu ayarla
    pdf.set_font_size(25)
    # İmleci resmin üzerine taşı
    pdf.set_y(140)
    # İsmi yazdır
    pdf.cell(0, 10, name, align = "C")
    # Dosyayı kaydet
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
