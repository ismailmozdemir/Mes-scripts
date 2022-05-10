# -*- coding: utf-8 -*-

'''
Date : 08/05/2022
Version : 1
Thème du script : Cherche dans tous les fichiers d'un dossier donné ceux qui contiennent des lignes commençant par un mot donné
et écrit dans un fichier rapport la liste des fichiers répondant au critère et ce récursivement.
On demande à l'utilisateur de choisir un répertoire et un mot, puis la fonction met au début la date du jour,
elle parcourt ensuite les fichiers de ce répertoire et si elle trouve le mot, elle met le répertoire, puis le fichier et la ligne de ce mot dans un rapport et ce récursivement
'''

# Importation des dépendances 
import os
import sys
from datetime import date

def rapport(repertoire,rechercheMot) :
    """
         Prend un répertoire et un mot recherché en entrée
         Elle met dans un rapport la date et si le mot est trouvé, elle met le répertoire,
         le fichier et la ligne du mot et ce récursivement
	 Entrées :
                  repertoire : Répertoire à parcourir récursivement
                  rechercheMot : Le mot recherché
	 Sortie :
		  Le rapport (rapport.txt)       
    """
    # Ouverture du rapport en écriture
    sys.stdout = open('rapport.txt','w')    
    # Écriture de la date dans le rapport
    print("Date :", date.today().strftime("%d/%m/%Y"))    
    # Initialisation des variables qui vont être utilisé par la suite pour tester si les noms de la racine et du fichier ont changé
    racine = ""
    ancienRacine = racine
    fichier = ""
    ancienFichier = fichier
    # Cette boucle parcourt le répertoire récursivement en recherchant les racines, les sous-répertoires et les fichiers
    # et en mettant ces résultats dans des tableaux
    for racine,sousRepertoires,fichiers in os.walk(repertoire):     
        # Pour tout fichier dans le tableau fichiers
        for fichier in fichiers :
            # On joint la racine et le fichier dans la variable cheminFichier, sans ça, la boucle n'arriverait pas à trouver le fichier en question
            cheminFichier = os.path.join(racine,fichier)
            # Ouverture de cheminFichier en tant "f"
            with open(cheminFichier) as f:
                # Pour chaque ligne du fichier "f" ainsi que son numéro dans ce fichier (en commençant par 1)
                for numero, ligne in enumerate(f,1):
                    # Si la ligne commence par le mot recherché, on affiche la racine (si elle a changé), le fichier (s'il a changé),
                    # la ligne et son numéro
                    if ligne.startswith(rechercheMot) :
                        if ancienRacine != racine :
                            print("\n------------------------------------------------------------------------------------------------------------\n")
                            print ("Dossier :",racine)
                        if ancienFichier !=  fichier :
                            print ("\n" + fichier)
                        print ("- Ligne",numero,":",ligne.strip())
                        # On met le nom de la racine et du fichier, dans leur variable "ancien" 
                        ancienRacine = racine
                        ancienFichier = fichier
    # Fermeture du rapport
    sys.stdout.close()

# On demande le nom du dossier à parcourir
dossier = str(input("Choisissez le dossier à parcourir : "))
# Si elle n'existe pas ou que ce n'est pas un dossier, on demande de le retaper
while not os.path.isdir(dossier) :
    print (dossier,"n'est pas un dossier, veuillez entrer un dossier valide et existant !")
    dossier = str(input("Choisissez le dossier à parcourir : "))
    
# On demande le mot recherché
rechercheMot = str(input("Entrez le mot recherché : "))

# Appel de la fonction
rapport(dossier,rechercheMot)
