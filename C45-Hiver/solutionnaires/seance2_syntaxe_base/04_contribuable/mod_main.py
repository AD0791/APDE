#Calcul de remboursement
#Saisie des données
nom = input('Saisir le nom:')
prenom = input('Saisir le prenom:')
courriel = input('Saisir le courriel:')
montant = float(input('Montant à payer pour les travaux:'))
contribution = float(input('Votre contribution:'))

#calcul
remboursement = montant * 0.85 - contribution

#affichage
print('=' * 50)
print('Mr, Mme', nom, ',', prenom)
print(courriel)
print("Merci d'avoir fait la demande de remboursement \n"
      " des frais d'assurance")
print('Voici les montants qui vous intéressent')
print('Montant des travaux nécessaires:', montant,'$')
print('Votre contribution déclarée:', contribution,'$')
print('-' * 50)
print('Remboursement auquel vous avez droit:', remboursement,'$')