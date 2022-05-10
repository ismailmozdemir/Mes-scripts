# -*- coding: utf-8 -*-

'''
Dimanche 30/01/2022
Version 1
Définition d'une fonction à trois arguments qui encadre le premier argument avec une double cadre formé par les deux autres arguments
Le programme fait ensuite appel à la fonction en utilisant des arguments fournis par l'utilisateur.
'''

def encadre2fois(maPhrase,C1,C2) :
        """
        Encadre avec 2 caractères motifs une phrase quelconque
        Entrées :
                maPhrase : Une phrase quelconque
                C1 : Le premier caractère motif
                C2 : Le deuxième caractère motif
        Sortie :
                Aucune : il s'agit d'un affichage
        Exemple :
                Encradre avec 2 caractères une phrase comme ci-dessous
                encadre2fois("Bonjour à tous","*","#")
                
                ******************
                *################*
                *#Bonjour à tous#*
                *################*
                ******************
        """
        l=int(len(maPhrase))
        print ("\n"+C1 * (l + 4))
        print (C1 + (C2 *(l+ 2) + C1))
        print (C1 + (C2 + maPhrase + C2) + C1)
        print (C1 + (C2 *(l+ 2) + C1))
        print (C1 * (l + 4))

################################################
########## PROGRAMME PRINCIPAL  ################
################################################

# On demande une phrase et un premier puis un deuxième caractère puis on encadre la phrase avec ces 2 caractères
Phrase = str(input("Entrez votre phrase : "))
Car1 = str(input("Entrez le premier caractère : "))
Car2 = str(input("Entrez le deuxième caractère : "))
encadre2fois(Phrase,Car1,Car2)

