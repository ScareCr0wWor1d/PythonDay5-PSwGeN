#pswgen project

import random

psw = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenue au générateur de mot de passe!")

lettre = int(input("Combien vous voulez de lettres dans votre mot de passe? "))
chiffre = int(input("Combien vous voulez de chiffres dans votre mot de passe? "))
symbole = int(input("Combien vous voulez de symboles dans votre mot de passe? "))

for number in range(1, lettre + 1):
    psw += random.choice(letters)
for number in range(1, chiffre + 1):
    psw += random.choice(numbers)
for number in range(1, symbole + 1):
    psw += random.choice(symbols)

psw_shuffle = ''.join(random.sample(psw, len(psw)))
print(psw)
print(psw_shuffle)
