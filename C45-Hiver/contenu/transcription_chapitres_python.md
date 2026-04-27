# Notes transcrites — Python

> Transcription réalisée à partir des photos fournies.  
> Certaines lignes très floues ou coupées peuvent nécessiter une vérification avec le livre original.

---

# Table des matières

## 1. Environnement de développement
- **1.1** Manipulation 1 : Installation de Python — p. 2
- **1.2** Manipulation 2 : Installation de l’IDE PyCharm — p. 5
- **1.3** Manipulation 3 : Prise en main de l’IDE PyCharm — p. 9
- **1.4** Manipulation 4 : Modification d’instructions de sortie — p. 12

## 2. Syntaxe de base — p. 13
- **Exercice 2.1** : Utilisation des fonctions `input()` et `print()` — p. 14
- **Exercice 2.2** : Conversion de données — p. 14
- **Exercice 2.3** : Saisie et conversion de valeurs avec utilisation d’opérateurs arithmétiques — p. 14
- **Exercice 2.4** : Détermination du type d’une variable — p. 15
- **Exercice 2.5** : Vérification du type d’une variable — p. 16
- **Exercice 2.6** : Utilisation des opérateurs division, division entière et modulo — p. 16
- **Exercice 2.7** : Conversion explicite de valeurs — p. 17
- **Exercice 2.8** : Priorité des opérateurs arithmétiques — p. 17
- **Exercice 2.9** : Priorité des opérateurs relationnels et logiques — p. 18
- **Exercice 2.10** : Utilisation de l’opérateur modulo — p. 19
- **Exercice 2.11** : Formatage de données en sortie — p. 19

## 3. Structures de test — p. 21
- **Exercice 3.1** : Utilisation des tests à une et à deux voies — p. 22
- **Exercice 3.2** : Utilisation d’opérateurs logiques et relationnels dans la condition — p. 22
- **Exercice 3.3** : Utilisation du test à deux voies — p. 23
- **Exercice 3.4** : Utilisation du test multi-voies — p. 24
- **Exercice 3.5** : Utilisation du test multi-voies comme menu de sélection — p. 25
- **Exercice 3.6** : Utilisation du test multi-voies comme menu de sélection — p. 26
- **Exercice 3.7** : Test multi-voies sur plusieurs niveaux — p. 27
- **Exercice 3.8** : Test multi-voies avec utilisation d’une règle d’affaire simple — p. 28
- **Exercice 3.9** : Test multi-voies avec utilisation d’une règle d’affaire — p. 29
- **Exercice 3.10** : Test multi-voies avec utilisation d’une règle d’affaire complexe — p. 30
- **Exercice 3.11** : Menu de sélection conditionnel — p. 32
- **Exercice 3.12** : Utilisation de l’opérateur conditionnel — p. 34

## 4. Structures de boucle — p. 35
- **Exercice 4.1** : Utilisation de la boucle `while` (1) — p. 36
- **Exercice 4.2** : Utilisation de la boucle `while` (2) — p. 36
- **Exercice 4.3** : Utilisation de la boucle `while` (3) — p. 37
- **Exercice 4.4** : Utilisation de la boucle `while` avec une variable sentinelle — p. 39
- **Exercice 4.5** : Utilisation de la boucle `for` sur un itérable — p. 40
- **Exercice 4.6** : Utilisation de la boucle `for` avec la fonction `range` (1) — p. 41
- **Exercice 4.7** : Utilisation de la boucle `for` avec la fonction `range` (2) — p. 42
- **Exercice 4.8** : Utilisation de la boucle `for` avec la fonction `range` — p. 43
- **Exercice 4.9** : Utilisation de la boucle `for` avec la fonction `range` et `randint` — p. 44

---

# Chapitre 2 — Syntaxe de base

## Connaissances requises

- Comprendre la structure d’un programme Python
- Comprendre ce qu’est une variable
- Identifier les types de données (`str`, `int`, `float`)
- Identifier les opérateurs arithmétiques
- Identifier les opérateurs relationnels
- Identifier les opérateurs logiques
- Comprendre comment faire une conversion de type

---

## Exercice 2.1

Demander à l’utilisateur son nom et afficher le résultat sous le format suivant :

```text
Bonjour nom_utilisateur
```

Sachant que `nom_utilisateur` est celui saisi par l’utilisateur.

Exemple : si l’utilisateur saisit `Flouflou`, on affichera :

```text
Bonjour Flouflou
```

### Solution

On utilise ici la fonction `input()` pour la saisie du nom qui est une chaîne de caractères.  
La fonction `print()` est utilisée pour l’affichage.

```python
nom_utilisateur = input('Saisir votre nom:')
print('Bonjour {}'.format(nom_utilisateur))
```

---

## Exercice 2.2

Demander à l’utilisateur son salaire et lui ajouter 500. Afficher le résultat sous le format suivant :

```text
Votre nouveau salaire est nouveau_salaire
```

Sachant que `nouveau_salaire` est la valeur finale du salaire.

Exemple : si l’utilisateur saisit `1200`, on affichera :

```text
Votre nouveau salaire est 1700.00
```

### Solution

On utilise ici la fonction `input()` pour la saisie du salaire. Étant donné que l’on va faire des calculs sur la valeur reçue, on procède à une conversion en utilisant `float()`.

```python
salaire = float(input('Saisir votre salaire:'))
salaire += 500
print('Votre nouveau salaire est: {0:7.2f}'.format(salaire))
```

---

## Exercice 2.3

Saisir le nom d’un étudiant, ses notes d’examen intra et final et afficher le résultat sous la forme suivante :

```text
Nom étudiant : nom_etudiant Moyenne : moyenne_etudiant
```

La moyenne est égale à :

