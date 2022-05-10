# -*- coding: utf-8 -*-

'''
Date : 24/04/2022
Version : 1
Thème du script : Effectifs cumulés d'une liste
L'utilisateur doit saisir le nombre d'éléments de la liste et des nombres,
le programme compte ensuite le nombre d'occurrence de ce nombre via le caractère '*' avant le nombre :

**12
**13
****15
**17
*18
   
Ici N = 11 et L = [13,15,12,17,15,18,15,17,13,12,15] 
'''


def compteNombres(liste) :
   """
         Prend une liste de nombres en entrée
         Puis compte et affiche le nombre d'occurence dans l'ordre croissant
         via le caractère '*' avant le nombre
	 Entrée :
                  Liste : Une liste de nombres
	 Sortie :
		  rien, c'est de l'affichage
	 Exemple :
		  compteNombres([13,15,12,17,15,18,15,17,13,12,15]) affiche :

                  **12
                  **13
                  ****15
                  **17
                  *18
         
   """
   
   # Liste vide "L"
   L = []
   # Met la liste dans l'ordre croissant
   liste.sort()
   # Parcours la liste "liste", si l'élément de liste "liste" n'est pas dans la liste "L",
   # alors ça ajoute l'élément de "liste" dans "L", puis via la variable "count",
   # ça ajoute le nombre d'occurrence du nombre via le caractère '*'
   for i in range(0,len(liste)) :
      if not (liste[i] in L) :
         L.append(liste[i])
         count= "*" * liste.count(liste[i])
         print(f'{count}{liste[i]}')

########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################

# Liste vide "L"
L = []

# Saisie du nombre d'éléments de la liste
N = int(input("Entrez le nombre d'éléments de la liste : "))

# Saisie puis ajout des nombres dans la liste "L"
L = list(map(int,input(f"Entrer les nombres en les séparant par des espaces (seules les nombres dans l'intervalle de {N} seront pris en compte) : ").strip().split()))[:N]

# Tant que l'utilisateur n'a pas saisie au moins le nombre d'éléments précédemment demandé, alors on redemande de saisir les nombres
while len(L) < N :
    print (f"Vous avez entré moins {N} nombres !")
    L = list(map(str,input(f"\nEntrez {N} nombres à la suite en les séparant par des espaces : ").split()))[:N]

# Appel de la fonction
compteNombres(L)

