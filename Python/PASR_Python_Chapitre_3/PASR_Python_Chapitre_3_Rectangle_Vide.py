# -*- coding: utf-8 -*-

'''
Dimanche 30/01/2022
Version 1
Définition d'une fonction à trois arguments qui dessine un rectangle vide formé par le premier argument,
d'une taille définit par le deuxième argument pour le nombre de lignes et le troisième pour le nombre de colonnes
Le programme appel ensuite la fonction pour dessiner un rectangle vide aux dimensions entrées par l'utilisateur.
'''


def rectangleVide(car,H,C):
    """
    dessine un rectangle vide avec un caractère motif
    Entrées :
        car : le caractère motif
        H : le nombre de lignes
        C : le nombre de colonnes
    Sortie :
        Aucune : il s'agit d'un affichage
    Exemple :
        rectangleVide("*",5,6)
        dessine le rectangle vide ci-dessous
        ******
        *    *
        *    *
        *    *
        ******
    """
    print("\n"+car * C)
    for i in range(H-2) :
        print (car +(" " * (C -2)) + car)
    print(car * C)
    
    
################################################
########## PROGRAMME PRINCIPAL  ################
################################################

# On demande un caractère puis le nombre de lignes et de colonnes, enfin, on crée le rectangle grâce à l'appel de la fonction
car = str(input("Entrez votre caractère : "))
H = int(input("Entrez le nombre de lignes : "))
C = int(input("Entrez le nombre de colonnes : "))
rectangleVide(car,H,C)