```text
0.4 * examen_intra + 0.6 * examen_final
```

Ici, `nom_etudiant` est le nom de l’étudiant, `examen_intra` et `examen_final` sont les notes de l’examen intra et final.

Exemple : si l’utilisateur saisit `Flouflou`, `65` et `70`, on affichera :

```text
Nom étudiant : Flouflou Moyenne : 68
```

### Solution

On utilise ici la fonction `input()` pour la saisie du nom qui est une chaîne de caractères et la fonction `print()` pour l’affichage. Pour les notes d’examen, on doit faire une conversion en utilisant `float()` car celles-ci vont être utilisées dans des opérations arithmétiques.

```python
nom_etudiant = input('Saisir le nom étudiant:')
examen_intra = float(input('Saisir la note intra:'))
examen_final = float(input('Saisir la note du final:'))
moyenne_etudiant = 0.4 * examen_intra + 0.6 * examen_final
print('Nom étudiant: {} Moyenne:{}'.format(nom_etudiant, moyenne_etudiant))
```

---

## Exercice 2.4

On veut identifier le type d’une variable en utilisant la fonction `type()`.

Soit les valeurs suivantes :

```text
10, 1000000000000, -10, 10.10, '10', True
```

Identifier les types de chacune de ces valeurs en affectant en premier la valeur à une variable.

### Solution

On utilise ici la fonction `type()`. Celle-ci retourne le type exact de la valeur passée en paramètre.

```python
var_1 = 0
var_2 = 1000000000000
var_3 = -10
var_4 = 10.10
var_5 = '10'
var_6 = True

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))
print(type(var_5))
print(type(var_6))
```

---

## Exercice 2.5

Développer le code qui permet de vérifier si une variable `var1` est du type `float`.

On utilisera la fonction `isinstance(votre_variable, type)` pour la vérification.  
La valeur de test à utiliser sera `48.5`.

### Solution

On utilise `isinstance(var_1, float)` pour faire la vérification du type d’une variable.

```python
var1 = float(input('Saisir une valeur réelle:'))
resultat = isinstance(var1, float)
print(resultat)
```

---

## Exercice 2.6

Écrire le code qui donne la division des variables `var1` par `var2`, le reste de la division et la division entière de `var1` par `var2`.

- On demandera à l’usager les valeurs pour `var1` et `var2`. Comme valeurs de test, on utilisera les valeurs initiales `20` et `8`.
- On utilise les variables `div`, `reste` et `div_entiere` pour stocker les résultats de la division, modulo et division entière.
- Ajouter les instructions pour afficher les valeurs de `var1`, `var2` et les résultats de la division, modulo et division entière.
- Qu’est-ce que vous remarquez ?

### Solution

On fait attention ici à différencier la division entière de la division réelle.

```python
var1 = 20
var2 = 8
div = var1 / var2
reste = var1 % var2
div_entiere = var1 // var2

print('La division de {} par {} donne:{}'.format(var1, var2, div))
print('Le reste de la division de {} par {} donne:{}'.format(var1, var2, reste))
print('La division entière de {} par {} donne:{}'.format(var1, var2, div_entiere))
```

---

## Exercice 2.7

On utilisera la conversion explicite de valeurs lors de calculs arithmétiques.

- Demander à l’utilisateur deux valeurs numériques en utilisant la fonction `input()`.
- Afin de réaliser la somme des deux valeurs, effectuer la conversion des valeurs obtenues en utilisant `float()` et afficher le résultat obtenu.

### Solution

Même si on pouvait convertir la valeur au moment de la saisie, on a préféré ici faire la conversion au moment de l’utilisation de la valeur. Pour cela, la fonction `float()` est appliquée sur la variable au lieu qu’elle le soit sur le retour de la fonction `input()`.

```python
val_1 = input('Saisir valeur 1:')
val_2 = input('Saisir valeur 2:')
resultat = float(val_1) + float(val_2)
print(resultat)
```

---

## Exercice 2.8

Écrire un programme qui demande à l’utilisateur d’entrer trois nombres entiers et effectue les opérations suivantes dans l’ordre indiqué :

- Calcule la somme des deux premiers nombres et multiplie le résultat par le troisième nombre.
- Soustrait le troisième nombre du résultat obtenu à l’étape 1.
- Divise le résultat obtenu à l’étape 2 par la somme des trois nombres.
- Affiche le résultat final.

### Solution

Le programme effectue les opérations conformément à la précédence des opérateurs, calcule le résultat final et l’affiche.

On remarque l’utilisation des parenthèses au niveau de l’addition étant donné que la multiplication et la division ont une plus grande précédence que l’addition.

```python
# Demander à l'utilisateur d'entrer trois nombres entiers
nombre1 = int(input("Entrez le premier nombre : "))
nombre2 = int(input("Entrez le deuxième nombre : "))
nombre3 = int(input("Entrez le troisième nombre : "))

# Calculer la somme des deux premiers nombres et multipliez le résultat par le troisième nombre
resultat1 = (nombre1 + nombre2) * nombre3

# Soustraire le troisième nombre du résultat obtenu à l'étape 1
resultat2 = resultat1 - nombre3

# Diviser le résultat obtenu à l'étape 2 par la somme des trois nombres
resultat_final = resultat2 / (nombre1 + nombre2 + nombre3)

# Afficher le résultat final
print("Le résultat final est : {}".format(resultat_final))
```

---

## Exercice 2.9

Écrire un programme qui demande à l’utilisateur d’entrer deux nombres entiers `a` et `b`.

Soit l’expression :

```text
((a > 3) and (a < 10)) or ((4 >= b) and (b != 2))
```

Éliminer les parenthèses superflues sans affecter l’ordre des opérations.

