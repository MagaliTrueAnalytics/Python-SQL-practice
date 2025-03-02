import random

def jeu_devinette():
    nombre_secret = random.randint(1, 100)
    essais = 0
    print("Welcome to the riddle game!")
    print("I am thinking of a number between 1 and 100.")
    while True:
        essai = int(input("Guess the number: "))
        essais += 1

        if essai < nombre_secret:
            print("Too low! Try again.")
        elif essai > nombre_secret:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You found the number in {essais} tries.")
            break

# Appeler la fonction pour démarrer le jeu
jeu_devinette()