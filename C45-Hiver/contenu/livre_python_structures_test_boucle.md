# Transcription structurée — Structures de test et structures de boucle

> Fichier Markdown créé à partir des photos fournies. Certaines pages étaient tournées ou partiellement visibles; le contenu ci-dessous reprend les éléments lisibles et les organise par chapitre, sections, exemples et exercices.

---

## Table des matières visible

### 3. Structures de test

- **3.1 Introduction** — p. 51
- **3.2 Structure simple `if`** — p. 52
  - 3.2.1 Logique de la structure `if` simple ou à une voie — p. 53
- **3.3 Structure `if-else`** — p. 54
  - 3.3.1 Logique de la structure `if-else` — p. 55
- **3.4 Structure complexe `if-elif-else`** — p. 56
- **3.5 Opérateur conditionnel** — p. 57
- **3.6 Résumé rapide** — p. 58
- **3.7 Quiz** — p. 59
- **3.8 Exercices de pratique** — p. 62
- **3.9 Exercices de programmation** — p. 64

### 4. Structures de boucle

- **4.1 Introduction** — p. 67
- **4.2 Structure `while`** — p. 68
  - 4.2.1 Logique de la boucle `while` — p. 69
- **4.3 Boucle `for`** — p. 70
  - 4.3.1 Fonction `range()` — p. 71
- **4.4 Transfert de contrôle** — p. 73
- **4.5 Résumé rapide** — p. 74
- **4.6 Quiz** — p. 75
- **4.7 Exercices de pratique** — p. 78
- **4.8 Exercices de programmation** — p. 81

---

# Chapitre 3 — Structures de test

## Dans ce chapitre, vous allez :

- Apprendre à utiliser une expression conditionnelle.
- Apprendre à intégrer des opérateurs relationnels et logiques dans les expressions conditionnelles.
- Développer des structures de test `if`, `if-else` et `if-elif`.
- Utiliser l’opérateur ternaire de test conditionnel.

---

## 3.1 Introduction

Un grand nombre de langages dont Python permettent deux types d’exécution. Le premier type permet une exécution **séquentielle simple**. Celle-ci fait en sorte que le programme s’exécute du début jusqu’à la fin de manière linéaire, une instruction à la fois.

Si, par exemple, on avait la première instruction à la ligne 1 et la dernière ligne à la ligne 100, l’exécution se ferait de l’instruction 1 à l’instruction 100.

Le deuxième type est basé sur le concept d’**exécution par sélection**. Celui-ci introduit la possibilité d’un choix d’exécution qui n’est pas nécessairement linéaire de la première instruction jusqu’à la dernière. Dans ce cas, on pourrait introduire des expressions qui conditionnent le passage par une série d’instructions au lieu d’une autre série.

En reprenant l’exemple des instructions de 1 à 100, l’exécution pourrait, selon certaines conditions préétablies, ne pas se faire de 1 à 100 de manière strictement linéaire.

Les structures de test en Python présentées sont :

- `if`
- `if-else`
- `if-elif-else`
- opérateur ternaire de test conditionnel

> **Note :** La structure `switch` que l’on retrouve dans d’autres langages n’est pas disponible de la même manière dans Python.

---

## 3.2 Structure simple `if` — une voie ou *one-way*

Une structure `if` à une voie est utilisée lorsqu’on veut tester une condition, que ce soit une variable ou une expression conditionnelle. Lorsque le résultat du test se réduit à `True`, un traitement est effectué.

### Forme générale

```python
if condition:
    bloc à exécuter quand la condition est True
```

Dans Python, le mot réservé pour commencer une structure de test simple est `if`. La condition est une expression booléenne qui permet de déterminer si le bloc sera exécuté ou non.

- Si la condition est `True`, le bloc d’instructions qui suit est exécuté.
- Si la condition est `False`, le bloc d’instructions qui suit n’est pas exécuté.

On utilise le marqueur `:` pour signaler le début du bloc d’instructions. Le bloc peut contenir une ou plusieurs instructions. Ces instructions doivent être indentées du même nombre d’espaces à partir de la gauche.

Le nombre d’espaces utilisé pour indiquer un bloc est généralement de 4. Il est important de ne pas mélanger les tabulations et les espaces dans le même code.

### Logique de la structure `if` simple

Au niveau du `if` à une voie, l’expression conditionnelle est évaluée pour être comparée à `True` ou `False`.

- Si l’expression s’évalue à `True`, la série d’instructions est exécutée.
- Si l’expression s’évalue à `False`, la série d’instructions n’est pas exécutée.