### Solution

On applique les règles de précédence entre les opérateurs en faisant attention aux opérandes. L’opérateur principal dans cette expression est `or`.

```python
a = int(input('Saisir une valeur entière 1:'))
b = int(input('Saisir une valeur entière 2:'))

valeur_1 = ((a > 3) and (a < 10)) or ((4 >= b) and (b != 2))
valeur_2 = a > 3 and a < 10 or 4 >= b and b != 2

print(valeur_1)
print(valeur_2)
```

---

## Exercice 2.10

Développer un programme qui donne les coupures de billets à rendre aux clients lors de leurs achats. Les caissiers ou caissières vont saisir le total à payer et le montant remis par le client en argent comptant. Le système doit afficher ce qu’il faut rendre aux clients.

Hypothèses :

- Le montant total est toujours un entier.
- Les billets disponibles sont `1$`, `5$`, `10$` et `20$` seulement.

### Solution

En premier, on devrait vérifier que le montant remis est supérieur au montant total. Étant donné que l’on n’a pas encore pratiqué les structures de test, on a omis cette vérification.

La solution proposée ici utilise l’opérateur de division entière ainsi que l’opérateur modulo.

```python
montant_remis = int(input('Saisir le montant remis:'))
montant_total = int(input('Saisir le montant total:'))

change = montant_remis - montant_total

cp_vingt = change // 20
cp_dix = (change % 20) // 10
cp_cinq = (change % 10) // 5
cp_un = change - cp_vingt * 20 - cp_dix * 10 - cp_cinq * 5

print('Vingt: {0}, Dix: {1}, Cinq:{2}, Un:{3}'.format(
    cp_vingt, cp_dix, cp_cinq, cp_un))
```

---

## Exercice 2.11

Écrire le code qui demande à l’usager de saisir son nom, âge et taille. On nous indique que le nom est une chaîne de caractères, l’âge est un entier et la taille est un réel.

Afficher les informations de cet usager en utilisant la méthode `format()`.

### Solution

Le formatage de données avec la méthode `format()` est très flexible pour incorporer des valeurs dans des chaînes de caractères. Elle permet de spécifier la précision des nombres, la largeur des champs, le formatage des dates, etc. en utilisant des spécifications de format appropriées.

Dans cet exercice, nous avons une variable `nom`, une variable `age` et une variable `taille`.

La méthode `format()` est utilisée pour formater les données dans la chaîne de caractères `message`.

Dans la chaîne de formatage, nous utilisons des accolades comme espaces réservés pour les valeurs que nous voulons insérer.

Les accolades sans index sont remplacées par les valeurs dans l’ordre des arguments fournis à la méthode `format()`.

L’index `:.2f` utilisé avec `{}` permet de formater `taille` en tant que nombre à virgule flottante avec deux décimales.

```python
nom = input('Saisir votre nom:')
age = int(input('Saisir votre age:'))
taille = float(input('Saisir votre taille:'))

# Formatage de données à l'aide de la méthode format()
message = "Votre nom est: {}, age est : {} ans. Votre taille est {:.2f} mètres.".format(nom, age, taille)

# Affichage du message formaté
print(message)

# Formatage de données à l'aide de la méthode format() en utilisant les index
message = "Votre nom est: {0:12s}, age est: {1:3d} ans. Votre taille est {2:.2f} mètres.".format(nom, age, taille)
print(message)
```

---

# Chapitre 3 — Structures de test

## Connaissances requises

- Utiliser une expression conditionnelle
- Utiliser des opérateurs relationnels dans les expressions conditionnelles
- Utiliser des opérateurs logiques dans les expressions conditionnelles
- Développer des structures de test `if`, `if-else` et `if-elif`
- Utiliser l’opérateur ternaire de test conditionnel

---

## Exercice 3.1

Demander à l’utilisateur trois nombres entiers. Ceux-ci seront stockés dans les variables `a`, `b` et `c`. Trouver le maximum et le minimum.

### Solution

Dans la première solution, on compare les deux variables `a` et `b` à l’aide du test à une voie. Le résultat sera ensuite comparé à la variable `c`.

```python
###### Solution 1 ######
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))

maximum = a
minimum = b

if b > a:
    maximum = b
    minimum = a

if maximum < c:
    maximum = c
elif minimum > c:
    minimum = c

print(minimum, maximum)
```

Une autre solution qui utilise l’affectation simultanée est la suivante :

```python
###### Solution 2 ######
a = int(input('Saisir a:'))
b = int(input('Saisir b:'))
c = int(input('Saisir c:'))

maximum, minimum = a, b

if b > a:
    maximum, minimum = b, a

if maximum < c:
    maximum = c
elif minimum > c:
    minimum = c

print(minimum, maximum)
```

---

## Exercice 3.2

Écrire un programme qui demande à l’utilisateur d’entrer un nombre entier et vérifie si ce nombre est pair et compris entre 10 et 100 inclusivement. Le programme doit afficher un message approprié selon le résultat.

### Solution

L’utilisateur saisit le nombre. Le programme vérifie si le nombre est pair en utilisant l’opérateur modulo avec la condition `% 2 == 0` et s’il est compris entre 10 et 100. Si les deux conditions sont satisfaites, le programme affiche le message `Le nombre est pair et compris entre 10 et 100.` Sinon, il affiche le message `Le nombre n’est pas pair et/ou n’est pas compris entre 10 et 100.`

```python
# Demander à l'utilisateur d'entrer un nombre entier
nombre = int(input("Entrez un nombre entier : "))

# Vérifier si le nombre est pair et compris entre 10 et 100
if nombre % 2 == 0 and nombre >= 10 and nombre <= 100:
    print("Le nombre est pair et compris entre 10 et 100.")
else:
    print("Le nombre n'est pas pair et/ou n'est pas compris entre 10 et 100.")
```

