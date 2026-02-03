grocery = {}

while True:
    try:
        item = input()
    except EOFError:
        break

    item = item.upper()

    if item in grocery:
        grocery[item] += 1

    else:
        grocery[item] = 1

last_list = sorted(grocery)

for i in last_list:
    count = grocery[i]
    print(f"{count} {i}")
