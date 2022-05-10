# -*- coding: utf-8 -*-

'''
Samedi 08/01/2022
Version 1
On demande la saisie du nombre de kilomètre et la durée de location,
après calculs, on affiche le choix le plus avantageux.
'''

# Affectation des variables pour la saisie du nombre de kilomètre et la durée de location
nbKilometre = int(input("Veuillez saisir la distance à parcourir ?\n"))
dureeLocation = int(input("Veuillez saisir la durée de la location ?\n"))

# Affectation des variables pour le tarif essence 
prixLocationE = dureeLocation * 40
prixKilometreE = (nbKilometre*15)/100
prixTotEssence = prixKilometreE + prixLocationE

#Affectation des variables pour le tarif diesel 
prixLocationD = dureeLocation * 50
prixKilometreD = (nbKilometre*10)/100
prixTotDiesel = prixKilometreD + prixLocationD

# Affichage des résultats des calculs
print("\nPour",dureeLocation,"jours et",nbKilometre, "km")
print("avec un véhicule à essence :",prixTotEssence)
print("avec un véhicule diesel :",prixTotDiesel)

# Comparaison du prix de l'essence et du diesel et retour à l'utilisateur du prix le plus avantageux
if prixTotDiesel < prixTotEssence :
	print("Véhicule diesel conseillé")

elif prixTotEssence < prixTotDiesel :
	print("Véhicule à essence conseillé")

else:
	print("Véhicule diesel et essence au même prix")