### Listing 3.1 — Utilisation de la structure `if` à une voie

```python
MAX = 20
total = int(input('S.V.P, saisir le total:'))
if total > MAX:
    print('Vous avez dépassé le maximum!!')
```

---

## 3.3 Structure `if-else` — deux voies ou *two-way*

Dans certains cas, `if` est suffisant pour couvrir les cas des instructions. Par contre, il est possible de vouloir exécuter deux chemins mutuellement exclusifs selon la valeur d’une condition.

### Forme générale

```python
if condition:
    instructions 1 pour condition True
else:
    instructions 2 pour condition False
```

Ainsi, un seul bloc d’instructions est exécuté, mais pas les deux. Les mots réservés sont `if` et `else`.

La condition est une expression booléenne utilisée pour déterminer lequel des deux blocs sera exécuté.

- Si la condition est `True`, le bloc d’instructions qui suit `if` est exécuté.
- Si la condition est `False`, le bloc d’instructions qui suit `else` est exécuté.

Le mot-clé `else` commence la deuxième partie du `if`. On utilise encore le symbole `:` pour démarrer le bloc. Les instructions du bloc doivent être indentées au même niveau.

Un commentaire n’est pas considéré comme une instruction. Si l’on n’a pas encore défini le code, on peut utiliser le mot-clé `pass` pour que le bloc soit valide.

### Logique de la structure `if-else`

La condition est évaluée pour être comparée à `True` ou `False`. Dans les deux cas, la valeur obtenue se réduit à `True` ou `False`.

### Listing 3.2 — Utilisation de la structure `if` à deux voies

```python
MAX = 20
total = int(input('S.V.P, saisir le total:'))
if total > MAX:
    print('Vous avez dépassé le maximum!!')
else:
    print('Total:', total)
    print('Vous n\'avez pas dépassé le maximum')
```

### Sortie lorsque le total dépasse le maximum

```text
S.V.P, saisir le total:25
Vous avez dépassé le maximum!!
```

### Sortie lorsque le total ne dépasse pas le maximum

```text
S.V.P, saisir le total:14
Total: 14
Vous n'avez pas dépassé le maximum
```

---

## 3.4 Structure complexe `if-elif-else` — plusieurs voies ou *multi-way*

Lorsqu’on a plusieurs chemins mutuellement exclusifs et qu’on veut exécuter les opérations selon une catégorie, on utilise la structure complexe `if-elif-else`.

### Forme générale

```python
if condition:
    instruction 1
elif condition:
    instruction 3
else:
    instruction 2
```

Cette structure est adaptée lorsqu’on veut sélectionner des instructions à exécuter à partir d’un certain nombre d’options. Le mot-clé `if` est obligatoire, tandis que `else` est optionnel. On peut inclure autant de `elif` que nécessaire.

---

## 3.5 Opérateur conditionnel

Python dispose d’un opérateur conditionnel ternaire qui utilise une condition booléenne pour choisir laquelle de deux expressions sera évaluée et possiblement affectée à une variable.

### Forme classique `if-else`

```python
if condition:
    val = expr1
else:
    val = expr2
```

### Forme ternaire

```python
val = expr1 if condition else expr2
```

Si la condition est `True`, `expr1` est évaluée. Si la condition est `False`, `expr2` est évaluée. La valeur retournée est affectée à la variable `val`.

### Exemple

```python
ma_var = num1 if num1 > num2 else num2
```

Si `num1` est plus grand que `num2`, alors `num1` est affecté à `ma_var`; sinon, `num2` est affecté à `ma_var`.

> **Bonne pratique :** Bien qu’il soit utile pour remplacer une opération d’affectation, l’opérateur conditionnel ternaire devrait être utilisé avec précaution.

---

## 3.6 Résumé rapide

- Les structures de test sont basées sur le concept d’exécution par sélection.
- On peut intégrer des opérateurs relationnels et logiques dans les expressions conditionnelles.
- On peut utiliser des structures de test `if`, `if-else` et `if-elif`.
- L’opérateur ternaire peut remplacer une structure `if-else` simple dans certains cas.

---

## 3.7 Quiz — éléments visibles

### Question 1

Les structures de test en Python qu’on peut utiliser sont :

- `if`
- `if-elif`
- `switch`

### Question 2

Une structure de test `if` à une voie peut-elle contenir une structure `else` ?

- Vrai
- Faux

### Question 3

Une structure de test `if` à deux voies contient-elle une structure `else` ?

