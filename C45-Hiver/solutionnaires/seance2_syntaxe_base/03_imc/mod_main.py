#calcul imc
poids = float(input('Saisir le poids:'))
taille = float(input('Saisir la taille:'))
imc = poids / taille ** 2
print('Votre imc est:', imc)