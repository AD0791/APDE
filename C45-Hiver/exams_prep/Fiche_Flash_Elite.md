# FICHE FLASH : RÉFLEXES DE SURVIE (15 MIN AVANT L'EXAMEN)

**Objectif :** Zéro erreur d'inattention. Rappel des syntaxes critiques.

---

## 1. SYNTAXE PYTHON (Checklist Visuelle)
- [ ] `:` présent après chaque `if`, `else`, `while`, `for`, `def`, `class`.
- [ ] Indentation (4 espaces) respectée rigoureusement.
- [ ] Parenthèses fermées par paires `( )`.
- [ ] Pas de majuscules aux mots-clés (`if`, pas `If` ; `while`, pas `While`).
- [ ] Guillemets cohérents (`" "` ou `' '`).

## 2. ALGORITHMIE (Pseudo-code)
- [ ] Déclaration obligatoire : `Variable nom_var en Type`.
- [ ] Affectation : `nom_var ← valeur` (Utilisez la flèche !).
- [ ] Lecture : `Lire nom_var`.
- [ ] Écriture : `Écrire "Message", valeur`.
- [ ] Fin de structure : `Fin Si`, `Fin Tant que`, `Fin Pour`.

## 3. TABLEAUX / LISTES
- [ ] Premier élément = Indice **0**.
- [ ] Dernier élément = Indice **Taille - 1**.
- [ ] Parcours complet : `for i in range(len(liste)):`

## 4. POO (Programmation Orientée Objet)
- [ ] Constructeur : `def __init__(self, ...):`
- [ ] Le mot `self` présent dans TOUTES les méthodes de classe.
- [ ] Appel attribut : `self.attribut`.
- [ ] Héritage : `class Enfant(Parent):`.

## 5. LES "PIÈGES À C" (Critiques)
- **Confusion `=` et `==`** : `=` affecte, `==` compare.
- **Conversion `input`** : `float(input())` pour les prix/notes, `int(input())` pour les comptes.
- **Concaténation** : On ne peut pas faire `"Texte" + 10`. Utilisez `f"Texte {10}"`.
- **Indice hors limite** : Accéder à `Tab[10]` dans un tableau de taille 10 cause un crash.

---
**RÉFLEXE FINAL :** Relisez votre code à l'envers (de bas en haut) pour repérer les oublis de parenthèses ou de deux-points.
