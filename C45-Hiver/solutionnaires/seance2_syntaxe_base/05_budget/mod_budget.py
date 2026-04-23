#Gestion de budget
#Saisie de valeurs
prenom = input('Prénom du voyageur:')
distance = float(input('Distance du trajet (en km)):'))
consommation = float(input('Consommation voiture (L/100km):'))
prix = float(input("Prix de l'essence ($/L) : "))
budget_nourriture =float(input('Budget nourriture ($) :'))
#Calcul
# essence = (distance / 100) * consommation * prix_essence
essence = (distance /100) * consommation * prix
peage = essence * 0.30
total = essence + peage + budget_nourriture

#Affichage
print('Voyageur:', prenom)
print('Distance:', distance, 'km')
print(' ')
print('Détails des couts:')
print('-Essence:', essence, '$')
print('-Péage(30%):', peage,'$')
print('-Nourriture:', budget_nourriture,'$')
print('=' * 50)
print('Budget total', total,'$')
print('Bon voyage', prenom,'!')