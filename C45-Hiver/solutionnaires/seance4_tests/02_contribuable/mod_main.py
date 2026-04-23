#Calcul impot à payer
TAUX = 0.85

#Saisir les données
nom = input('Saisir le nom:')
prenom = input('Saisir le prenom:')
revenu_total = float(input('Saisir le revenu total:'))
retrait_source = float(input('Saisir retrait à la source:'))

#Calcul du revenu reel
revenu_reel = revenu_total * TAUX - retrait_source
#determiner le taux
if revenu_reel < 10_000:
    taux_imposition = .15
elif revenu_reel < 30_000:
    taux_imposition = .25
elif revenu_reel < 100_000:
    taux_imposition = .35
else:
    taux_imposition = .55

#calculer impot
impot_payer = revenu_reel * taux_imposition
#afficher le relevé
print(f'Mr, Mme {nom}, {prenom}')
print(f'Montant:{revenu_total}$')
print(f'Retrait:{retrait_source}$')
print(f'Montant à payer:{impot_payer}$')