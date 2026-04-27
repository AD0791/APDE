# Fiche de Synthèse — Fondamentaux de la Programmation Python
### Spécialiste en intégration de données | Révision complète pour l'examen

---

## 1. TYPES DE DONNÉES FONDAMENTAUX

| Type   | Mot-clé | Exemples               | Notes importantes                                   |
|--------|---------|------------------------|-----------------------------------------------------|
| Entier | `int`   | `0`, `-10`, `1_000_000`| Précision arbitraire en Python (pas de dépassement) |
| Réel   | `float` | `3.14`, `-0.5`, `2e10` | Norme IEEE 754 — attention aux erreurs de précision |
| Chaîne | `str`   | `"data"`, `'csv'`      | **Immuable** — chaque modification crée une nouvelle chaîne |
| Booléen| `bool`  | `True`, `False`        | Sous-type de `int` : `True == 1`, `False == 0`      |

> **Piège classique :** `0.1 + 0.2` donne `0.30000000000000004`, pas `0.3`. Les flottants ne sont pas exacts.

---

## 2. FONCTIONS ESSENTIELLES

| Fonction              | Rôle                                          | Exemple                              |
|-----------------------|-----------------------------------------------|--------------------------------------|
| `input("msg")`        | Saisie utilisateur — retourne **toujours** `str` | `x = input("Valeur : ")`          |
| `print(val)`          | Affichage à l'écran                           | `print("Résultat : {}".format(n))`   |
| `int(x)`              | Convertit en entier (troncature, pas arrondi) | `int(3.9)` → `3`                     |
| `float(x)`            | Convertit en réel                             | `float("3.14")` → `3.14`            |
| `str(x)`              | Convertit en chaîne                           | `str(42)` → `"42"`                   |
| `type(x)`             | Retourne le type exact                        | `type(3.0)` → `<class 'float'>`      |
| `isinstance(x, T)`    | Vérifie appartenance au type (**recommandé**) | `isinstance(3.0, float)` → `True`    |
| `len(x)`              | Longueur d'une chaîne ou séquence             | `len("data")` → `4`                  |
| `round(x, n)`         | Arrondit à n décimales                        | `round(3.14159, 2)` → `3.14`         |

> **Piège :** `int("10.5")` lève une erreur. Solution : `int(float("10.5"))` → `10`.

---

## 3. OPÉRATEURS ET TABLE DE PRÉCÉDENCE

### 3.1 Opérateurs arithmétiques

| Opérateur | Nom                | Exemple        | Résultat |
|-----------|--------------------|----------------|----------|
| `**`      | Puissance          | `2 ** 10`      | `1024`   |
| `*`       | Multiplication     | `3 * 4`        | `12`     |
| `/`       | Division réelle    | `7 / 2`        | `3.5`    |
| `//`      | Division entière   | `7 // 2`       | `3`      |
| `%`       | Modulo (reste)     | `7 % 2`        | `1`      |
| `+`       | Addition           | `3 + 4`        | `7`      |
| `-`       | Soustraction       | `7 - 3`        | `4`      |

### 3.2 Table de précédence complète (du plus au moins prioritaire)

```
1. ()          — Parenthèses (force l'ordre)
2. **          — Puissance (associativité DROITE : 2**3**2 = 2**(3**2) = 512)
3. *, /, //, % — Multiplicatifs (même niveau, gauche à droite)
4. +, -        — Additifs (même niveau, gauche à droite)
5. ==, !=, <, >, <=, >= — Relationnels (comparaisons)
6. not         — Négation logique
7. and         — ET logique
8. or          — OU logique
```

> **Exemple crucial :** `2 + 3 * 4` = `14` (pas `20`). Toujours utiliser `()` pour clarifier.

---

## 4. TABLES DE VÉRITÉ DES OPÉRATEURS LOGIQUES

### `and` (ET)
| A       | B       | A and B |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `False` |
| `False` | `True`  | `False` |
| `False` | `False` | `False` |

### `or` (OU)
| A       | B       | A or B  |
|---------|---------|---------|
| `True`  | `True`  | `True`  |
| `True`  | `False` | `True`  |
| `False` | `True`  | `True`  |
| `False` | `False` | `False` |

### `not` (NON)
| A       | not A   |
|---------|---------|
| `True`  | `False` |
| `False` | `True`  |

> **Court-circuit (Short-circuit evaluation) :**
> - `and` : si la 1ère condition est `False`, la 2ème n'est **jamais** évaluée.
> - `or`  : si la 1ère condition est `True`, la 2ème n'est **jamais** évaluée.
>
> **Application :** `if total != 0 and (somme / total) > 5:` — division par zéro impossible grâce au court-circuit.

---

## 5. STRUCTURES DE TEST (SÉLECTION)

### 5.1 Les quatre formes

