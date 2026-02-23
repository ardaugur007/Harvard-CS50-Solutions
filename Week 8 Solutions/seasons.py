from datetime import date
import sys
import inflect

def main():
    # Tarihi iste
    birth_date_str = input("Date of Birth: ")
    # String olan tarihi date yap
    try:
        birth_date = date.fromisoformat(birth_date_str)

    except ValueError:
        sys.exit("Invalid date")
    # Bugünün tarihini al
    today = date.today()
    # Dakikayı hesapla
    minutes = get_minutes(birth_date, today)
    # Yazıya çevir
    print(convert(minutes))

def get_minutes(start_date, end_date):
    # İki datei çıkarınca geriye timedelta objesi dönsün
    delta = end_date - start_date
    # Günü dakikaya çevir
    minutes = delta.days * 24 * 60
    return minutes

def convert(minutes):
    # Dakikayı ingilizce metne çevir
    p = inflect.engine()
    words = p.number_to_words(minutes, andword = "")
    return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()
