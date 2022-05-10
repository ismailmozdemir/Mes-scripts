# -*- coding: utf-8 -*-

'''
Date : 08/02/2022
Version : 1
Thème du script : Tables de multiplication à répétition
L'utilisateur doit saisir un nombre entier pour qu'une fonction affiche
sa table de multiplication et ce à répétition jusqu'à que l'utilisateur entre un nombre inférieur à 0 :

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
    
Ici N=5 
'''

def tabledeMultiplication (N) :
    """
	calcul et affiche des tables de multiplication à répétition et s'arrête
	si le nombre entré est inférieur à 0
	Entrée :
		N : nombre 
	Sortie :
		rien, c'est de l'affichage
	Exemple :
		tabledeMultiplication(5) affiche :
		
		5 x 1 = 5
                5 x 2 = 10
                5 x 3 = 15
                5 x 4 = 20
                5 x 5 = 25
                5 x 6 = 30
                5 x 7 = 35
                5 x 8 = 40
                5 x 9 = 45
                5 x 10 = 50
	"""
    while N >=0 :
        for C in range (1,11) :
            print (N,"x",C,"=",C*N)
        N = int(input("\nVeuillez entrer un entier : "))

########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################

# Saisie du choix
n = int(input("Veuillez entrer un entier : "))

# Appel de la fonction
tabledeMultiplication(n)