```
┌─────────────────┐   ┌─────────────────────┐   ┌──────────────────────┐   ┌──────────────────┐
│  UNE VOIE       │   │  DEUX VOIES         │   │  MULTI-VOIES         │   │  TERNAIRE        │
│                 │   │                     │   │                      │   │                  │
│ if cond:        │   │ if cond:            │   │ if cond1:            │   │ x = A if cond    │
│     bloc        │   │     bloc_vrai       │   │     bloc1            │   │     else B       │
│                 │   │ else:               │   │ elif cond2:          │   │                  │
│ (rien si False) │   │     bloc_faux       │   │     bloc2            │   │ Affecte A si     │
│                 │   │                     │   │ elif cond3:          │   │ cond True,       │
└─────────────────┘   └─────────────────────┘   │     bloc3            │   │ sinon B          │
                                                 │ else:                │   └──────────────────┘
                                                 │     bloc_defaut      │
                                                 └──────────────────────┘
```

### 5.2 Logique de fonctionnement (flowchart)

```
         ┌────────────┐
         │  Condition │
         └─────┬──────┘
          True │  False
         ┌─────┘
         ▼
    [Bloc if]    (elif évalué SEULEMENT si if est False)
                 (else exécuté SEULEMENT si TOUT le reste est False)
```

### 5.3 Règles critiques

- **`elif` vs `if` multiples** : `elif` s'arrête dès qu'une condition est vraie. Des `if` séparés testent **tous** les cas.
- **Indentation** : 4 espaces obligatoires. L'indentation définit l'appartenance au bloc.
- **`pass`** : mot-clé valide pour un bloc vide (placeholder).

```python
# DIFFÉRENCE FONDAMENTALE
x = 15
# Avec elif : un seul bloc s'exécute
if x > 10: print("A")   # imprime A
elif x > 5: print("B")  # ignoré car la 1ère était True

# Avec if séparés : plusieurs blocs peuvent s'exécuter
if x > 10: print("A")   # imprime A
if x > 5: print("B")    # imprime aussi B (test indépendant)
```

---

## 6. STRUCTURES DE BOUCLE (RÉPÉTITION)

### 6.1 Boucle `while` — Non-déterministe

```python
# PATRON OBLIGATOIRE : 3 éléments
initialisation   # variable de contrôle définie AVANT la boucle
while condition:
    corps        # instructions répétées
    mise_à_jour  # MODIFIER la variable de contrôle → sinon boucle infinie !
```

**Cas d'utilisation :** Nombre d'itérations inconnu à l'avance (lecture jusqu'à sentinelle, validation de saisie, jeu).

### 6.2 Boucle `for` — Déterministe

```python
for element in iterable:
    corps
```

**Cas d'utilisation :** Nombre d'itérations connu à l'avance (parcourir une chaîne, itérer N fois avec range).

### 6.3 Fonction `range()` — Formes importantes

| Forme                  | Génère                        | Exemple                       |
|------------------------|-------------------------------|-------------------------------|
| `range(n)`             | `0, 1, 2, ..., n-1`           | `range(5)` → `0,1,2,3,4`     |
| `range(debut, fin)`    | `debut, ..., fin-1`           | `range(1,6)` → `1,2,3,4,5`   |
| `range(debut,fin,pas)` | avec incrément                | `range(0,10,2)` → `0,2,4,6,8`|
| `range(n, 0, -1)`      | compte à rebours              | `range(5,0,-1)` → `5,4,3,2,1`|

> **Règle d'or :** La valeur de `fin` est **toujours exclue**.

### 6.4 Transferts de contrôle

| Instruction | Effet                                              | Utilisation typique                 |
|-------------|----------------------------------------------------|-------------------------------------|
| `break`     | Quitte la boucle **immédiatement**                 | Recherche : "trouvé, on s'arrête"  |
| `continue`  | Saute à l'**itération suivante**                   | Filtrage : "donnée invalide, skip" |
| `pass`      | Ne fait rien (bloc syntaxiquement valide)          | Placeholder de développement       |

### 6.5 Tableau de choix : `while` vs `for`

| Critère                          | `while`                        | `for`                        |
|----------------------------------|--------------------------------|------------------------------|
| Nombre d'itérations              | Inconnu                        | Connu ou borné               |
| Variable de contrôle             | Gérée manuellement (attention!)| Gérée automatiquement        |
| Risque de boucle infinie         | **OUI** si oubli de mise à jour| **NON** (range fini)         |
| Parcourir une chaîne             | Possible (index manuel)        | **Préféré** (`for c in s:`) |
| Répétition N fois                | Possible                       | **Préféré** (`range(N)`)     |
| Lecture jusqu'à sentinelle       | **Préféré**                    | Non adapté                   |

---

## 7. FORMATAGE DE SORTIE

### 7.1 Méthode `.format()`

```python
"{:.2f}".format(3.14159)       # "3.14"         — 2 décimales
"{:8.2f}".format(3.14)         # "    3.14"      — largeur 8, 2 décimales, aligné à droite
"{:08.2f}".format(3.14)        # "00003.14"      — rempli de zéros
"{:12s}".format("data")        # "data        "  — chaîne sur 12 chars, alignée à gauche
"{:02d}".format(7)             # "07"             — entier sur 2 chiffres avec zéro
"{:.0%}".format(0.75)          # "75%"           — pourcentage sans décimales
"{:e}".format(12345.0)         # "1.234500e+04"  — notation scientifique
```

### 7.2 F-strings (Python 3.6+)

