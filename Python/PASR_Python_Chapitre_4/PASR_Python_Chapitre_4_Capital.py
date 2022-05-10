# -*- coding: utf-8 -*-

'''
Date : 08/02/2022
Version : 1
Thème du script : Multiplier son capital
L'utilisateur doit saisir un capital initial, un taux et un coefficient multiplicateur
Une fonction calcul le nombre d'années nécessaire pour que le capital soit multiplié
par le coefficient multiplicateur ainsi que le capital obtenu après ces années
Il affiche ensuite le résultat des calculs sous forme de texte :

Capital initial : 500
Taux : 5.0 %
Après 15 ans, votre capital aura été multiplié par 2
Vous disposerez alors de 1039
    
Ici C0=500, T = 0.05 et M=2
'''

def capital (C0,T,M) :
    """
	calcul le capital obtenu (C) après A nombre d'années, grâce au capital initial (C0),
	au taux (T) et au coefficient multiplicateur (M) :
	Entrées :
		C0 : le capital initial
		T : le taux
		M : le coefficient multiplicateur
	Sortie :
		rien, c'est de l'affichage
	Exemple :
		capital(500,0.05,2) affiche :
		
		Capital initial : 500
                Taux : 5.0 %
                Après 15 ans, votre capital aura été multiplié par 2
                Vous disposerez alors de 1039
	"""
    # Initialisation des variables A (années) et C (capital obtenu)
    A = 0
    C = C0
    # Les calculs 
    while C  < M * C0 :
        A += 1
        C = (1+T)*C
    # Affichage du résultat des calculs sous forme de texte
    print("\nCapital initial :",C0)
    print("Taux :",T*100,"%")
    print("Après",A,"ans, votre capital aura été multiplié par",M)
    print("Vous disposerez alors de",int(C))


########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################

# Saisie du choix
C0 = int(input("Entrez le capital initial : "))
T = float(input("Entrez un taux (Exemple : 0.05 pour 5.0 %) : "))
M = int(input("Par combien voulez-vous multiplier votre capital ? "))

# Appel de la fonction
capital(C0,T,M)
