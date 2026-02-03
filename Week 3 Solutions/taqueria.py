menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_cost = 0

while True:
    try:
        food = input("Item: ")

    except EOFError:
        break
    food = food.title()

    if food in menu:
        cost = float(menu[food])
        total_cost += cost
        print(f"Total: ${total_cost:.2f}")

    else:
        pass
