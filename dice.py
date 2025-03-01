#random game with dice - you can roll as much as dice you want! 
#the program give you the final total of your dice :)
import random
print("Welcome to the dice game !")

nombre_des = int(input("How many dice do you want to roll ?: "))

valeur_des = [1, 2, 3, 4, 5, 6]
result = random.choices(valeur_des, k = nombre_des)
total_des = sum(result)

if nombre_des > 20:
    print("\nYou're a true gambler \U0001F60E ! \nThe total of the dice is :", total_des)
else:
    print(result, "\nThe total of the dice is :", total_des)
