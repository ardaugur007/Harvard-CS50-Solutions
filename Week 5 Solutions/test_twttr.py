from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("google") == "ggl"
    assert shorten("aeiou") == ""

def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_mixed():
    assert shorten("TwItTeR") == "TwtTR"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("123") == "123"

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("What's up?") == "Wht's p?"

"""
# Week 5 Update

def main():
    word = input("Input: ")
    output = shorten(word)
    print(f"Output: {output}")

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"] # Sesli harfleri daha sonradan ayıklayabilmek için tanımlıyoruz
    result = ""

    for char in word:
        if char.lower() not in vowels:
            result += char
    return result # Sesli harflerden arınmış kelimeyi gönder

if __name__ == "__main__":
    main()
"""
