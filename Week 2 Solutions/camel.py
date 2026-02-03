camelcase = input("camelCase: ")
print("snake_case: ", end = "")

for i in camelcase:

    if i.isupper():
        print("_" + i.lower(), end = "")
    else:
        print(i, end = "")

print()