- Vrai
- Faux

### Question 4

Les deux structures suivantes donnent-elles le même résultat ?

```python
valeur = int(input('Saisir une valeur:'))
if valeur < 20:
    print('La valeur est inférieure à 20')
elif valeur < 30:
    print('La valeur est supérieure ou égale à 20 et inférieure à 30')
else:
    print('La valeur est supérieure ou égale à 30')
```

et

```python
valeur = int(input('Saisir une valeur:'))
if valeur < 20:
    print('La valeur est inférieure à 20')
if valeur < 30:
    print('La valeur est inférieure à 30')
else:
    print('La valeur est supérieure ou égale à 30')
```

### Question 5

Exécution du code suivant :

```python
age = 10
if age > 20:
    print('Vous êtes un adulte')
print('Merci')
```

Choix visibles :

- Vous êtes un adulte
- Vous êtes un adulte / Merci
- Merci

### Question 6

Pour représenter une opération logique `OR`, on utilise :

- `OR`
- `or`
- `||`

### Question 7

Si on veut que le message « Vous avez dix ans » s’affiche, on doit remplacer `?` par :

```python
age = 10
if age ? 10:
    print('Vous avez dix ans')
```

Choix visibles :

- `=`
- `==`
- `equals`

### Question 8

Code visible :

```python
age = 10
message = 'adulte' if age > 18 else 'enfant'
print(message)
```

Le résultat affiché est :

- adulte
- enfant
- erreur

### Question 9

On considère l’opérateur logique `and`. Les affirmations possibles :

- Le résultat est `True` si les deux opérandes sont `True`.
- Le résultat est `True` si l’un des deux opérandes est `True`.
- Le résultat est `False` si l’un des deux opérandes est `False`.

---

## 3.8 Exercices de pratique

### Exercice 3.1

Demander à l’utilisateur un nombre entier. Celui-ci sera stocké dans la variable `val_a`. Afficher si le nombre est pair.

```python
# trouver si nombre est pair
val_a = int(input('Saisir un nombre entier:'))
if val_a % 2 == 0:
    print('{} est pair'.format(val_a))
```

Sortie :

```text
Saisir un nombre entier:12
val_a: 12 est pair
```

Note : le code permet seulement de dire si la valeur saisie est paire. Par contre, il n’indique pas si la valeur est impaire.

### Exercice 3.2

Reprendre l’exercice 3.1. Développer le code qui permet d’afficher si le nombre est pair ou impair.

```python
# trouver si nombre est pair
val_a = int(input('Saisir un nombre entier:'))
if val_a % 2 == 0:
    print('val_a: {} est pair'.format(val_a))
else:
    print('val_a: {} est impair'.format(val_a))
```

Sortie :

```text
Saisir un nombre entier:12
val_a: 12 est pair
```

Sinon, dans le cas d’un nombre impair :

```text
Saisir un nombre entier:51
val_a: 51 est impair
```

### Exercice 3.3

Demander à l’utilisateur un nombre entier. Celui-ci sera stocké dans la variable `val_a`.

Afficher si le nombre est inférieur ou égal à 20, supérieur à 20 mais inférieur ou égal à 50, sinon s’il est supérieur à 50.

```python
# trouver si nombre est dans un intervalle donné
val_a = int(input('Saisir un nombre entier:'))
if val_a <= 20:
    print('inférieur ou égal à 20')
elif val_a <= 50:
    print('inférieur ou égal à 50')
else:
    print('supérieur à 50')
```

Sortie :

```text
Saisir un nombre entier:75
supérieur à 50
```

Note : la sortie montrée est pour une valeur supérieure à 50. Le code peut être amélioré de plusieurs façons, mais l’essentiel est de voir la structure de test utilisée.

---

# Chapitre 4 — Structures de boucle

## Dans ce chapitre, vous allez :

- Développer des structures de boucle `while`.
- Développer des structures de boucle `for`.
- Apprendre à choisir entre les types de boucle selon le besoin.

---

## 4.1 Introduction

Le mode séquentiel et le mode d’exécution par sélection ne permettent pas toujours de résoudre les problèmes dans lesquels il faut répéter une série d’instructions.

Une structure répétitive, plus communément appelée **boucle**, est une série d’actions qui se répète dans un ordre précis, un nombre déterminé de fois selon une condition.

On a besoin de définir :

- la suite d’instructions à effectuer;
- le nombre de répétitions ou la condition d’arrêt.

En Python, on retrouve principalement :

