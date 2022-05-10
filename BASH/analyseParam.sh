# !/bin/bash

# Initialisation des variables, fichier qui va contenir les noms des fichiers et ext qui contient l'extension par défaut .save
fichier=""
ext=".save"

# Tant que le nombre de paramètres de position ayant une valeur est différent de 0
while (( $# )); do
	# Si un des paramètres de position est égal aux modèles ci-dessous
	case "$1" in
		# Pour tous les paramètres commençant de a à z, les paramètres sont concaténés dans la variable fichier
		[a-z]*)
			fichier="$fichier $1"
			shift;;
		# Si il y a un paramètre -v ou --verbose, alors la variable v=1
		-v|--verbose)
			v=1
			shift;;
		# Si il y a un paramètre -e ou --extension, alors la variable ext prend la valeur du deuxième paramètre après -e ou --extension
		-e|--extension)
			ext="$2"
			shift;;
		# Pour tous les autres paramètres
		*)
			shift;;
	esac
done

# On isole les noms des fichiers dans la variable fichier
set $fichier

# Tant que le nombre de paramètres de position ayant une valeur est différent de 0
while (( $# )); do
	# Si la variable v est égale à 1, alors affiche le mode bavard et informe l'utilisateur de l'avancement
	if [[ $v -eq 1 ]]; then
		echo "Sauvegarde de fichier $1 en $1$ext"
		cp "$1" "$1$ext"
		shift
	# Sinon copie sans informer l'utilisateur
	else
		cp "$1" "$1$ext"
		shift
	fi
done
