# -*- coding: utf-8 -*-

'''
Samedi 08/01/2022
Version 1
On demande à l'utilisateur de taper une lettre, puis on détermine sa casse.
Si la casse est majuscule, on opére pour la changer en miniscule et inversement.
Si il s'agit d'un caractère, on affiche que ce n'est pas une lettre.
'''

# Affectation de la variable en demandant une saisie pour avoir une lettre 
lettre = str(input("Veuillez saisir une lettre :\n"))

# On teste si la lettre est majuscule, minuscule et on change sa casse, si c'est un caractère on indique que ce n'est pas une lettre
if "A"<=lettre<="Z":
	print("Vous avez saisi la lettre majuscule",lettre+".\nAprès transformation en minuscule, on obient la lettre",lettre.swapcase()+".")
		
elif "a"<=lettre<="z":
	print("Vous avez saisi la lettre minuscule",lettre+".\nAprès transformation en majuscule, on obient la lettre",lettre.swapcase()+".")
		
else:
	print("Vous avez saisi le caractère",lettre+", ce n'est pas une lettre.")

