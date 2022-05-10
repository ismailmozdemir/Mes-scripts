# -*- coding: utf-8 -*-

'''
Samedi 11/12/2021
Version 1
Ecriture d'un programme générique qui demande à l'utilisateur le prix de l'article ainsi que la remise
et qui affiche le montant de la remise et le prix final de l'article avec la remise
'''

#On demande le prix de l'article
PrixArticle = float(input("Prix de l'article? \n"))
#On demande le % de la reduction
Reduction = int(input("Pourcentage de la réduction?\n"))
#On formate la réduction pour pouvoir effectuer des opérations
PourcentageReduction = float(Reduction/100)
#On calcule le montant de la réduction
MontantReduction = float(PrixArticle*PourcentageReduction)
#On calcule le prix de l'article soldé
PrixFinal =(PrixArticle-MontantReduction)
#On présente à l'utilisateur les informations au bon format
print("Pour un article à un prix initial de" ,("%.2f" % PrixArticle),"€ et soldé à" ,Reduction,"% :" )
print("Le montant de la réduction est" ,("%.2f" % MontantReduction), "€.")
print("Le prix soldé est" ,("%.2f" % PrixFinal),"€.")