---

## Exercice 3.3

Une épicerie vend des produits sous différents formats de poids. Développer le code qui demande à l’utilisateur le nom, le poids et le prix du produit. On suppose que pour l’exemple, on n’a que deux formats.

Afficher à la fin le format qui est meilleur marché.

### Solution

On demande à l’utilisateur d’entrer le nom, le poids et le prix pour chaque format du produit. Ensuite, on calcule le prix par unité de poids pour chaque format en divisant le prix par le poids.

Enfin, on compare les deux prix par unité de poids pour déterminer le format le moins cher et afficher le résultat.

```python
# Demander à l'utilisateur le nom du produit, le poids et le prix pour chaque format
nom_produit = input("Entrez le nom du produit : ")
poids1 = float(input("Entrez le poids du premier format : "))
prix1 = float(input("Entrez le prix du premier format : "))
poids2 = float(input("Entrez le poids du deuxième format : "))
prix2 = float(input("Entrez le prix du deuxième format : "))

# Calcul du prix par unité de poids pour chaque format
prix_unite1 = prix1 / poids1
prix_unite2 = prix2 / poids2

# Comparaison des deux prix par unité de poids pour déterminer le format le moins cher
if prix_unite1 < prix_unite2:
    format_choisi = "Format 1"
    prix_format = prix_unite1
else:
    format_choisi = "Format 2"
    prix_format = prix_unite2

# Affichage du format choisi
print("Le format le moins cher pour {} est {} à un prix de {} par unité de poids.".format(
    nom_produit, format_choisi, prix_format))
```

---

## Exercice 3.4

Écrire le code qui effectue le taux de change de dollars américains en dollars canadiens ou vice-versa. Demander à l’utilisateur de saisir `0` pour convertir des dollars américains en dollars canadiens et `1` pour convertir des dollars canadiens en dollars américains. Ensuite, l’utilisateur devra saisir le montant en dollars américains ou dollars canadiens pour la conversion selon le choix désiré.

On prendra comme taux de change actuel `1.21`, ce qui nous donne `1.21` dollar canadien pour un dollar américain.

### Solution

Dans cette solution, on utilise un test à plusieurs voies étant donné que l’utilisateur peut saisir un choix invalide autre que les valeurs `0` ou `1`.

On remarque aussi que les valeurs saisies sont converties selon le besoin.

```python
TAUX_CHANGE = 1.21

# Demander à l'utilisateur de saisir 0 pour convertir des dollars américains en dollars canadiens
# et 1 pour convertir des dollars canadiens en dollars américains
choix = int(input("Entrez 0 pour convertir des dollars américains en dollars canadiens\n ou 1 pour convertir des dollars canadiens en dollars américains: "))

# Demander à l'utilisateur de saisir le montant à convertir
montant = float(input("Entrez le montant à convertir: "))

if choix == 0:
    # Conversion de dollars américains en dollars canadiens
    taux = TAUX_CHANGE
    montant_converti = montant * taux
    print("${0:.2f} USD est égal à ${1:.2f} CAD".format(montant, montant_converti))

elif choix == 1:
    # Conversion de dollars canadiens en dollars américains
    taux = 1 / TAUX_CHANGE
    montant_converti = montant * taux
    print("${0:.2f} CAD est égal à ${1:.2f} USD".format(montant, montant_converti))

else:
    print("Choix invalide. Veuillez entrer 0 ou 1 pour choisir la conversion désirée.")
```

---

## Exercice 3.5

Dans certains pays dont le Canada, certains mesurent les distances en pieds alors qu’officiellement les mesures devraient être en mètres. Afin d’aider ces personnes, développer un programme qui permet de faire la conversion de mètres vers pieds sachant qu’un pied équivaut à `30.48 cm` environ.

Modifier votre code pour faire la conversion inverse. Ajouter un prompt au début afin de demander le type de conversion désirée.

### Solution

On effectue ici la conversion selon l’échelle choisie. On aurait pu choisir un test à deux voies mais comme l’utilisateur peut choisir des valeurs non prises en compte, on a opté pour un test à plusieurs voies `if-elif-else`.

```python
# conversion de mètres vers pieds, solution 1
distance = float(input('Saisir la distance en metres:'))
distance_convertie = distance / .3048
print('La distance en pieds est:{0:7.2f}'.format(distance_convertie))
```

Une solution plus élaborée qui offre un menu de choix de conversion est la suivante :

```python
# conversion de mètres vers pieds et pied en mètres
distance = float(input('Saisir la distance à convertir:'))
option = int(input('Saisir option 1 ou 2 \n1. Convertir metres en pieds\n2. Convertir pieds en metres\n'))

if option == 1:
    distance_convertie = distance / .3048
    print('La distance en pieds est:{0:7.2f}'.format(distance_convertie))
elif option == 2:
    distance_convertie = distance * .3048
    print('La distance en metres est:{0:7.2f}'.format(distance_convertie))
else:
    print('Option choisie est invalide')
```

---

## Exercice 3.6

Une chaîne de distribution alimentaire internationale propose ses produits en kilogramme pour la majorité de ses clients. Afin d’aider ses clients qui utilisent le système impérial, elle désire leur fournir la même information mais en livre. Développer le programme qui permet de faire la conversion de kilogramme vers livre sachant qu’un kilogramme équivaut à `2.2` livres.

Modifier votre code pour faire la conversion inverse. Ajouter un prompt au début afin de demander le type de conversion désirée.

### Solution

On effectue ici la conversion selon l’échelle de poids choisie. Comme l’utilisateur peut choisir des valeurs non prises en compte, on a opté pour un test à plusieurs voies.