- la boucle `while`;
- la boucle `for`.

---

## 4.2 Structure `while`

La boucle `while` permet la répétition de l’exécution d’une série d’instructions tant qu’une condition est vraie.

### Syntaxe

```python
while <condition>:
    bloc d'instructions
```

Si la condition est `True`, le bloc d’instructions est exécuté. La condition est ensuite évaluée de nouveau. Si elle est toujours `True`, le bloc est exécuté une autre fois, jusqu’à ce que la condition devienne `False`.

### Logique de la boucle `while`

La boucle `while` est basée sur la structure algorithmique :

```text
Tant que ... faire
    bloc d'instructions
Fin tant que
```

Le losange représente la condition. Lorsque la condition est vraie, la série d’instructions est exécutée, puis on revient à l’évaluation de la condition.

### Listing 4.1 — Boucle de comptage simple

```python
compteur = 1
while compteur <= 5:
    print(compteur)
    compteur += 1
```

Sortie :

```text
1
2
3
4
5
```

Il faut noter qu’avant d’entrer dans la boucle, la variable `compteur` doit être initialisée. Elle est ensuite incrémentée dans la boucle. Sinon, on risque une boucle infinie.

---

## 4.3 Boucle `for`

La boucle `for` permet de répéter l’exécution d’une série d’instructions un nombre spécifique de fois.

### Syntaxe

```python
for tmp in [valeur1, valeur2, ..., valeurN]:
    instructions
```

La boucle va itérer à travers une séquence d’éléments. À chaque passage, un élément de la séquence est affecté à la variable `tmp`.

### Listing 4.2 — Boucle `for` utilisant un itérable

```python
for tmp in [0, 1, 2, 3, 4, 5]:
    print(tmp)
```

Sortie :

```text
0
1
2
3
4
5
```

Dans l’exemple précédent, on a utilisé une séquence de 6 nombres consécutifs en commençant par 0 et en terminant par 5. Il n’est pas important que les nombres soient consécutifs; on peut avoir n’importe quelle séquence.

### Listing 4.3 — Sortie du programme

```text
0
1
2
3
4
5
```

### Listing 4.4 — Séquence d’itération quelconque

```python
for tmp in ['toto', 'dodo']:
    print(tmp)
```

Sortie :

```text
toto
dodo
```

---

## 4.3.1 Fonction `range()`

Dans le cas où l’on désire développer une boucle `for` avec un itérable contenant des valeurs numériques, on peut utiliser la fonction `range()`.

La forme générale est :

```python
range(debut, fin, pas)
```

Elle permet de générer un itérable contenant une séquence de valeurs. La valeur de départ est incluse, mais la valeur de fin n’est pas incluse.

### Listing 4.5 — Utilisation de la fonction `range`

```python
for tmp in range(1, 6, 2):
    print(tmp)
```

Sortie :

```text
1
3
5
```

Si le pas est égal à 1, on peut l’omettre :

### Listing 4.6 — Fonction `range` avec pas de 1

```python
for tmp in range(1, 6):
    print(tmp)
```

---

## 4.4 Transfert de contrôle

Python offre la possibilité d’introduire un transfert conditionnel du flux d’exécution du programme en utilisant `break` ou `continue`.

### Syntaxe du `break`

L’instruction `break` peut être utilisée à l’intérieur d’une boucle pour sortir immédiatement de la boucle. Lorsqu’elle est exécutée, la séquence d’exécution est transférée à la suite du programme.

### Listing 4.9 — Utilisation de `break`

```python
for count in range(1, 6):
    if count == 4:
        break
    print(count)
print('Sortie après break')
```

Sortie :

```text
1
2
3
Sortie après break
```

### Syntaxe du `continue`

L’instruction `continue` peut être utilisée dans une boucle pour éviter l’exécution d’une série d’instructions qui suivent immédiatement l’instruction `continue`. Lorsque l’instruction est exécutée, on retourne à l’évaluation de la condition ou à l’itération suivante.

### Listing 4.10 — Utilisation de `continue`

```python
for count in range(1, 6):
    if count == 4:
        continue
    print(count)
```

Sortie :

```text
1
2
3
5
```

---

## 4.5 Résumé rapide

- Une structure répétitive est une série d’actions qui se répète dans un ordre précis, un nombre déterminé de fois selon une condition.
- Une structure de boucle `while` utilise une condition qui s’évalue soit à `True`, soit à `False`.
- Une structure de boucle `for` utilise un compteur afin de se répéter un nombre spécifique de fois.

