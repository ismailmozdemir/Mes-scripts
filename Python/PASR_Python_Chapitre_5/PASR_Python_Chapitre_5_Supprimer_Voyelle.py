# -*- coding: utf-8 -*-

'''
Date : 24/04/2022
Version : 1
Thème du script : Supprimer les mots contenant une voyelle donnée
L'utilisateur doit saisir le nombre de mots de la liste et des mots,
il doit ensuite saisir une voyelle, puis le programme supprime les mots dans lesquels se trouvent cette voyelle de la liste :

['Homer', 'Moe', 'Nelson', 'Milhouse', 'Krusty']
   
Ici N = 10, L = ["Homer", "Marge", "Bart", "Lisa", "Moe", "Charles", "Nelson", "Milhouse", "Krusty", "Barney"] et V = "a"
'''

def supprimeVoyelle (L,V) :
    """
         Prend une liste de mots en entrée
         Puis supprime les mots dans lesquels se trouvent une voyelle
	 Entrées :
                  L : Une liste de mots
                  V : Une voyelle
	 Sortie :
		  rien, c'est de l'affichage
	 Exemple :
		  supprimeVoyelle(["Homer", "Marge", "Bart", "Lisa", "Moe", "Charles", "Nelson", "Milhouse", "Krusty", "Barney"],"a") affiche :

                  ['Homer', 'Moe', 'Nelson', 'Milhouse', 'Krusty']
         
    """

    i = 0
    # Parcours les éléments de la liste "L"
    # Si la voyelle "V" est dans les mots de la liste "L"
    # alors la fonction supprime ce mot et enfin affiche la liste "L"
    while i < len(L) :
            if V in L[i] :
                L.pop(i)
            else :
                i += 1
    print (L)

########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################

# Liste vide "L"
L = []

# Saisie de l'utilisateur du nombre de mots et des mots
N = int(input("Entrez le nombre de mots : "))
L = list(map(str,input(f"\nEntrer les mots en les séparant par des espaces (seules les mots dans l'intervalle de {N} seront pris en compte) : ").split()))[:N]

# Si l'utilisateur saisie moins de mots que le nombre de mots demandé précédemment, on redemande de saisir les mots
while len(L) < N :
    print (f"Vous avez entré moins {N} mots !")
    L = list(map(str,input(f"\nEntrez {N} mots à la suite en les séparant par des espaces : ").split()))[:N]

    
# Liste contenant les voyelles de l'alphabet
voyelles = ["a","e","i","o","u","y"]

# On demande la saisie de la voyelle, si elle ne se trouve pas dans la liste "voyelles", on redemande de saisir la voyelle
V = str(input("Entrez une voyelle : "))
while not (V in voyelles) :
    print (V,"n'est pas une voyelle !")
    V = str(input("Entrez une voyelle : "))

# Appel de la fonction
supprimeVoyelle(L,V)




