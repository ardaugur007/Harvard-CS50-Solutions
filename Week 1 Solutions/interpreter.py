interpreter = input("Expression: ")
x, y, z = interpreter.split(" ")

num_x = float(x)
num_z = float(z)

if y == "+":
    print(f"{num_x + num_z:.1f}")

elif y == "-":
    print(f"{num_x - num_z:.1f}")

elif y == "*":
    print(f"{num_x * num_z:.1f}")

elif y == "/":
    print(f"{num_x / num_z:.1f}")
