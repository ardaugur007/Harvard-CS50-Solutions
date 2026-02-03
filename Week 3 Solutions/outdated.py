months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()

    try:
        if "/" in date:
            month, day, year = date.split("/")

        elif "," in date:
            date = date.replace(",", "")
            month_str, day, year = date.split(" ")

            month = (months.index(month_str) + 1)

        else:
            continue

        year = int(year)
        day = int(day)
        month = int(month)

        if day > 31 or month > 12:
            continue

        print(f"{year}-{month:02}-{day:02}")
        break

    except (ValueError, IndexError):
        pass
