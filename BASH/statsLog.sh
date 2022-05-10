# !/bin/bash

# Attribution de la variable jour (qui stocke la date du jour sous ce format AAAA/MM/JJ),
# de la variable log (résultat de la commande ls log), et de la constante rep utilisée pour spécifier
# le chemin complet des fichiers logs dans les commandes.
log=$(ls log)
rep=log/
jour=$(date +%Y%m%d)

# Pour chaque éléments de la variable log
for i in $log; do
	# Si l'élement se termine par .log et débute par une valeur égal à la variable jour
	if [ ${i:(-4)} == ".log" ] && [ ${i%%_*} == $jour ]; then
		# On incremente la variable fichiersLog
		# Puis on affiche les fichiers logs, puis le nombre d'erreurs et de warns pour chacun des fichiers
		# Enfin on incremente le nombre d'erreurs et de warns
		((fichiersLog++))
		echo -e "\n$i"
		echo "-- ERROR > $(more $rep$i | grep "ERROR" | wc -l)"
		((erreur+=$(more $rep$i | grep "ERROR" | wc -l)))
		echo "-- WARNING > $(more $rep$i | grep "WARNING" | wc -l)"
		((warn+=$(more $rep$i | grep "WARNING" | wc -l)))
	else
		# Sinon, on  incremente la variable autres, pour les fichiers ne correspondant pas aux critères
		# plus haut
		((autres++))
	fi
	# On incremente pour stocker le nombre total de fichiers dans la variable total
	((total++))
done

# Affichage des variables
echo -e "\nNombre de fichiers de log du jour : $fichiersLog\n"
echo -e "Nombre de fichiers dans le répertoire : $total\n"
echo -e "Nombre d'autres fichiers : $autres\n"
echo -e "Nombre total d'erreurs : $erreur\n"
echo -e "Nombre total d'avertissements : $warn\n"

