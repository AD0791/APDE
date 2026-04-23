# Guide de Révision Complet : Programmation Python (C45-Hiver)

Ce document est conçu pour maximiser votre efficacité de révision en vous concentrant sur les éléments essentiels qui rapportent le plus de points.

---

## Partie 1 : La Règle de Pareto (Le 20% qui donne 80% de résultats)

Pour réussir l'examen, vous devez maîtriser parfaitement ces concepts de base. La majorité des points de l'intra et de l'examen final reposent sur eux.

### 1. La Structure Fondamentale (S.I.P.)
Tout programme simple suit ce schéma :
- **S**aisie : `variable = input("Message")` (Pensez à convertir : `int()` ou `float()`)
- **I**nstructions : Calculs et logique (`x = y + 2`)
- **P**rint : Affichage du résultat (`print(f"Le résultat est {x}")`)

### 2. Les Tests (L'Indentation est LOI)
- **Syntaxe :** `if condition :` (N'oubliez pas les **deux-points** !)
- **Indentation :** Tout ce qui est à l'intérieur du bloc doit être décalé.
- **Comparaison :** `==` pour tester l'égalité (Ne confondez pas avec `=` qui est l'affectation).

### 3. Les Boucles (Répétition)
- **`for i in range(n):`** : Quand on connaît le nombre de tours (ex: 7 jours de la semaine).
- **`while condition:`** : Quand on attend un événement (ex: "Voulez-vous continuer ?").

### 4. Les Fonctions
- `def nom_fonction(parametre):`
- `return resultat` (Indispensable pour récupérer une valeur).

---

## Partie 2 : Concepts Détaillés & Mnémotechniques

### 1. Les Variables et Types
**Mnémotechnique : "V.A.L.E.U.R."**
- **V**ariable : Un nom clair (ex: `prix_total`).
- **A**ffectation : Utiliser `=`.
- **L**ecture : `input()`.
- **E**ntier : `int` pour les nombres sans virgule.
- **U**nité réelle : `float` pour les nombres avec virgule (Utilisez le `.` et non la `,`).
- **R**envoi : `print()`.

*Pourquoi cette mnémotechnique ?* Elle rappelle que chaque variable stocke une **valeur** et qu'il faut définir son type correctement pour éviter les erreurs de calcul.

### 2. Les Erreurs de Syntaxe Classiques
**Mnémotechnique : "C.I.P.2"**
- **C**asse : Python est sensible à la casse (`Print` != `print`, `If` != `if`).
- **I**ndentation : Un espace de trop ou de moins casse le code.
- **P**arenthèses : Toujours par paires `( )`.
- **2** Points : Toujours après `if`, `else`, `for`, `while`, `def`.

*Pourquoi cette mnémotechnique ?* Ce sont les 4 points vérifiés systématiquement par les correcteurs dans les exercices de "Détection d'erreurs".

### 3. Listes et Séquences
**Mnémotechnique : "I.A.L."**
- **I**ndex : Commence toujours à **0**.
- **A**ppend : Pour ajouter à la fin.
- **L**en : Pour connaître la longueur.

### 4. Programmation Orientée Objet (POO)
**Mnémotechnique : "C.O.H.P."**
- **C**lasse : Le plan de construction (Le moule à gâteaux).
- **O**bjet : L'instance créée (Le gâteau).
- **H**éritage : Une classe "Enfant" qui reprend les caractéristiques du "Parent".
- **P**olymorphisme : Une même méthode qui agit différemment selon l'objet.

---

## Partie 3 : Exercices Corrigés (Difficulté Graduelle)

### Exercice 1 : Niveau Facile (Syntaxe & Saisie)
Écrivez un programme qui demande l'âge de l'utilisateur et affiche s'il est majeur (18 ans et plus) ou mineur.

**Solution :**
```python
age = int(input("Entrez votre âge : ")) # Conversion en int nécessaire
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

### Exercice 2 : Niveau Moyen (Boucles & Listes)
Créez une liste contenant 3 notes. Calculez la moyenne de ces notes à l'aide d'une boucle `for`.

**Solution :**
```python
notes = [15, 12, 18]
somme = 0
for note in notes:
    somme += note
moyenne = somme / len(notes)
print(f"La moyenne est : {moyenne}")
```

### Exercice 3 : Niveau Avancé (Fonctions & Logique)
Écrivez une fonction `calculer_prix(quantite, prix_unitaire)` qui applique une remise de 10% si la quantité est supérieure à 5, puis retourne le prix final.

**Solution :**
```python
def calculer_prix(quantite, prix_unitaire):
    total = quantite * prix_unitaire
    if quantite > 5:
        total = total * 0.90  # Applique 10% de remise
    return total

# Test
res = calculer_prix(6, 10)
print(f"Le prix total est : {res}") # Devrait afficher 54.0
```

---
*Document généré pour la révision du cours C45-Hiver.*
