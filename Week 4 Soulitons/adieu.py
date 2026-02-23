import inflect

inf = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)

    except EOFError:
        print()
        break

end = inf.join(names)
print(f"Adieu, adieu, to {end}")

