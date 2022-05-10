#! /bin/bash

# Attribution des constantes pointant vers le programme bash et le répertoire bin
stRepertoire='/bin'
stProgramme='/bin/bash'

# Pour afficher les 5 plus gros fichiers dans /bin/bash
echo -e "\nLes 5 fichiers les plus gros sont : $(ls -S $stRepertoire | head -n5 | tr '\n' ' ')"

# Pour afficher les 5 plus anciens fichiers dans /bin/bash
echo -e "\nLes 5 fichiers les plus anciens sont : $(ls -tr $stRepertoire | head -n5 | tr '\n' ' ')"

# Pour donner la taille du programme bash
echo -e "\nLa taille du fichier $stProgramme est : $(du -h $stProgramme | cut -f1)"

# Pour donner la dernière date de modification du programme bash
echo -e "\nLa date de modification du fichier $stProgramme est : $(ls -l --time-style=+"%d/%m/%Y" $stProgramme | cut -d ' ' -f6)\n"