```python
# conversion de kilogramme vers livre, solution 1
poids = float(input('Saisir le poids en kilo:'))
poids_converti = poids * 2.2
print('Le poids en livre est:{0:7.2f}'.format(poids_converti))
```

Une solution plus élaborée qui offre un menu de choix de conversion est la suivante :

```python
# conversion de kilogramme vers livre et livre vers kilogramme
poids = float(input('Saisir le poids à convertir:'))
option = int(input('Saisir option 1 ou 2 \n1. Convertir kilogramme en livre\n2. Convertir livre en kilogramme\n'))

if option == 1:
    poids_converti = poids * 2.2
    print('Le poids en livre est:{0:7.2f}'.format(poids_converti))
elif option == 2:
    poids_converti = poids / 2.2
    print('Le poids en kilo est:{0:7.2f}'.format(poids_converti))
else:
    print('Option choisie est invalide')
```

---

## Exercice 3.7

Développer un programme qui demande à l’utilisateur un nombre correspondant à un mois de l’année puis affiche le nom du mois associé avec le nombre saisi. Dans le cas où le nombre saisi ne correspond pas à un mois valide, on affichera un message d’erreur et on arrête le programme.

### Solution

Une solution basique, mais non pythonique, commence par la saisie d’un nombre correspondant à un mois de l’année. Si le nombre saisi correspond à un mois valide entre `1` et `12`, le programme affiche le nom du mois associé. Sinon, il affiche un message d’erreur.

```python
# Afficher le mois en toute lettre
# Il y'a d'autres solutions plus élégantes que celle-ci
option = int(input('Saisir le mois désiré 1-12:'))

if option == 1:
    mois = 'Janvier'
elif option == 2:
    mois = 'Fevrier'
elif option == 3:
    mois = 'Mars'
elif option == 4:
    mois = 'Avril'
elif option == 5:
    mois = 'Mai'
elif option == 6:
    mois = 'Juin'
elif option == 7:
    mois = 'Juillet'
elif option == 8:
    mois = 'Aout'
elif option == 9:
    mois = 'Septembre'
elif option == 10:
    mois = 'Octobre'
elif option == 11:
    mois = 'Novembre'
elif option == 12:
    mois = 'Decembre'
else:
    mois = 'invalide'

print('Le mois choisi est:{}'.format(mois))
```

---

## Exercice 3.8

Pour les besoins du calcul d’imposition, on classe les salariés en catégories de salaire.

Pour les plus de `100 000$`, le taux est `45%`.  
Pour ceux entre `70 000$` et moins de `100 000$`, le taux est de `32%`.  
Pour ceux entre `40 000$` et moins de `70 000$`, le taux est de `18%`.  
Ceux qui gagnent moins de `40 000$` sont imposés à hauteur de `10%`.

Développer le programme qui demande à l’utilisateur son salaire et lui affiche ensuite le montant qu’il doit payer.

### Solution

On reçoit le salaire d’un employé et on calcule l’impôt sur le revenu en fonction de sa catégorie de salaire. Si le salaire est négatif, un message d’erreur est affiché. Sinon, l’impôt sur le revenu est calculé et affiché à l’écran.

```python
salaire = float(input('Saisir votre salaire:'))

if salaire < 0:
    print("Erreur: le salaire ne peut pas être négatif.")
else:
    if salaire >= 100000:
        taux_imposition = 0.45
    elif salaire >= 70000:
        taux_imposition = 0.32
    elif salaire >= 40000:
        taux_imposition = 0.18
    else:
        taux_imposition = 0.1

    impot = salaire * taux_imposition

    # Formatage avec f-strings
    print(f"Pour un salaire de {salaire:.2f}$, l'impôt sur le revenu est de {impot:.2f}$.")
```

---

## Exercice 3.9

Développer le code qui calcule le montant de la rémunération d’un vendeur à commission. Celui-ci a un salaire de base de `5000$`. L’utilisateur doit saisir le montant total des ventes, qui doit être positif, pour le mois. Si le montant total est négatif, on doit afficher un message d’erreur.

Le taux de commission est défini par l’échelle suivante :

- moins de `1000$` : `2.5%`
- `1001$` à `5000$` : `5%`
- plus de `5000$` : `7.5%`

Afficher le montant du salaire formaté avec deux décimales et le symbole du dollar.

### Solution

En fonction du montant des ventes, le taux de commission est déterminé en utilisant une série de conditions `if/elif/else`. Le montant de la commission est ensuite calculé en multipliant le montant des ventes par le taux de commission. Le salaire total est ensuite calculé en ajoutant le montant de la commission au salaire de base de `5000$`.

```python
ventes = float(input("Entrez le montant total des ventes pour le mois: "))

if ventes < 0:
    print("Erreur: le montant des ventes ne peut pas être négatif.")
else:
    if ventes < 1000:
        taux_commission = 0.025
    elif ventes <= 5000:
        taux_commission = 0.05
    else:
        taux_commission = 0.075

    commission = ventes * taux_commission
    remuneration = commission + 5000  # 5000 $ est le salaire de base

    print("La rémunération du vendeur est de {0:.2f}$".format(remuneration))
```

---

## Exercice 3.10

Développer un programme qui prépare le relevé mensuel des clients pour la compagnie MasterPop International, une banque qui délivre des cartes de crédit.

### Données

Le programme a comme entrée le solde précédent du compte, le versement effectué par le client et le montant total des charges additionnelles (achats) durant le mois.

Le solde courant est le solde précédent moins le versement effectué par le client. Le programme devra calculer l’intérêt dû pour le mois, le nouveau solde total et le minimum à payer.

