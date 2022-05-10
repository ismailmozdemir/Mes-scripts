# !/bin/bash

# Saut de ligne
echo ""

# Demande de saisie à l'utilisateur de la borne supérieur
read -p "Saisissez la borne supérieur [100] : " borne

# Si aucune saisie de l'utilisateur, borne = 100 par défaut
if [ -z "$borne" ]; then
	borne=100
fi

# Définition de la variable résultat, qui est un nombre aléatoire entre 1 et la borne
resultat=$((RANDOM%$borne+1))

echo ""

# Demande de saisie à l'utilisateur d'un nombre entre 1 et la borne
read -p "Saisissez un nombre entre 1 et $borne : " nombre

# Tant que l'utilisateur ne trouve pas le résultat
while [ $resultat != $nombre ];do
	# Dans le cas ou le nombre saisie est plus grand que le résultat, on redemande la saisie du nombre
	if  [ $nombre -lt $resultat ]; then
		echo -e "\nLe nombre mystère est plus grand que $nombre.\n"
		read -p "Saisissez un nombre entre 1 et $borne : " nombre
	# Dans le cas ou le nombre saisie est plus petit que le résultat, on redemande la saisie du nombre
	else
		echo -e "\nLe nombre mystère est plus petit que $nombre.\n"
		read -p "Saisissez un nombre entre 1 et $borne : " nombre
	fi
done

# Sortie de la boucle car l'utilisateur a trouvé le résultat, message de félicitation
echo -e "\nBravo, le nombre mystère était $nombre !!"
