#Saisir les données
TAUX = 0.85
nom = input('Saisir le nom:')
prenom = input('Saisir le prenom:')
revenu_total = float(input('Saisir le revenu:'))
retrait_source = float(input('Saisir votre retrait:'))
#calcul du rrevenu reel
revenu_reel = revenu_total * TAUX - retrait_source
#determination du taux
if revenu_reel < 10_000:
    taux = .15
elif revenu_reel < 30_000:
    taux = .25
elif revenu_reel < 100_000:
    taux = .35
else:
    taux = .55

#calcul impot
impot_payer = revenu_reel * taux
#affichage
print(f'Mr, Mme {nom}, {prenom}')
print("Merci d'avoir rempli la déclaration")
print(f'Montant declaré:{revenu_total:7.1f}')
print(f'Montant retrait:{retrait_source:7.1f}')
print(f'Montant à payer:{impot_payer:7.1f}')