La règle d’affaire utilisée par MasterPop International pour le calcul de l’intérêt est basée sur le solde courant. Ainsi, si le solde courant est `0`, l’intérêt appliqué pour le mois courant est `0%`. Si le solde courant est supérieur à `0`, l’intérêt appliqué est de `5%` sur le total actuel, soit le solde courant plus les charges additionnelles.

### Besoins

Le programme devra calculer le minimum à payer. La règle d’affaire pour le calcul du minimum à payer est basée sur le nouveau solde.

- Si le nouveau solde est de moins de `50$`, alors le minimum à payer sera le montant du nouveau solde.
- Si le nouveau solde est entre `50$` et `295$`, alors le minimum à payer est de `50$`.
- Si le nouveau solde dépasse `295$`, alors le minimum à payer est de `25%` du nouveau solde.

### Format d’affichage

La sortie du programme devra avoir la forme suivante :

```text
MasterPop International
Relevé mensuel des charges
Solde précédent : XXXX.XX $
Versement : XXXX.XX $
Solde courant : XXXX.XX $
Frais d’intérêt : XXXX.XX $
Achats : XXXX.XX $
Nouveau solde : XXXX.XX $
Minimum exigé : XXXX.XX $
```

### Solution

Le programme commence par définir les constantes pour le calcul du minimum à payer. Ensuite, il lit les entrées utilisateur : le solde précédent, le versement et le montant total des charges additionnelles.

À partir de ces données, il calcule le solde courant et l’intérêt dû selon les règles d’affaire spécifiées. Il calcule ensuite le nouveau solde et le minimum à payer.

```python
# Définition des constantes pour le calcul du minimum à payer
MINIMUM_1 = 50
MINIMUM_2 = 295
TAUX_MINIMUM_3 = 0.25

# Lecture des entrées utilisateur
solde_precedent = float(input("Entrez le solde précédent du compte: "))
versement = float(input("Entrez le versement effectué par le client: "))
achats = float(input("Entrez le montant total des charges additionnelles (achats): "))

# Calcul du solde courant et de l'intérêt dû
solde_courant = solde_precedent - versement

if solde_courant <= 0:
    frais_interet = 0
else:
    frais_interet = (solde_courant + achats) * 0.05

# Calcul du nouveau solde et du minimum à payer
nouveau_solde = solde_courant + achats + frais_interet

if nouveau_solde < MINIMUM_1:
    minimum_a_payer = nouveau_solde
elif nouveau_solde < MINIMUM_2:
    minimum_a_payer = MINIMUM_1
else:
    minimum_a_payer = nouveau_solde * TAUX_MINIMUM_3

# Affichage du relevé mensuel des charges
print("MasterPop International")
print("Relevé mensuel des charges")
print("Solde précédent :", format(solde_precedent, ".2f"), "$")
print("Versement :", format(versement, ".2f"), "$")
print("Solde courant :", format(solde_courant, ".2f"), "$")
print("Frais d'intérêt :", format(frais_interet, ".2f"), "$")
print("Achats :", format(achats, ".2f"), "$")
print("Nouveau solde :", format(nouveau_solde, ".2f"), "$")
print("Minimum à payer :", format(minimum_a_payer, ".2f"), "$")
```

---

## Exercice 3.11

Développer un programme qui demande à l’utilisateur deux nombres, les stocke dans deux variables préalablement définies puis affiche : la somme, le produit et la différence des deux nombres.

On fournira à l’utilisateur un menu simple similaire au suivant :

```text
Addition
Soustraction
Multiplication
Quitter
```

On utilisera une structure de test appropriée.

- Si l’utilisateur choisit l’option `1`, `2` ou `3`, on demande la saisie des deux nombres et on effectue l’opération. Finalement, on affiche le résultat et le message de sortie.
- Si l’utilisateur choisit l’option `4`, on affiche le message `Merci d’avoir utilisé notre application` et on termine l’application.
- Si l’utilisateur saisit une valeur invalide, on affiche le message `Valeur invalide` et on quitte l’application.

### Solution

```python
print("MENU")
print('=' * 40)
print("1.Addition")
print("2.Soustraction")
print("3.Multiplication")
print("4.Quitter")
print('=' * 40)

option = int(input("Saisir une option de menu 1-4:"))

if option == 4:
    print("Merci d’avoir utilisé notre application")
elif 1 <= option <= 3:
    a = int(input("Saisir le premier nombre:"))
    b = int(input("Saisir le deuxième nombre:"))

    if option == 1:
        resultat = a + b
    elif option == 2:
        resultat = a - b
    else:
        resultat = a * b

    print("Resultat de l'opération:{}".format(resultat))
else:
    print("Option de menu non valide")
```

---

## Exercice 3.12

Développer le code qui permet de saisir la note de passage d’un conducteur à l’examen de conduite. On affectera à la variable `resultat` la chaîne `Réussi` si la note est supérieure ou égale à `60` et `Échec` si la note est inférieure à `60`. On utilisera l’opérateur conditionnel.

### Solution

On affecte le résultat du test fait à travers l’opérateur conditionnel à la variable `resultat`.

```python
note = int(input('Saisir la note:'))
resultat = 'Réussi' if note >= 60 else 'Échec'
print("Le résultat à l'examen est:{}".format(resultat))
```

---

# Chapitre 4 — Structures de boucle

## Connaissances requises

- Développer des structures de boucle `while`
- Développer des structures de boucle `for`
- Choisir entre les types de boucle selon le besoin

---

## Exercice 4.1

On se propose de réaliser un programme permettant à un usager de deviner un nombre entier compris entre `1` et `100`. Ce nombre secret sera généré aléatoirement.

On veillera à respecter les points suivants :