```python
nom = "Alice"
score = 98.5
print(f"Étudiant : {nom}, Score : {score:.1f}%")
# → "Étudiant : Alice, Score : 98.5%"
```

---

## 8. MODULE `random`

```python
import random
random.randint(a, b)   # Entier entre a et b INCLUS (contrairement à range où fin est exclue)
```

> **Différence critique :** `random.randint(1, 6)` inclut `6`. `range(1, 6)` exclut `6`.

---

## 9. MÉTHODES DE CHAÎNE ESSENTIELLES

| Méthode              | Rôle                                    | Exemple                          |
|----------------------|-----------------------------------------|----------------------------------|
| `.upper()`           | Tout en majuscules                      | `"data".upper()` → `"DATA"`     |
| `.lower()`           | Tout en minuscules                      | `"DATA".lower()` → `"data"`     |
| `.strip()`           | Supprime espaces/sauts autour           | `"  abc  ".strip()` → `"abc"`   |
| `.replace(a, b)`     | Remplace `a` par `b`                    | `"a b".replace(" ","_")` → `"a_b"` |
| `.startswith(s)`     | Commence par `s` ?                      | `"data.csv".startswith("data")` → `True` |
| `.endswith(s)`       | Finit par `s` ?                         | `"file.csv".endswith(".csv")` → `True` |
| `.isdigit()`         | Uniquement des chiffres ?               | `"123".isdigit()` → `True`       |
| `s[0]`, `s[-1]`      | Premier / dernier caractère             | `"abc"[0]` → `"a"`, `"abc"[-1]` → `"c"` |
| `in`                 | Appartenance                            | `"@" in "a@b"` → `True`          |

---

## 10. PATTERNS CLASSIQUES À MAÎTRISER

### 10.1 Accumulateur (somme, produit, compteur)
```python
somme = 0               # initialisation AVANT la boucle
for i in range(1, n+1):
    somme += i          # accumulation
```

### 10.2 Recherche de max/min
```python
maxi = premier_element  # initialiser avec la 1ère valeur, jamais avec 0 (si valeurs négatives)
for i in range(2, n+1):
    v = float(input())
    if v > maxi:
        maxi = v
```

### 10.3 Validation de saisie (boucle de garde)
```python
note = -1                          # valeur initiale invalide pour forcer l'entrée
while note < 0 or note > 100:
    note = int(input("Note (0-100) : "))
    if note < 0 or note > 100:
        print("Saisie invalide, recommencez.")
```

### 10.4 Sentinelle
```python
saisie = input("Valeur (FIN pour terminer) : ")
while saisie.upper() != "FIN":
    # traitement
    saisie = input("Valeur (FIN pour terminer) : ")
```

### 10.5 Compteurs multiples dans une boucle
```python
nb_pairs = nb_impairs = total = 0
for i in range(n):
    v = int(input())
    total += v
    if v % 2 == 0:
        nb_pairs += 1
    else:
        nb_impairs += 1
```

---

## 11. PIÈGES CLASSIQUES À L'EXAMEN

| Piège                              | Erreur fréquente                        | Solution correcte                         |
|------------------------------------|-----------------------------------------|-------------------------------------------|
| `input()` retourne toujours `str`  | `x = input()` puis `x + 5`             | `x = int(input())`                        |
| `int("10.5")` échoue               | Convertir directement                   | `int(float("10.5"))`                      |
| Boucle infinie `while`             | Oublier `i += 1` dans le corps         | Toujours vérifier la mise à jour          |
| `range(1, 10)` exclut 10           | Écrire `range(1, 10)` pour 1 à 10      | `range(1, 11)`                            |
| `elif` vs `if` multiples           | `if` teste même si précédent `True`     | `elif` stoppe au 1er `True`               |
| `=` vs `==`                        | `if x = 5` (erreur de syntaxe)         | `if x == 5`                               |
| `//` arrondit vers le bas          | `7 // 2` donne `3`, pas `3.5`          | Utiliser `/` pour division réelle         |
| `**` associativité à droite        | `2 ** 3 ** 2` = `2 ** 9` = `512`       | Mettre des parenthèses pour clarifier     |
| Variable non initialisée           | Utiliser `total` avant `total = 0`      | Toujours initialiser avant la boucle      |
| `random.randint` vs `range`        | `randint(1,6)` inclut 6, `range(1,6)` exclut 6 | Attention aux bornes selon le contexte |

---

## 12. RÉFÉRENCE RAPIDE : DIVISION ENTIÈRE ET MODULO

```
Règle fondamentale : a = (a // b) * b + (a % b)

Exemples :
  17 // 5 = 3    (quotient entier)
  17 %  5 = 2    (reste)

Applications classiques :
  n % 2 == 0     → n est pair
  n % 2 != 0     → n est impair
  n % k == 0     → n est divisible par k
  secondes // 3600  → heures
  secondes % 3600   → secondes restantes après extraction des heures
  n // 1000      → chiffre des milliers (pour n < 10000)
  (n % 1000) // 100 → chiffre des centaines
```

---

*Fiche de synthèse complète — Programme C45 Hiver | Révisée pour l'examen spécialiste données*