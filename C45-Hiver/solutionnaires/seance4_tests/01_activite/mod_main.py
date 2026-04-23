#Determination des activités
temperature = float(input('Saisir la température:'))
#tests multiples
if temperature < 2:
    activite = 'Ski'
elif temperature < 18:
    activite = 'Randonnée dans les bois'
elif temperature < 25:
    activite = 'Tennis'
else:
    activite = 'Natation'

print(f'Activité recommandée:{activite}')