DIFF = 3
initial = int(input('Saisir valeur initiale:'))
chiffre = int(input('Saisir nombres désirés:'))
for compteur in range(1,chiffre+1):
    print(f'{initial + DIFF * compteur}')