---

## 4.6 Quiz — éléments visibles

### Question 1

Les structures de boucle en Python sont :

- `while`
- `do-while`
- `for`

### Question 2

Une boucle `for` peut-elle être transformée en boucle `while` ?

- Vrai
- Faux

### Question 3

Dans une boucle, peut-on utiliser les mots-clés `continue` et `break` ?

- Vrai
- Faux

### Question 4

La boucle `for` suivante :

```python
for compteur in range(0, 5):
    print(compteur)
```

peut être transformée en boucle `while` suivante :

```python
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1
```

### Question 5

Code visible :

```python
compteur = 0
while compteur < 5:
    compteur += 1
    if compteur == 3:
        continue
    print(compteur)
```

### Question 6

Afin de produire la sortie suivante : `10 20 30`, quelle condition faut-il utiliser ?

```python
compteur = 10
while ?:
    print(compteur)
    compteur += 10
```

Choix visibles :

- `compteur < 30`
- `compteur < 40`
- `compteur < 20`

### Question 7

Code visible :

```python
compteur = 0
while compteur < 0:
    print(compteur)
    compteur += 10
print(compteur)
```

Sortie possible :

- `1`
- `0`
- Erreur

### Question 8

Boucles imbriquées :

```python
i = 0
while i < 5:
    j = 0
    while j < 4:
        print('i:{}, j:{}'.format(i, j))
        j += 1
    i += 1
```

Le nombre de lignes affichées sera :

- 19
- 5
- 25

### Question 9

Autre exemple de boucles imbriquées :

```python
i = 0
while i < 5:
    j = 0
    while j < i:
        print('i:{}, j:{}'.format(i, j))
        j += 1
    i += 1
```

Le nombre de lignes affichées sera :

- 9
- 10
- 11
- 25

### Question 10

Dans une boucle `while`, pour arrêter l’exécution des instructions et revenir à l’évaluation de la condition, on utilise :

- `break`
- `continue`
- `goto`
- `return`

---

## 4.7 Exercices de pratique

### Exercice 4.1

En utilisant une boucle `while`, développer le code qui affiche les nombres de 1 à 7.

```python
compteur = 1
while compteur <= 7:
    print(compteur)
    compteur += 1
```

Sortie :

```text
1
2
3
4
5
6
7
```

### Exercice 4.2

En utilisant une boucle `for` et la fonction `range()`, développer le code qui affiche les nombres de 1 à 7.

```python
for compteur in range(1, 8):
    print(compteur)
```

Sortie :

```text
1
2
3
4
5
6
7
```

### Exercice 4.3

Demander à l’utilisateur de saisir une chaîne de caractères. Afficher ensuite tous les caractères qui sont dans cette chaîne.

```python
# boucle avec itérateur de chaîne
phrase = input('Saisir une chaîne de caractères:')
for index in phrase:
    print(index)
```

Sortie :

```text
Saisir une chaine de caractères:Renard
R
e
n
a
r
d
```

### Exercice 4.4

Demander à l’utilisateur de saisir le caractère `O` pour continuer l’exécution. Tout autre caractère saisi arrête le programme.

```python
reponse = 'O'
while reponse == 'O':
    reponse = input('Voulez-vous continuer? O pour continuer:')

print('Merci d\'avoir utilisé notre logiciel')
```

Sortie :

```text
Voulez-vous continuer? O pour continuer:O
Voulez-vous continuer? O pour continuer:N
Merci d'avoir utilisé notre logiciel
```

Note : le code ne donne pas le résultat demandé si la saisie se fait en minuscule.

### Exercice 4.5

Demander à l’utilisateur de saisir le caractère `O` pour continuer l’exécution. Tout autre caractère saisi arrête le programme. On prend en compte les caractères en majuscule ou en minuscule.

### Exercice 4.6

Solution fournie en annexe.

On veut réaliser un programme permettant à un usager de deviner un nombre entier compris entre 1 et 100. Ce nombre secret sera généré aléatoirement.

À respecter :

- Afficher un message demandant de saisir un nombre.
- Indiquer si le nombre est plus grand ou plus petit que le nombre secret.
- Si l’usager devine correctement le nombre secret, afficher `Bravo` et donner le nombre d’essais.

### Exercice 4.7

Soit l’itérable suivant :

```python
[10, 12, 14, 16, 18, 20]
```

En utilisant une boucle `for`, faire en sorte que la séquence de nombres affichée en sortie soit :

```text
13 15 17 19 21 23
```

