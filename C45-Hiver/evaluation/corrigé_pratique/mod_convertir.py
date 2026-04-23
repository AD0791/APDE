# Convertisseur de distance
# demander l'unité
print('=' * 50)
print('1. Convertir Km en mile')
print('2. Convertir mile en Km')
print('=' * 50)
option = int(input('Saisir une option (1-2):'))
if option == 1:  # km -> mile
    distance = float(input('Saisir la distance en km:'))
    distance_convertie = distance / 1.60935
elif option == 2:  # mile en km 1.60935
    distance = float(input('Saisir la distance en mile:'))
    distance_convertie = distance * 1.60935
else:
    print('Valeur invalide')

#affichage du resultat

if option == 1:  # km -> mile
    print(f'distance en km {distance:7.2f} equivalent à: {distance_convertie:7.2f} mile')
elif option == 2:  # mile en km 1.60935
    print(f'distance en mile {distance:7.2f} equivalent à: {distance_convertie:7.2f} km')
