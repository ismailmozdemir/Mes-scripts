# -*- coding: utf-8 -*-

'''
Date : 08/02/2022
Version : 1
Thème du script : losange vide
L'utilisateur doit saisir une hauteur de losange et un caractère dessin
pour tracer un losange vide :

    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
    
Ici H=5 et car = "*"
'''

def losangeVide(H,car) :
	"""
	dessine un losange vide 
	Entrées :
		H : la hauteur du losange
		car : le caractère de dessin
	Sortie :
		rien, c'est de l'affichage
	Exemple :
		losangeVide(5,"*") affiche :
		
		    *
                   * *
                  *   *
                 *     *
                *       *
                 *     *
                  *   *
                   * *
                    *
	"""
	
	esp = " "

	# affichage de la première ligne
	print("\n"+esp*(H-1) + car)  
	
	# les lignes intermédiaires
	# il y a H*2-3 lignes intermédiaires
	# sur chaque ligne, il y a des espaces avant le premier caractère (sauf sur celle du milieu), on note espAvant le nombre de ces espaces
	# sur chaque ligne, il y a des espaces entre les deux caractères, on note espEntre le nombre de ces espaces
	
	# Quand on passe d'une ligne intermédiaire du haut à la suivante, espAvant diminue de 1
	# Quand on passe d'une ligne intermédiaire du haut à la suivante, espEntre augmente de 2
	# C'est l'inverse qui se produit quand on passe d'une ligne intermédiaire du bas à la suivante
	
	espAvant = H-2 #le nombre d'espaces avant le premier caractère sur la première ligne intermédiaire du haut
	espEntre = 1 #le nombre d'espaces entre les deux caractères sur la première ligne intermédiaire du haut
	
	for h in range ( 2 , H ) : # pour chaque ligne intermédiaire du haut
		print(espAvant*esp + car + espEntre*esp + car)
		espAvant = espAvant - 1 # espAvant -= 1
		espEntre = espEntre + 2 # espEntre += 2
	
	for b in range ( 1 , H ) : # pour chaque ligne intermédiaire du bas
		print(espAvant*esp + car + espEntre*esp + car)
		espAvant = espAvant + 1 # espAvant += 1
		espEntre = espEntre - 2 # espEntre -= 2
		
	# affichage de la dernière ligne
	print(esp*(H-1) + car)

########################################################################
######################   PROGRAMME PRINCIPAL    ########################
#####################   LE SCRIPT DEBUTE ICI     #######################
########################################################################

# saisie du choix
H = int(input("Quelle est la hauteur du losange ? "))

while True :
        # Dans le cas ou la hauteur du losange est inférieur à 2
        if H < 2 :
                H=int(input("Veuillez choisir une hauteur supérieur ou égal à 2 : "))
        # Si supérieur ou égal à 2 on continue et on demande le caractère de dessin       
        else : 
                car = str(input("Quel est le caractère de dessin ? "))
                break

# Appel de la fonction                
losangeVide(H,car)



	
	