- On affichera un message à l’usager lui demandant de saisir un nombre.
- On indiquera à l’usager si son nombre est plus grand ou plus petit que le nombre secret.
- Si l’usager devine correctement le nombre secret, on lui affichera `Vous avez réussi à trouver le nombre` et on lui donne le nombre d’essais qu’il a fait.

### Solution

On commence par générer le nombre inconnu à deviner. Pour cela, on utilise la fonction `randint()` du module `random`.

On utilise ici une boucle `while` car on ne sait pas quand l’utilisateur va saisir la valeur exacte. Dans le corps de la boucle, on utilise un test à deux voies afin d’aider l’utilisateur à cibler la prochaine valeur à saisir.

```python
# Générer un nombre aléatoire
import random

inconnu = random.randint(1, 100)
print(inconnu)

# Trouver le nombre
essai = 1
nombre = int(input('Deviner le nombre:'))

while nombre != inconnu:
    if nombre > inconnu:
        print('votre nombre est plus grand!')
    else:
        print('votre nombre est plus petit!')

    essai += 1
    nombre = int(input('Deviner le nombre:'))

print('Vous avez réussi à trouver le nombre {} en {} fois'.format(inconnu, essai))
```

---

## Exercice 4.2

Demander à l’utilisateur un nombre entier. Développer un programme qui nous donne le total de nombres pairs, en commençant par `2`, qui doivent être utilisés pour que leur somme soit égale ou supérieure à ce nombre. Afficher ces nombres.

Exemple : si la somme considérée est `8`, on devra utiliser `2`, `4`, `6` donc `3` nombres. On ne peut pas utiliser `2` et `4` seulement car leur total est `6` et donc inférieur à `8`.

### Solution

On utilise ici une boucle `while` car on ne sait pas d’avance le total de nombres pairs à utiliser.

On ajoute donc `2` à chaque fois jusqu’à atteindre le nombre saisi.

```python
# Déterminer le total de nombres pairs pour obtenir un nombre donné
a = int(input('Saisir a:'))
sum = 0
i = 1

while sum < a:
    print(2 * i)
    sum += 2 * i
    i += 1

print('On a besoin des {} premiers nombres pairs'.format(i - 1))
```

---

## Exercice 4.3

Développer un programme qui permet de saisir un nombre indéterminé de nombres réels. La saisie devra s’arrêter lorsque l’utilisateur saisit le nombre `999`. On affichera ensuite la somme et la moyenne des nombres saisis. Modifier le code pour afficher aussi le total des nombres qui sont positifs ainsi que le nombre de fois où le nombre zéro a été saisi.

### Solution

On utilise ici une boucle `while` car on ne sait pas d’avance quand l’utilisateur va saisir `999`.

#### Solution 1

```python
###### Solution 1 ######
# Boucle sur 999
nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0

while nombre != 999:
    somme += nombre
    compteur += 1
    nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(somme, somme / compteur))
```

#### Solution 2 avec arrondi sur 2 décimales

```python
###### Solution 2 avec arrondi sur 2 décimales ######
# Boucle sur 999
nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0

while nombre != 999:
    somme += nombre
    compteur += 1
    nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(round(somme, 2), round(somme / compteur, 2)))
```

#### Solution 3 avec total de nombres positifs et nombre de répétition du chiffre zéro

```python
# Solution 3 avec total de nombres positifs et nombre de répétition du chiffre zéro

# Boucle sur 999
nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))
somme = 0
compteur = 0
somme_positifs = 0
nb_zeros = 0

while nombre != 999:
    somme += nombre
    compteur += 1

    if nombre == 0:
        nb_zeros += 1
    elif nombre > 0:
        somme_positifs += nombre

    nombre = float(input('1. Saisir une valeur. Saisir 999 pour arreter:'))

print('Somme est:{} et la moyenne est:{}'.format(round(somme, 2), round(somme / compteur, 2)))
print('Somme de nombres positifs:{}'.format(somme_positifs))
print('Nombre occurrences de zéro:{}'.format(nb_zeros))
```

---

## Exercice 4.4

Développer un programme qui demande à l’utilisateur `2` nombres, les stocke dans `2` variables préalablement définies puis affiche : la somme, le produit et la différence des `2` nombres.

Menu :

```text
Addition
Soustraction
Multiplication
Quitter
```

- Si l’utilisateur ne saisit pas une option du menu, on affiche de nouveau le menu.
- Si l’utilisateur choisit l’option `1`, `2` ou `3`, on demande la saisie des `2` nombres et on effectue l’opération. Finalement, on affiche le résultat.
- Si l’utilisateur choisit l’option `4`, on affiche le message `Merci d’avoir utilisé notre application` et on termine l’application.

### Solution

On utilise ici une boucle `while` car on ne sait pas d’avance le choix à faire par l’utilisateur. Dans ce cas, on intègre une variable sentinelle qui prend la valeur `False` si l’utilisateur choisit de quitter l’application.

```python
flag = True

while flag:
    print("MENU")
    print('=' * 40)
    print("1.Addition")
    print("2.Soustraction")
    print("3.Multiplication")
    print("4.Quitter")
    print('=' * 40)

    option = int(input("Saisir une option de menu 1-4:"))

    if option == 4:
        print("Merci d’avoir utilisé notre application")
        flag = False

    elif 1 <= option <= 3:
        a = int(input("Saisir le premier nombre:"))
        b = int(input("Saisir le deuxième nombre:"))

        if option == 1:
            resultat = a + b
        elif option == 2:
            resultat = a - b
        else:
            resultat = a * b

        print("Resultat de l'opération:{}".format(resultat))
    else:
        print("Option de menu non valide")
```

---

## Exercice 4.5

Soit l’itérable suivant :

