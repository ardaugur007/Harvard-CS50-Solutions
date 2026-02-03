message = input("Input: ")
print("Output: ", end = "")

for l in message:

    if l.lower() not in ["a", "e", "i", "u", "o"]:
        print(l, end = "")

print()
