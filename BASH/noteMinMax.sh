# !/bin/bash

# Saut de ligne
echo ""

# Demande de saisie des notes, que l'on stocke dans la variable tableauNotes sous forme de tableau
read -p "Saisir un tableau d'entier : " -a tableauNotes

# Initialisation des variables qui stocke la note la plus basse et la plus haute,
# pour l'instant il s'agit du premier élement de tableauNotes
minTableau=${tableauNotes[0]}
maxTableau=${tableauNotes[0]}

# Pour chaque éléments du tableau
for i in ${tableauNotes[*]}; do
	# Si la valeur de la variable minTableau est plus grande que l'élement de tableauNotes,
	# On met la valeur de cette élément dans minTableau
	if [ $minTableau -gt $i ]; then
		minTableau=$i
	# Sinon si, la valeur de la variable maxTableau est plus petite que l'élement de tableauNotes
	# On met la valeur de cette élément dans maxTableau
	elif [ $maxTableau -lt $i ]; then
		maxTableau=$i
	fi
done

# Affichage de la note maxi et mini
echo -e "\nNote minimale :" $minTableau
echo -e "\nNote maximale :" $maxTableau "\n"
