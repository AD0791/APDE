DIFF = 1
initial = int(input('Saisir valeur initiale:'))
chiffre = int(input('Saisir nombres désirés:'))
compteur = 1
while compteur <= chiffre and initial - DIFF * compteur >= 0:
    print(f'{initial - DIFF * compteur}')
    if initial - DIFF * compteur == 0:
        print('nombre négatif atteint !')
    compteur += 1