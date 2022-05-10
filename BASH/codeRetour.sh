# !/bin/bash

# Si l'argument est un fichier, code retour 1
if [ -f $1 ]; then
	exit 1
# Si l'argument est un répertoire, code retour 2
elif [ -d $1 ]; then
	exit 2
# Si l'argument est un fichier spécial, code retour 3
elif [ -c $1 ]; then
	exit 3
# Si l'argument est un fichier qui n'existe pas, code retour 0
else
	exit 0
fi