```python
[10, 12, 14, 16, 18, 20]
```

En utilisant une boucle `for`, faire en sorte que la séquence de nombres affichée en sortie soit :

```text
13 15 17 19 21 23
```

Modifier votre code afin d’obtenir le même résultat mais en utilisant cette fois la fonction `range()` au lieu de la séquence.

### Solution

On a deux solutions intéressantes ici. Si l’on veut utiliser les listes Python, on peut directement itérer à travers la liste de valeurs et obtenir les valeurs en sortie modifiées.

Sinon, on peut utiliser la fonction `range()` en faisant attention à prendre un pas d’incrémentation de `2`.

```python
# Solution avec la séquence
for tmp in [10, 12, 14, 16, 18, 20]:
    print(tmp + 3)

# Solution avec la fonction range
for tmp in range(10, 22, 2):
    print(tmp + 3)
```

---

## Exercice 4.6

Développer un programme qui demande à l’utilisateur une phrase puis lui donne le nombre de caractères qui la composent.

Par exemple, si l’utilisateur entre :

```text
Je veux aller sur Andromède
```

Le programme devra afficher :

```text
Nombre de caractères : 27
```

On demandera à l’usager la phrase à manipuler.

Modifier le programme afin de donner le nombre de fois que la lettre `a` se retrouve dans la phrase.  
Modifier votre programme afin de prendre en compte les majuscules et minuscules.

### Solution

On utilise ici une boucle `for` car on sait d’avance le nombre total de lettres contenues dans la chaîne de caractères.

```python
phrase = input('Saisir une phrase:')
longueur = len(phrase)
print('Le nombre de caractères est:{}'.format(longueur))

# nombre de répétition de la lettre a
compteur = 0

for tmp in phrase:
    if tmp == 'a':
        compteur += 1

print('Le caractère {} se retrouve {} fois'.format('a', compteur))

# nombre de répétition de la lettre a ou A
compteur = 0

for tmp in phrase:
    if tmp in ['a', 'A']:
        compteur += 1

print('Le caractère {} ou {} se retrouve {} fois'.format('a', 'A', compteur))
```

---

## Exercice 4.7

Un étudiant à l’université paye `2500$` comme frais de scolarité pour la première année. Le registrariat lui a indiqué qu’en raison de l’inflation, celles-ci augmenteront de `3.5%` chaque année.

Développer le code qui lui permettra d’obtenir le montant total payé à la fin de ses études, sachant que celles-ci peuvent durer `4` ans.

### Solution

On utilise une boucle `for` pour calculer le montant total payé à la fin des études.

```python
frais_premiere_annee = 2500  # Frais de scolarité de la première année
TAUX_INFLATION = 0.035       # Taux d'inflation annuel
annees_etudes = 4            # Durée des études en années

montant_total = frais_premiere_annee  # Montant total initialisé avec les frais de la première année

for annee in range(2, annees_etudes + 1):
    # Ne pas oublier que l'indice de fin n'est pas pris en compte
    frais_annee = frais_premiere_annee * (1 + TAUX_INFLATION) ** (annee - 1)
    montant_total += frais_annee

print("Le montant total payé à la fin des études est de :{:.2f}".format(montant_total))
```

---

## Exercice 4.8

Développer le code qui demande à l’utilisateur de saisir un entier. Celui-ci sera stocké dans une variable appelée `repetition`.

On affichera en sortie la figure ci-dessous. Le cas montré est pour une valeur de `repetition` égale à `4`.

```text
repetition =1
#
repetition =2
****
repetition =3
********
repetition =4
************
```

### Solution

Tout d’abord, il faut comprendre la nature de la figure à dessiner. On constate alors que la variation se trouve au niveau du symbole `*` alors que le symbole `#` est utilisé juste comme caractère de séparation.

```python
repetition = int(input("Entrez un entier : "))

figure = "#"
for i in range(1, repetition + 1):
    print("repetition=" + str(i))
    figure += "*" + "*" * (i - 1) + "#"
    print(figure)
```

---

## Exercice 4.9

Développer un programme qui permet de générer une suite arbitraire de nombres aléatoires entiers dont la valeur est entre `0` et `100`. Au début, on demandera à l’utilisateur le nombre de valeurs souhaitées et on lui affichera en sortie les statistiques suivantes :

- Le nombre de valeurs impaires générées
- Les valeurs minimum et maximum générées
- L’étendue qui est définie par la différence entre la valeur maximum et minimum

### Solution

On utilise ici une boucle `for` pour générer les nombres aléatoires.

Les variables `nombre_impairs`, `minimum` et `maximum` sont mises à jour à chaque itération.

L’étendue est calculée en soustrayant la valeur minimum de la valeur maximum.

```python
import random

# Demander à l'utilisateur le nombre de valeurs
n = int(input("Saisir le nombre de valeurs: "))

# Initialiser les variables pour les statistiques
nombre_impairs = 0
minimum = 100
maximum = 0

# Générer les nombres aléatoires et mettre à jour les statistiques
for tmp in range(n):
    valeur = random.randint(0, 100)

    if valeur % 2 != 0:
        nombre_impairs += 1

    if valeur < minimum:
        minimum = valeur

    if valeur > maximum:
        maximum = valeur

# Calculer l'étendue
etendue = maximum - minimum

# Afficher les statistiques
print("Nombre de valeurs impaires:".format(nombre_impairs))
print("Valeur minimum:".format(minimum))
print("Valeur maximum:".format(maximum))
print("Étendue:".format(etendue))
```

---

## Note finale

Cette transcription couvre les pages photographiées : table des matières, chapitre 2, chapitre 3 et début du chapitre 4 jusqu’à l’exercice 4.9.
