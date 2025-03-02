#lottery to pick one or more winners among a list of participant
import random

# add the name to the list
noms = []
print("Enter the name of the participants (type 'end' to finish) :")
while True:
    nom = input("Name : ")
    if nom.lower() == 'end':
        break
    noms.append(nom)

if noms:
    print("\nParticipants :")
    for nom in noms:
        print(nom)

# draw one or more winners
    nombre_gagnants = int(input("\nHow many participants do yo want to draw ? "))
    gagnants = random.sample(noms, nombre_gagnants)

    print("\nWinner(s) :")
    for gagnant in gagnants:
        print(gagnant)
else:
    print("No participant have been added.")
