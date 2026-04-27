# Manuel de Révision Théorique — Programmation Python
## Spécialiste en intégration de données | Niveau universitaire

---

## Introduction

Ce manuel couvre en profondeur les concepts fondamentaux du cours. L'objectif n'est pas de mémoriser de la syntaxe, mais de **comprendre les mécanismes** qui gouvernent l'exécution d'un programme Python. Un spécialiste de données qui comprend pourquoi le code fonctionne d'une certaine façon sera toujours plus efficace que celui qui applique des recettes sans réfléchir.

Chaque section suit la structure : **Définition formelle → Fonctionnement interne → Règles critiques → Exemples annotés → Erreurs fréquentes → Points d'examen**.

---

## Chapitre I — Le Typage en Python : Fondements et Implications

### 1.1 Qu'est-ce qu'un type de donnée ?

Un **type de donnée** est un contrat qui définit simultanément :
1. La **représentation en mémoire** (combien d'octets, quel encodage)
2. Les **opérations légales** (qu'est-ce qu'on peut faire avec cette valeur)
3. L'**ensemble des valeurs possibles** (domaine)

En Python, contrairement au C ou Java, les **variables ne sont pas typées** : ce sont les **valeurs** qui le sont. Une variable est simplement une étiquette (un nom) qui pointe vers un objet en mémoire. Cet objet possède un type immuable.

```python
x = 10        # x pointe vers l'objet entier 10
x = "hello"   # x pointe maintenant vers l'objet chaîne "hello"
              # l'entier 10 existe toujours en mémoire, x ne pointe plus vers lui
```

Ce comportement s'appelle le **typage dynamique** : le type est déterminé à l'exécution, pas à la compilation.

### 1.2 Les types fondamentaux du cours

#### Le type `int` (Entier)

En Python, les entiers ont une **précision arbitraire** : il n'y a pas de limite supérieure due à la taille d'un registre processeur (contrairement à Java où `int` est limité à 2 147 483 647). Python alloue automatiquement la mémoire nécessaire.

```python
# Tous ces entiers sont valides
a = 42
b = -1_000_000    # Le _ est un séparateur visuel (Python 3.6+)
c = 10 ** 100     # Un googol — aucun problème en Python
```

**Usage en traitement de données :** Les entiers servent d'index de lignes, de compteurs, d'identifiants (clés primaires), de quantités entières. Ne jamais utiliser un `float` pour représenter un ID ou un compteur.

#### Le type `float` (Réel)

Les flottants suivent la norme **IEEE 754 double précision** (64 bits). Cela implique une précision de ~15-17 chiffres significatifs, mais aussi des **erreurs d'arrondi inévitables** pour certains nombres décimaux.

```python
print(0.1 + 0.2)       # Affiche 0.30000000000000004, pas 0.3
print(0.1 + 0.2 == 0.3) # Affiche False !
```

**Pourquoi ?** Les nombres décimaux comme `0.1` ne peuvent pas être représentés exactement en binaire (comme `1/3` ne peut pas être représenté exactement en décimal). Ils sont stockés avec une légère approximation.

**Implication pratique :** Ne jamais tester l'égalité exacte de deux flottants calculés. Utiliser : `abs(a - b) < 0.0001` à la place de `a == b`.

#### Le type `str` (Chaîne de caractères)

Une chaîne est une **séquence immuable** de caractères Unicode. Immuable signifie qu'une fois créée, elle ne peut pas être modifiée en place — toute opération qui semble modifier une chaîne crée en réalité une **nouvelle chaîne**.

```python
s = "data"
s[0] = "D"      # ERREUR : TypeError — les chaînes sont immuables
s = "D" + s[1:] # CORRECT : crée une nouvelle chaîne "Data"
```

Les **indices** permettent d'accéder aux caractères :
- `s[0]` → premier caractère
- `s[-1]` → dernier caractère (équivaut à `s[len(s)-1]`)
- `s[-2]` → avant-dernier caractère

#### Le type `bool` (Booléen)

`bool` est un **sous-type de `int`** en Python. `True` vaut `1` et `False` vaut `0`.

```python
print(True + True)    # 2
print(True * 5)       # 5
print(False + 10)     # 10
```

Ce comportement est parfois utile pour compter des conditions vraies sans `if`.

**Falsy values (valeurs qui s'évaluent à `False`) :**
- `0`, `0.0` (zéros de tout type numérique)
- `""` (chaîne vide)
- `None`

**Tout le reste s'évalue à `True`**, ce qui permet d'écrire `if chaine:` à la place de `if chaine != "":`.

### 1.3 Conversion de types (Casting)

La conversion explicite est fondamentale en Python car `input()` retourne **toujours** une chaîne, même si l'utilisateur saisit un nombre.

```python
# Chaîne → Entier
int("42")       # 42    ✓
int("-10")      # -10   ✓
int("3.14")     # ERREUR : ValueError — int() ne comprend pas les décimales
int("abc")      # ERREUR : ValueError — pas un nombre

# Solution pour convertir "3.14" en entier :
int(float("3.14"))    # 3 (troncature, pas arrondi !)

# Entier → Réel
float(10)       # 10.0
float("3.14")   # 3.14

# Réel → Entier (attention : troncature vers zéro, pas arrondi)
int(3.9)        # 3  (pas 4 !)
int(-3.9)       # -3 (pas -4 !)
round(3.9)      # 4  (arrondi)
```

### 1.4 `type()` vs `isinstance()` — Lequel utiliser ?

`type(x) == int` est une **vérification stricte** : elle retourne `False` si `x` est un booléen (même si `bool` est un sous-type de `int`).

`isinstance(x, int)` est **flexible et recommandée** : elle respecte la hiérarchie des types et retourne `True` si `x` est un `int` ou un sous-type de `int` (comme `bool`).

```python
x = True
type(x) == int          # False (True est un bool, pas exactement un int)
isinstance(x, int)      # True  (bool est un sous-type de int)
isinstance(x, (int, float))  # True — peut tester plusieurs types à la fois
```

**Règle d'examen :** Utiliser `isinstance()` dans le code de production. `type()` est utile uniquement pour du débogage ou quand la correspondance exacte est requise.

---

## Chapitre II — Opérateurs et Précédence

### 2.1 Les opérateurs arithmétiques en détail

Les opérateurs arithmétiques de Python se comportent parfois différemment des attentes mathématiques.

#### Division réelle (`/`) vs Division entière (`//`)

```python
# Division réelle — retourne TOUJOURS un float
7 / 2    # 3.5
6 / 2    # 3.0  (pas 3 !)
-7 / 2   # -3.5

# Division entière — retourne TOUJOURS un int (ou float si opérande est float)
7 // 2    # 3   (arrondi vers le bas, vers -∞)
-7 // 2   # -4  (PAS -3 ! arrondi vers -∞, pas vers zéro)
7.0 // 2  # 3.0 (float // retourne un float)
```

**Point critique :** `//` arrondit **vers le bas** (vers moins l'infini), pas vers zéro. `-7 // 2 = -4` et non `-3`.

#### Modulo (`%`) — Applications pratiques

Le modulo donne le **reste** de la division euclidienne. La relation invariante est :
```
a = (a // b) * b + (a % b)
```

Applications fréquentes à l'examen :
```python
n % 2 == 0          # n est pair
n % 2 != 0          # n est impair
n % k == 0          # n est divisible par k (k divise n)

# Décomposer un nombre en heures/minutes/secondes
duree = 3725  # secondes
h = duree // 3600           # 1 heure
m = (duree % 3600) // 60    # 2 minutes
s = duree % 60              # 5 secondes

# Décomposer les chiffres d'un entier
n = 1234
milliers = n // 1000        # 1
centaines = (n % 1000) // 100  # 2
dizaines = (n % 100) // 10    # 3
unites = n % 10               # 4

# Rendu de monnaie
monnaie = 87
billets_50 = monnaie // 50   # 1
reste = monnaie % 50         # 37
billets_20 = reste // 20     # 1
reste = reste % 20           # 17
billets_10 = reste // 10     # 1
...
```

#### Puissance (`**`)

`**` a une **associativité à droite** : `2 ** 3 ** 2` est interprété comme `2 ** (3 ** 2) = 2 ** 9 = 512`, pas comme `(2 ** 3) ** 2 = 64`.

```python
# Racine carrée (sans module math)
racine = nombre ** 0.5       # √nombre
racine_cubique = nombre ** (1/3)

# Application : distance euclidienne entre deux points
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
```

### 2.2 La précédence des opérateurs — Mémorisation

**Mnémotechnique** : **PEMDAS** (Parenthèses, Exposants, Multiplication/Division, Addition/Soustraction) + opérateurs logiques en dernier.

```
Niveau 1 (le plus fort) : ( )
Niveau 2               : **                          (droite → gauche)
Niveau 3               : *, /, //, %                 (gauche → droite)
Niveau 4               : +, -                        (gauche → droite)
Niveau 5               : ==, !=, <, >, <=, >=        (comparaisons)
Niveau 6               : not
Niveau 7               : and
Niveau 8 (le plus faible): or
```

**Exemple d'analyse :**
```python
# Expression : 2 + 3 * 4 ** 2 - 1
# Étape 1 : ** → 4 ** 2 = 16
# Étape 2 : *  → 3 * 16 = 48
# Étape 3 : +  → 2 + 48 = 50
# Étape 4 : -  → 50 - 1 = 49
résultat = 2 + 3 * 4 ** 2 - 1  # 49
```

**Règle d'or :** Quand on doute, on met des parenthèses. C'est une bonne pratique de codage, pas une faiblesse.

### 2.3 Court-circuit (Short-circuit Evaluation)

Python évalue les expressions logiques de gauche à droite et **s'arrête dès que le résultat est déterminé**.

```python
# Avec and : s'arrête si la première est False
if total != 0 and (somme / total) > 5:
    # Si total == 0, la division n'est JAMAIS calculée → pas de division par zéro
    print("Ratio élevé")

# Avec or : s'arrête si la première est True
if cache_valide or charger_depuis_db():
    # Si cache_valide est True, charger_depuis_db() n'est JAMAIS appelée
    utiliser_donnees()
```

Ce mécanisme est fondamental pour écrire des conditions robustes sans erreurs d'exécution.

---

## Chapitre III — Structures de Test (Sélection)

### 3.1 Philosophie des structures de test

Une structure de test implémente la **sélection** : l'idée qu'un programme peut choisir différents chemins d'exécution selon les données. C'est ce qui distingue un programme intelligent d'une simple séquence de calculs.

La condition d'un `if` est évaluée comme une expression booléenne. Tout ce qui peut être évalué à `True` ou `False` est une condition valide.

### 3.2 La structure `if` à une voie

```python
if condition:
    bloc_si_vrai
```

Le bloc est exécuté **uniquement** si la condition est `True`. Si elle est `False`, le programme saute le bloc et continue après. Il n'y a pas de branche alternative.

**Cas d'usage :** Appliquer une transformation optionnelle (ex: "si la valeur est négative, la mettre à zéro").

```python
# Nettoyage : forcer les valeurs négatives à zéro
if valeur < 0:
    valeur = 0
# L'exécution continue ici dans tous les cas
print(valeur)
```

### 3.3 La structure `if-else` à deux voies

```python
if condition:
    bloc_si_vrai
else:
    bloc_si_faux
```

**Un seul** des deux blocs sera toujours exécuté. Les blocs sont **mutuellement exclusifs** et **exhaustifs** (tout cas est couvert).

**Invariant important :** `else` ne possède pas de condition. Son bloc s'exécute pour tout ce qui ne satisfait pas la condition du `if`.

```python
# Exemple : classification données
taille = float(input("Taille du fichier (Mo) : "))
if taille > 100:
    categorie = "Gros fichier"
else:
    categorie = "Fichier normal"
print("Catégorie :", categorie)
```

### 3.4 La structure `if-elif-else` multi-voies

```python
if condition_1:
    bloc_1
elif condition_2:
    bloc_2
elif condition_3:
    bloc_3
else:
    bloc_par_defaut
```

**Fonctionnement critique :** Les conditions sont évaluées **dans l'ordre**, et le premier bloc dont la condition est `True` s'exécute. **Toutes les branches suivantes sont ignorées**, même si leurs conditions seraient aussi `True`.

```python
note = 85

# Correct : elif garantit l'exclusivité
if note >= 90:
    print("A")
elif note >= 80:   # Testé SEULEMENT si note < 90
    print("B")     # ← Cette branche s'exécute pour 85
elif note >= 70:   # Ignorée (B déjà trouvé)
    print("C")
else:
    print("Échec")

# Incorrect : if multiples (tout est évalué)
if note >= 90: print("A")
if note >= 80: print("B")  # S'exécute aussi pour note=95 !
if note >= 70: print("C")  # S'exécute aussi pour note=95 !
```

**Question d'examen classique :** "Quelle est la différence entre `elif` et `if` ?" → `elif` stoppe la chaîne dès le premier `True`; des `if` séparés évaluent tous les cas indépendamment.

### 3.5 L'opérateur ternaire (conditionnel)

```python
valeur = expression_si_vrai if condition else expression_si_faux
```

C'est une **expression**, pas une instruction. Elle retourne une valeur et peut être placée dans une affectation, un `print()`, etc.

```python
# Forme classique
if score >= 60:
    resultat = "Réussi"
else:
    resultat = "Échec"

# Forme ternaire équivalente
resultat = "Réussi" if score >= 60 else "Échec"

# Utilisation dans print directement
print("Accès autorisé" if age >= 18 else "Accès refusé")
```

**Bonne pratique :** Utiliser le ternaire uniquement pour des affectations simples. Pour des blocs complexes ou des conditions multiples, la forme `if-else` est plus lisible.

### 3.6 Tests imbriqués (Nested)

Il est possible de placer une structure de test à l'intérieur d'une autre. C'est utile pour les hiérarchies de décisions.

```python
salaire = float(input("Salaire : "))

if salaire < 0:
    print("Erreur : salaire négatif")
else:
    # Test imbriqué, exécuté seulement si salaire >= 0
    if salaire >= 100000:
        taux = 0.45
    elif salaire >= 70000:
        taux = 0.32
    elif salaire >= 40000:
        taux = 0.18
    else:
        taux = 0.10
    impot = salaire * taux
    print(f"Impôt dû : {impot:.2f}$")
```

**Point technique :** La validation d'entrée (salaire < 0) en premier est une bonne pratique : elle protège le code principal des données invalides avant de faire des calculs.

### 3.7 Conditions composées — Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs conditions en une seule expression.

```python
# ET logique : les DEUX doivent être vraies
if age >= 18 and revenu > 30000:
    print("Éligible au prêt")

# OU logique : AU MOINS UNE doit être vraie
if est_vip or total_achats > 1000:
    print("Remise appliquée")

# NOT : inverse la condition
if not champ.isdigit():
    print("Erreur : ce champ doit être numérique")

# Combinaison complexe (utiliser des parenthèses pour la clarté)
if (age >= 18 and age <= 65) and (ville == "Montreal" or ville == "Quebec"):
    print("Profil cible")
```

**Priorité des opérateurs logiques :** `not` > `and` > `or`

```python
# Sans parenthèses : interprété comme not(a) and b or c
not a and b or c

# Avec parenthèses explicites (recommandé) :
(not a) and b or c
# ou mieux :
((not a) and b) or c
```

---

## Chapitre IV — Structures de Boucle (Répétition)

### 4.1 Philosophie des structures de boucle

Une boucle exprime l'idée qu'une série d'instructions doit se répéter selon une règle. Il existe deux paradigmes :

1. **Répétition déterministe** (`for`) : on sait combien de fois avant de commencer.
2. **Répétition non-déterministe** (`while`) : on continue tant qu'une condition est remplie, sans savoir à l'avance quand elle s'arrêtera.

Le choix entre les deux impacte la lisibilité, la sécurité (risque de boucle infinie), et la performance.

### 4.2 La boucle `while` — Anatomie complète

```python
# Les 3 composants obligatoires
initialisation   # AVANT la boucle : définir et initialiser la variable de contrôle
while condition: # TEST de la condition (si False dès le début : le corps n'exécute JAMAIS)
    corps        # Instructions à répéter
    mise_à_jour  # MODIFIER la variable de contrôle pour progresser vers la sortie
```

**Invariant de boucle :** La condition doit éventuellement devenir `False`. Si ce n'est pas garanti, c'est une boucle infinie.

```python
# Exemple complet annoté : trouver la 1ère puissance de 2 > N
n = int(input("N : "))
puissance = 1             # INITIALISATION
while puissance <= n:     # CONDITION : continue tant que pas dépassé
    puissance *= 2        # MISE À JOUR : puissance croît donc condition finira par être False
print(f"Première puissance de 2 supérieure à {n} : {puissance}")
```

**Cas d'usage typiques de `while` :**

```python
# 1. Validation de saisie (boucle de garde)
note = -1
while not (0 <= note <= 100):
    note = int(input("Note (0-100) : "))
    if not (0 <= note <= 100):
        print("Valeur hors plage, recommencez.")

# 2. Lecture jusqu'à sentinelle (valeur de fin)
total = 0
nb = 0
valeur = float(input("Valeur (999 pour terminer) : "))
while valeur != 999:
    total += valeur
    nb += 1
    valeur = float(input("Valeur (999 pour terminer) : "))
if nb > 0:
    print(f"Moyenne : {total/nb:.2f}")

# 3. Menu interactif persistant
continuer = True
while continuer:
    print("1. Option A  2. Option B  3. Quitter")
    choix = int(input("Choix : "))
    if choix == 3:
        continuer = False   # Variable drapeau (flag)
    elif choix == 1:
        print("Option A exécutée")
    # ...
```

**Point technique — La variable drapeau (flag) :** Une variable booléenne (`flag = True`) qui contrôle la boucle est une alternative à `break`. Elle est parfois plus lisible car le point de sortie est explicite dans la condition de la boucle.

### 4.3 La boucle `for` — Mécanisme d'itération

```python
for variable_iteration in iterable:
    corps
```

À chaque passage (itération), la `variable_iteration` prend la valeur suivante de l'`iterable`. La boucle s'arrête automatiquement quand l'itérable est épuisé.

Un **itérable** est tout objet qu'on peut parcourir élément par élément. Les itérables du cours :
- **Chaîne de caractères** (`str`) : parcourt caractère par caractère
- **Objet `range`** : génère une séquence de nombres à la demande

```python
# Parcourir une chaîne
for caractere in "PYTHON":
    print(caractere)  # P, Y, T, H, O, N (un par ligne)

# Parcourir avec range
for i in range(1, 6):
    print(i)          # 1, 2, 3, 4, 5

# La variable d'itération est disponible DANS le corps
for i in range(1, 11):
    print(f"{i} × 7 = {i * 7}")
```

### 4.4 La fonction `range()` — Anatomie complète

`range(debut, fin, pas)` est un **générateur paresseux** : il ne crée pas la liste en mémoire, il génère les valeurs une par une à la demande. C'est très efficace même pour `range(1, 1_000_000)`.

**Règle absolue :** La valeur de `fin` est **toujours exclue**.

```python
range(5)          # 0, 1, 2, 3, 4     — commence à 0, fin exclue
range(1, 6)       # 1, 2, 3, 4, 5     — debut inclus, fin exclue
range(0, 10, 2)   # 0, 2, 4, 6, 8     — pas de 2
range(10, 0, -1)  # 10, 9, ..., 2, 1  — compte à rebours (pas négatif)
range(10, 0, -2)  # 10, 8, 6, 4, 2    — compte à rebours par 2

# ERREUR FRÉQUENTE : pour afficher 1 à 10 inclus
range(1, 10)    # FAUX — donne 1 à 9
range(1, 11)    # CORRECT — donne 1 à 10
```

**Équivalence `for` ↔ `while` :**
```python
# Ces deux boucles sont équivalentes
for i in range(1, 6):
    print(i)

compteur = 1
while compteur < 6:
    print(compteur)
    compteur += 1
```

Préférer `for` pour sa concision et sa sécurité (pas de risque de boucle infinie).

### 4.5 Boucles imbriquées (Nested Loops)

Une boucle peut contenir une autre boucle dans son corps. La boucle interne s'exécute **complètement** à chaque itération de la boucle externe.

```python
# Nombre total d'exécutions = nb_iter_externe × nb_iter_interne
for i in range(1, 4):     # 3 itérations externes
    for j in range(1, 4): # 3 itérations internes × 3 = 9 au total
        print(f"({i},{j})", end=" ")
    print()  # Retour à la ligne après chaque ligne de la boucle externe
```

Sortie :
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

**Application classique :** Tables de multiplication, génération de patterns, grilles de données.

### 4.6 Transferts de contrôle : `break` et `continue`

#### `break` — Sortie immédiate

`break` arrête immédiatement l'exécution de la boucle courante (pas des boucles externes) et transfert le contrôle à la première instruction après la boucle.

```python
# Recherche : on cherche le premier multiple de 17 entre 1 et 1000
for i in range(1, 1001):
    if i % 17 == 0:
        print(f"Trouvé : {i}")
        break           # Inutile de continuer, on a trouvé
# L'exécution continue ici après le break

# Équivalence sémantique : break = "objectif atteint, sortir"
```

**Cas d'usage :** Recherche où on s'arrête dès qu'on trouve, validation avec nombre maximal d'essais.

#### `continue` — Saut d'itération

`continue` interrompt l'**itération courante** et passe directement à la suivante. Le reste du corps de la boucle pour cette itération est ignoré.

```python
# Filtrage : sommer uniquement les valeurs positives
total = 0
for i in range(10):
    v = float(input(f"Valeur {i+1} : "))
    if v < 0:
        print("Valeur négative ignorée.")
        continue    # Saute le `total += v` pour cette itération
    total += v
print(f"Somme des positifs : {total}")

# Nettoyer une chaîne : reconstruire sans les espaces
chaine = "data avec espaces"
resultat = ""
for c in chaine:
    if c == " ":
        continue    # Saute les espaces
    resultat += c
print(resultat)  # "dataavecespaces"
```

**Tableau comparatif `break` vs `continue` :**

| | `break` | `continue` |
|---|---|---|
| Effet | Quitte la boucle | Saute à l'itération suivante |
| Position d'exécution | Instruction après la boucle | Début de l'itération suivante |
| La condition est-elle réévaluée ? | Non | Oui |
| Usage typique | "Trouvé ce qu'on cherchait" | "Ignorer ce cas particulier" |

---

## Chapitre V — Stratégies et Patterns pour l'Examen

### 5.1 Algorithme de traitement par accumulation

L'accumulation est le pattern le plus fréquent dans les exercices. Il consiste à maintenir un résultat intermédiaire qui se construit itération par itération.

**Structure générale :**
```python
# Initialisation des accumulateurs AVANT la boucle
somme = 0
compteur = 0
maximum = float('-inf')   # ou la première valeur saisie

for i in range(n):
    valeur = float(input(f"Valeur {i+1} : "))
    # Mise à jour des accumulateurs
    somme += valeur
    compteur += 1
    if valeur > maximum:
        maximum = valeur

# Calcul final APRÈS la boucle
if compteur > 0:
    moyenne = somme / compteur
```

**Erreur classique :** Initialiser les accumulateurs à `0` même quand `0` est une valeur possible dans les données. Pour le maximum, initialiser à la première valeur ou à `float('-inf')`.

### 5.2 Comment choisir la bonne structure

Utiliser cette grille de décision :

```
Problème à résoudre
       │
       ├─ Répétition nécessaire ?
       │         │
       │      Non → Utiliser if/elif/else + séquence
       │         │
       │      Oui ─┬─ Nombre d'itérations connu à l'avance ?
       │            │
       │         Oui ──────────────→ for + range(n)
       │            │
       │          Non ─┬─ Parcourir une chaîne ?
       │                │
       │             Oui ──────────→ for c in chaine:
       │                │
       │              Non ─┬─ Nombre inconnu d'itérations ?
       │                    │
       │                 Oui ──────→ while
       │                    │
       │                  Non ─────→ Revoir le problème
```

### 5.3 L'importance de l'initialisation

**Règle critique :** Toute variable utilisée dans une boucle comme accumulateur ou comparateur DOIT être initialisée avant la boucle.

```python
# ERREUR : total non initialisé
for i in range(5):
    total += float(input())  # NameError : total n'existe pas encore

# CORRECT
total = 0
for i in range(5):
    total += float(input())
```

### 5.4 Analyse de complexité simple

Pour l'examen, savoir compter le nombre d'exécutions :

```python
# Boucle simple : N itérations
for i in range(N):
    print(i)      # Exécuté N fois

# Boucles imbriquées : N × M itérations
for i in range(N):
    for j in range(M):
        print(i, j)  # Exécuté N × M fois

# Exemple : range(5) externe, range(4) interne → 5 × 4 = 20 exécutions
```

**Question d'examen :** "Combien de lignes affiche ce code ?"
```python
i = 0
while i < 5:
    j = 0
    while j < i:   # Variable ! j < i, pas j < 4
        print(i, j)
        j += 1
    i += 1
# Quand i=0 : j < 0 → 0 itérations
# Quand i=1 : j < 1 → 1 itération
# Quand i=2 : j < 2 → 2 itérations
# Quand i=3 : j < 3 → 3 itérations
# Quand i=4 : j < 4 → 4 itérations
# Total : 0+1+2+3+4 = 10 lignes
```

### 5.5 Techniques de débogage mental

Quand un exercice semble incorrect, effectuer une **trace d'exécution** à la main :

```python
# Exercice : que s'affiche-t-il ?
a = 10
b = 3
while a > b:
    a = a - b
    print(a)

# Trace manuelle :
# Itération 1 : a=10, b=3, cond: 10>3=True → a=10-3=7 → print(7)
# Itération 2 : a=7,  b=3, cond: 7>3=True  → a=7-3=4  → print(4)
# Itération 3 : a=4,  b=3, cond: 4>3=True  → a=4-3=1  → print(1)
# Itération 4 : a=1,  b=3, cond: 1>3=False → SORTIE
# Réponse : 7, 4, 1
```

### 5.6 Pièges récurrents à l'examen

#### Piège 1 : Le `while` qui ne démarre jamais
```python
n = 10
while n > 100:   # False dès le départ !
    n += 1       # Ce code ne s'exécute JAMAIS
print(n)         # Affiche 10
```

#### Piège 2 : `if` vs `elif` dans la cascade de notes
```python
note = 75
# Avec if séparés (INCORRECT pour une classification exclusive)
if note >= 70: print("C")  # True → affiche C
if note >= 80: print("B")  # False → rien
if note >= 90: print("A")  # False → rien
# Résultat : "C" (correct par chance)

note = 95
if note >= 70: print("C")  # True → affiche C  ← PROBLÈME
if note >= 80: print("B")  # True → affiche B  ← PROBLÈME
if note >= 90: print("A")  # True → affiche A
# Résultat : "C", "B", "A" (INCORRECT)

# CORRECT avec elif
if note >= 90: print("A")
elif note >= 80: print("B")
elif note >= 70: print("C")
# Pour note=95 → affiche seulement "A"
```

#### Piège 3 : Oublier de lire AVANT la boucle sentinelle
```python
# INCORRECT : la première valeur n'est jamais traitée si différente de FIN
while saisie.upper() != "FIN":
    saisie = input()   # La saisie se fait à la fin, pas au début

# CORRECT : patron "lire-tester-traiter"
saisie = input("Valeur : ")          # Lire avant
while saisie.upper() != "FIN":       # Tester
    traiter(saisie)                  # Traiter
    saisie = input("Valeur : ")      # Lire à nouveau pour le prochain tour
```

#### Piège 4 : Indentation incorrecte
```python
# INCORRECT : print est dans la boucle (s'exécute N fois)
somme = 0
for i in range(1, 6):
    somme += i
    print(f"Somme finale : {somme}")  # S'affiche 5 fois !

# CORRECT : print est après la boucle
somme = 0
for i in range(1, 6):
    somme += i
print(f"Somme finale : {somme}")  # S'affiche 1 fois (15)
```

---

## Annexe — Résumé des Formules Importantes

### Formules mathématiques utiles au cours

```python
# Moyenne de N valeurs
moyenne = somme / n

# Pourcentage
taux = (partie / total) * 100

# Intérêt simple : I = C × t × d
interet = capital * taux_annuel * duree_annees

# Intérêt composé : Cn = C0 × (1 + t)^n
capital_final = capital_initial * (1 + taux) ** annees

# Distance euclidienne
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

# IMC
imc = poids / (taille ** 2)

# Conversion Celsius → Fahrenheit
F = C * 9/5 + 32

# Conversion Celsius → Kelvin
K = C + 273.15

# Conversion secondes → H:M:S
heures   = secondes_totales // 3600
minutes  = (secondes_totales % 3600) // 60
secondes = secondes_totales % 60
```

### Méthodes de chaîne par catégorie

```python
# Transformation de casse
"data".upper()        # "DATA"
"DATA".lower()        # "data"

# Nettoyage
"  abc  ".strip()     # "abc"
"abc abc".replace(" ", "_")  # "abc_abc"

# Tests (retournent True/False)
"123".isdigit()       # True (que des chiffres)
"abc".isdigit()       # False
"url.ca".endswith(".ca")   # True
"AB_1".startswith("AB")    # True
"@" in "user@mail.com"     # True (opérateur in)

# Accès
"python"[0]           # "p"  (premier)
"python"[-1]          # "n"  (dernier)
len("python")         # 6
```

---

*Manuel de révision théorique — Programme C45 Hiver | Niveau universitaire*