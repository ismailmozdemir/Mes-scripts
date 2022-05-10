# !/bin/bash

# Appel du script codeRetour sur le premier argument,
# pour tester si celui-ci est un répertoire et qu'il existe
./codeRetour.sh $1

# Si c'est un répertoire (code retour 2)
if [ $? -eq 2 ] ; then
	# Définition de la fonction analyseRepertoire
	function analyseRepertoire {
		# Pour tous les éléments de l'argument récursivement
		for i in $1/* ; do
			# Appel de la fonction pour tester les sous-répertoires/fichiers
			./codeRetour.sh $i
			# Dans le cas où le code retour est 2 (répertoire),
			# incrémentation de la variable rep et appel récursif de la fonction sur les éléments de l'argument.
			# Si c'est un fichier (les autres codes retour), incrémentation de la variable fic
			case $? in
				2)
					((rep++))
					analyseRepertoire $i;;
				*)
					((fic++));;
			esac
		done
	}

	# Appel de la fonction sur l'argument
	analyseRepertoire $1

	# Affichage du résultat
	echo -e "\nIl y a $rep sous-répertoires et $fic fichiers dans le répertoire $1\n"

# Si l'argument est un fichier ou si il n'existe pas, informer l'utilisateur
else
	echo -e "\n$1 n'est pas un répertoire ou n'existe pas\n"
fi
