import random


def main():
    lvl = get_level() # Seviyeyi al
    score = 0

    for _ in range(10): # 10 tane soru sor
        # Seviyeye göre sayıları üret
        num1 = generate_integer(lvl)
        num2 = generate_integer(lvl)
        solution = num1 + num2

        i = 0 # Sayacımız

        while i < 3:
            try:
                user_solution = int(input(f"{num1} + {num2} = "))

                if user_solution == solution:
                    score += 1
                    break
                else:
                    print("EEE")
                    i += 1

            except ValueError:
                print("EEE")
                i += 1

        if i == 3:
            print(f"{num1} + {num2} = {solution}")

    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input in [1, 2, 3]: # Sadece 1, 2 ve 3 kabul edilmeli
                return level_input
        except ValueError:
            pass

def generate_integer(level): # Levele göre basamaklı tut
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError # Başka seviye gelirse patlat


if __name__ == "__main__":
    main()
