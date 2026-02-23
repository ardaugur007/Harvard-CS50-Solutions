from nation import Nation
from tabulate import tabulate
import sys
import random
import re

def main():
    print("WELCOME TO EMPIRE BUILDER")
    name = input("Name your empire: ")
    player = Nation(name)

    while True:
        # Her turun başında durumu göster
        display_status(player)
        # Kullanıcı ne yapmak istiyor
        print("\nCommands: 'build X farm', 'next', 'quit'")
        cmd_input = input("Your command, my liege?: ")

        # utils ile parçala
        action, amount, target = parse_command(cmd_input)

        if action == "quit":
            sys.exit("\nYour empire has fallen into history...")

        elif action == "next":
            # Tur atlama işlemleri
            food, gold = player.collect_resources()
            print(f"\n--- NEW TURN ---")
            print(f"Production: +{food} Food, +{gold} Gold")
            print(f"Population Growth: +{player.population // 10} people born!")

            # %30 ihtimalle saldırı olur
            if random.randint(1, 3) == 1:
                print("\nBARBARIAN RAID DETECTED!")
                # Savunma gücü: Her kışla 10, her duvar 50 koruma sağlar, düşman gücü: zenginlikle doğru orantılı artar
                defense_power = calculate_defense(player.buildings["barrack"], player.buildings["wall"])
                enemy_power = calculate_enemy_power(player.population)

                print(f"Enemy Power: {enemy_power} vs Your Defense: {defense_power}")

                if defense_power < enemy_power:
                    print("DEFEAT! Barbarians looted your city!")
                    # Cezası: Altın ve yemeğin yarısını çalar, nüfusu %10 azaltır
                    player.gold //= 2
                    player.food //= 2
                    casualties = player.population // 10
                    player.population -= casualties

                    print("You lost 50% of your resources.")
                else:
                    print("VICTORY! Your defenses held strong.")

            # Kıtlık kontrolü
            if player.food < 0:
                print("Your people are starving! Population decreased by 5.")
                player.population -= 5
                player.food = 0

            # Nüfus biterse oyun biter
            if player.population <= 0:
                sys.exit("\nYour empire has no population left. Game Over.")

        elif action == "build":
            # nation.py dosyasında hatayı verdiğimden burayı koru
            try:
                player.build(target, amount)
                print(f"Successfully built {amount} {target}(s)!")
            except ValueError as e: # Hata olursa program çökmeyecek mesajı basacak
                print(f"ERROR: {e}")

        else:
            print("Invalid command. Please try again.")

def display_status(nation):
    # Tabulate ile verileri tablola
    data = [
        ["Gold", nation.gold],
        ["Food", nation.food],
        ["Population", nation.population],
        ["Farms", nation.buildings["farm"]],
        ["Barracks", nation.buildings["barrack"]],
        ["Walls", nation.buildings["wall"]]
    ]
    print("\n" + tabulate(data, headers = ["Asset", "Amount"], tablefmt = "fancy_grid"))

def parse_command(command):
    # Kullanıcıdan gelen komudu algıla
    pattern = r"^(build|train)\s+(\d+)\s+(\w+)"
    # Komutu düzenle
    match = re.search(pattern, command.lower().strip())

    if match:
        # Regex tutarsa parçaları döndür
        return match.group(1), int(match.group(2)), match.group(3).rstrip('s') # Farm da farms da kabul edilsin diye rstrip('s')

    if command.strip().lower() in ["status", "quit", "next"]:
        # Regex tutmazsa tek kelimelik komutlara bak
        return command.strip().lower(), None, None

    # Hiçbiri değilse boş dön
    return None, None, None

def calculate_defense(barracks, walls):
    return (barracks * 10) + (walls * 50)

def calculate_enemy_power(population):
    return population * 2

if __name__ == "__main__":
    main()
