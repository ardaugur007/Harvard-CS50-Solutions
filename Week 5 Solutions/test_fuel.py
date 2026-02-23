import pytest
from fuel import convert, gauge

def test_convert_valid(): # Doğru girdilerin testi
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("4/4") == 100
    assert convert("0/4") == 0

def test_convert_errors(): # Hatalı girdilerin testi
    with pytest.raises(ValueError):
        convert("5/4")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    with pytest.raises(ValueError):
        convert("cat/dog")

def test_negative_values(): # Negatif girdilerin testi
    with pytest.raises(ValueError):
        convert("-1/4")

    with pytest.raises(ValueError):
        convert("5/-3")

    with pytest.raises(ValueError):
        convert("-1/-1")

def test_gauge(): # Sınır değerlerin testi
    assert gauge(1) == "E"
    assert gauge(0) == "E"

    assert gauge(99) == "F"
    assert gauge(100) == "F"

    assert gauge(50) == "50%" # Normal yüzde testi



"""
Week 5 update fuel
def main():

    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction) # Dönüştür
            result = gauge(percentage) # Göstergeyi al
            print(result) # Yazdır, çık
            break

        except (ValueError, ZeroDivisionError): # Hata olursa başa sar
            pass

def convert(fraction):

    if "/" not in fraction: # Bölme işareti yoksa veya fazla varsa hata ver
        raise ValueError

    x_str, y_str = fraction.split("/")

    x = int(x_str)
    y = int(y_str)

    if x < 0 or y < 0: # Sayılar negatifse ValueError ver
        raise ValueError

    if y == 0: # Sıfıra bölme kontrolü
        raise ZeroDivisionError

    if x > y: # x'in y'den büyük olma kontrolü
        raise ValueError

    p = round((x / y) * 100) # Yüzde hesaplama ve yuvarlama
    return p


def gauge(percentage):

    if percentage <= 1: # %1 ve altı boşsa E
        return "E"

    elif percentage >= 99: # %99 ve üstü doluysa F
        return "F"

    else: # Arası normal yüzde
        return f"{percentage}%"


if __name__ == "__main__":
    main()
"""
