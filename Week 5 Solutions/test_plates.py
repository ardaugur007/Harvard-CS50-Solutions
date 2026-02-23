from plates import is_valid

def test_start_two_letters(): # Başta en az iki harf var mı?
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C50") == False
    assert is_valid("50") == False

def test_length(): # Uzunluğu 2 ile 6 arası mı?
    assert is_valid("AA") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_numbers_and_zero(): # Sayılar ve sıfır doğru yerde mi?
    assert is_valid("AAA222") == True
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True

def test_punctuation(): # Noktalama kuralları doğru mu?
    assert is_valid("PI3.14") == False
    assert is_valid("CS 50") == False
    assert is_valid("HI!") == False

"""
Week 5 update vanity plates
def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6: # Uzunluk 2 ile 6 arasında mı?
        return False

    if not s[0:2].isalpha(): # İlk iki karakter harf mi?
        return False

    if not s.isalnum(): # Noktalama işareti veya boşluk var mı?
        return False

    for i in range(len(s)): # Sayıların konumu ve sıfır kuralı için

        if s[i].isdigit(): # İlk sayı sıfır olmamalı
            if s[i] == '0':
                retrun False
            else:
                if s[i:].isdigit(): # İlk sayıdan sonrası full sayı olmalı
                    return True
                else:
                    return False

    return True # Hiç sayı yoksa sadece harfse diğer kuralları aksatmıyorsa geçer

if __name__ == "__main__":
    main()
"""