Modifier le code pour obtenir le même résultat en utilisant la fonction `range()` au lieu de la séquence.

### Exercice 4.8

Solution fournie en annexe.

Demander à l’utilisateur un nombre entier. Développer un programme qui donne le total de nombres pairs, en commençant par 2, qui doivent être utilisés pour que leur somme soit égale ou supérieure à ce nombre. Afficher ces nombres.

Exemple : si la somme considérée est 8, on devra utiliser 2, 4, 6 donc 3 nombres. On ne peut pas utiliser 2 et 4 seulement, car leur total est 6, inférieur à 8.

### Exercice 4.9

Développer un programme qui permet de saisir un nombre non déterminé de nombres entiers. La saisie s’arrête lorsque l’utilisateur saisit `999`. On affiche ensuite la somme et la moyenne des nombres saisis.

Modifier le code pour afficher aussi le total des nombres positifs ainsi que le nombre de fois où le nombre zéro a été saisi.

---

## 4.8 Exercices de programmation

### Exercice 4.10

Développer un programme qui demande à l’utilisateur 2 nombres, les stocke dans 2 variables préalablement définies puis affiche :

- la somme;
- le produit;
- la différence des 2 nombres.

Menu :

- Addition
- Soustraction
- Multiplication
- Quitter

Consignes visibles :

- Si l’utilisateur ne saisit pas une option du menu, on affiche de nouveau le menu.
- Si l’utilisateur choisit l’option 1, 2 ou 3, on demande la saisie des deux nombres et on effectue l’opération.
- Si l’utilisateur choisit l’option 4, on affiche le message « Merci d’avoir utilisé notre application » et on termine l’application.

### Exercice 4.11

Développer un programme qui demande à l’utilisateur une phrase puis lui donne le nombre de caractères qui la composent.

Exemple : si l’utilisateur saisit :

```text
Je veux aller sur Andromède
```

le programme affiche :

```text
Nombre de caractères : 27
```

Modifier le programme afin de donner le nombre de fois que la lettre `a` se retrouve dans la phrase. Ensuite, modifier encore pour prendre en compte les majuscules et minuscules, donc `a` ou `A`.

### Exercice 4.12

Développer un programme qui informe des activités possibles selon la météo.

On demande la température à l’usager puis on propose l’activité la plus adéquate selon la règle d’affaire :

- Si la température est supérieure ou égale à 25°C, proposer la natation.
- Si la température est supérieure ou égale à 18°C et inférieure à 25°C, proposer le tennis.
- Si la température est inférieure à 18°C mais supérieure ou égale à 2°C, proposer une randonnée dans les bois.
- Si la température est inférieure à 2°C, proposer le ski.

### Exercice 4.13

Un étudiant à l’université paie 2500$ comme frais de scolarité pour la première année. Le registrariat lui a indiqué qu’en raison de l’inflation, ceux-ci augmenteront de 3,5% chaque année.

Développer le code qui permettra d’obtenir le montant total payé à la fin de ses études, sachant qu’elles peuvent durer 4 ans.

### Exercice 4.14

Développer un programme qui donne les coupures de billets à rendre aux clients lors de leurs achats.

Les caissiers ou caissières saisissent le total à payer et le montant remis par le client. Le système doit afficher ce qu’il faut rendre aux clients.

Hypothèses :

- Le montant total est toujours un entier.
- Les billets disponibles sont 1$, 5$, 10$ et 20$ seulement.

### Exercice 4.15

Développer le code qui demande à l’utilisateur de saisir un entier. Celui-ci sera stocké dans une variable appelée `repetition`.

Le programme affiche une figure selon la valeur saisie. Exemple pour `repetition = 4` :

```text
repetition = 1
#
repetition = 2
****
repetition = 3
*********
repetition = 4
****************
```

### Exercice 4.16

Développer un programme qui permet de générer un nombre arbitraire de nombres aléatoires entiers dont la valeur est entre 0 et 100. On demandera à l’utilisateur de fournir le nombre de valeurs souhaitées et on affichera :

- le nombre de valeurs impaires générées;
- les valeurs minimum et maximum générées;
- l’étendue, définie par la différence entre la valeur maximum et minimum.

---

## Notes de qualité de transcription

- Certaines images étaient inversées; le texte a été réorganisé dans le bon ordre logique.
- Certaines zones de pages étaient partiellement floues ou coupées; les passages non lisibles ont été reformulés prudemment.
- Les blocs de code ont été normalisés en Markdown avec indentation Python.

