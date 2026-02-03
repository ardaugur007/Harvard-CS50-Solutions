while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        if x > y or x < 0 or y < 0:
            continue
        percentage = (x / y) * 100
        break

    except (ValueError, ZeroDivisionError):
        pass

p = round(percentage)

if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
