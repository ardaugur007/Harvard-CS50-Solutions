from bank import value

def test_value_0(): # Hello diyenler 0 alıyor mu?
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("Hello Newman") == 0

def test_value_20(): # H ile başlayanlar 20 alıyor mu?
    assert value("Hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20
    assert value("hola amigo") == 20

def test_value_100():
    assert value("What's up?") == 100
    assert value("good morning") == 100
    assert value("123") == 100
    assert value("Yo Whaddup?") == 100

"""
Week 5 bank update:
def main():
    greeting = input("Greeting: ")
    result = value(greeting) # Parayı çağır
    print(f"${result}") # Yazdır

def value(greeting): # Selamlamaya göre gelecek para
    greeting = greeting.lower().strip()

    if greeting.startswith("hello"):
        return 0

    elif greeting.startswith("h"):
        return 20

    else:
        return 100


if __name__ == "__main__":
    main()
"""
