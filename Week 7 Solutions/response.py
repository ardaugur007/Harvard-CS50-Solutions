from validator_collection import checkers

def main():
    # Mail iste
    email = input("What's your email address? ")

    # Kütüphane ile kontrol et
    is_valid = checkers.is_email(email)
    # Sonucu yaz
    if is_valid:
        print("Valid")

    else:
        print("Invalid")

if __name__ == "__main__":
    main()
