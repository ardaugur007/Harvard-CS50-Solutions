import random

while True:
    try:
        level = input("Level: ")
        level_int = int(level)

        if (level_int > 0): # Pozitif bir sayı mı?
            break

    except ValueError: # Sayı mı değil mi kontrol
        pass

answer = random.randint(1, level_int) # Levele kadar rastgele bir sayı tut

while True:
    try:
        guess = input("Guess: ")
        guess  = int(guess) # Ettiğimiz tahmini inte çevir ki matematiksel olarak tartabilelim

        if guess > 0:
            if guess < answer:
                print("Too small!")
            elif guess > answer:
                print("Too large!")
            else:
                print("Just right!")
                break # Kazandı oyun bitebilir

    except ValueError: # Sayı değilse başa sar
        pass

