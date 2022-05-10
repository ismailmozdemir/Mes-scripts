# -*- coding: utf-8 -*-

'''
Samedi 11/12/2021
Version 1
On demande le nombre de personne pour réaliser une pâte à crêpes
Puis adapte la recette en fonction du nombre de personne
'''

# Affectation de la varible en demandant une saisie pour avoir le nombre de personne pour adapter la recette en fonction
nbPersonnes = int(input("Pour combien de personne souhaitez-vous réaliser la pâte à crêpes ?\n"))

# Affectation des variables de la recette
farineTot = 31.25*nbPersonnes # en g
oeufsTot=0.5*nbPersonnes
laitTot=6.25*nbPersonnes # en cl
beurreTot=6.25*nbPersonnes # en g
sucrevTot=1.25*nbPersonnes # en g
rhumTot=0.625*nbPersonnes # en cl

# Affichage à l'utilisateur de la recette complète en fonction du nombre de personne demandé
print("\nPour",nbPersonnes,"personnes il faut :")
print(int(farineTot),"g de farine")
print(int(oeufsTot),"oeufs")
print(int(laitTot),"cl de lait")
print("1 pincée de sel")
print(int(beurreTot),"g de beurre")
print(int(sucrevTot),"g de sucre vanillé")
print(int(rhumTot),"cl de rhum")
