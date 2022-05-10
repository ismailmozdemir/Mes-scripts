# -*- coding: utf-8 -*-

'''
Dimanche 30/01/2022
Version 1
Définition d'une fonction qui retourne l'aire d'un disque grâce au calcul de son rayon^2 * Pi
'''

# Importation de pi
from math import pi as pi

def aire(r):
    """
    Calcul de l'aire d'un disque avec comme argument le rayon
    Entrée :
        r : Le rayon du disque
    Sortie :
        L'aire du disque (Pi * rayon^2)
    Exemple :
        Calcul de l'aire du disque avec comme argument le rayon comme ci-dessous
        print(aire(2))

        12.566370614359172
        
    """
    return pi*r**2

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

# On demande un rayon puis on donne son aire en appelant la fonction aire
r=float(input("Entrez le rayon du disque : "))
print("\nL'aire d'un disque de rayon",r,"est", aire(r))
