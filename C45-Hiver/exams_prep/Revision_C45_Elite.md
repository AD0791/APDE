# GUIDE DE RÉVISION ÉLITE : INITIATION À LA PROGRAMMATION (C45-HIVER)

Ce guide est votre outil de maîtrise totale. Il synthétise les notes de cours, les exercices d'algorithmique et les standards de programmation Python 3.X.

---

## PARTIE 1 : LA RÈGLE DE PARETO (Le 20% pour 80% de réussite)

À l'examen, 80% des erreurs et des points perdus concernent ces quatre piliers. Maîtrisez-les, et vous garantissez votre réussite.

### 1. La Logique S.I.P. (Saisie - Instruction - Print)
Tout algorithme ou programme suit ce flux immuable :
- **S**aisie : Acquisition des données (`input()`, `lire`).
- **I**nstruction : Traitement logique (calculs, conditions, boucles).
- **P**rint : Communication du résultat (`print()`, `écrire`).
*Erreur fatale : Oublier de convertir les saisies numériques (`int()` ou `float()`).*

### 2. Le Mur de l'Indentation (La Loi de l'Espace)
En Python, l'espace n'est pas esthétique, il est **syntaxique**.
- Chaque bloc (après un `:`) doit être décalé de 4 espaces.
- **Analogie de la "Chambre"** : Si une instruction n'est pas alignée, elle n'est pas dans la bonne chambre (bloc) et ne s'exécutera pas au bon moment.

### 3. Les Deux-Points (`:`) : Le Portier du Code
Oublier le `:` après un `if`, `while`, `for`, `def` ou `class` est l'erreur la plus fréquente en examen.
- **Réflexe** : Dès que vous ouvrez une structure, le portier `:` doit être là.

### 4. `Return` vs `Print` : L'Analogie du Haut-Parleur et de l'Enveloppe
- **`Print()` (Le Haut-Parleur)** : Crie la valeur au monde (l'écran). La valeur est perdue pour le reste du programme.
- **`Return` (L'Enveloppe)** : Transmet discrètement la valeur à une autre partie du programme. On peut alors la stocker dans une variable.

---

## PARTIE 2 : CONCEPTS DÉTAILLÉS & ANALYSES PROFONDES

### 1. Algorithmique : Pseudo-Code vs Flowcharts
Le cours exige une distinction nette :
- **Variables** : Toujours déclarées avec leur type (`Variable x en Entier`).
- **Tableaux (Algo)** : Indiqués par `Tableau Tab[N] en Entier`.
- **Lecture/Écriture** : Utilisez `Lire` et `Écrire` (ou `Afficher`).
*Conseil d'expert : En examen, si le pseudo-code n'est pas indenté, vous perdez des points de structure.*

### 2. Les Tableaux (Algo) vs Les Listes (Python)
Bien que similaires, ils diffèrent dans la rigueur :
- **Tableau** : Taille souvent fixe, type homogène.
- **Liste** : Dynamique, peut contenir n'importe quoi.
- **Indexation** : Commence TOUJOURS à **0**. Le dernier élément est à `taille - 1`.

### 3. La POO : Le Modèle "A PIE"
Le plan de cours met l'accent sur l'approche orientée objet. Retenez ces 4 piliers :
- **A**bstraction : Cacher la complexité (on appuie sur un bouton, on ne regarde pas les fils).
- **P**olymorphisme : Une même action (`calculer_paie()`) peut avoir des résultats différents selon l'objet (Vendeur vs Développeur).
- **I**nhéritage : Une classe "Enfant" reçoit les gènes de sa classe "Parent" (`super().__init__()`).
- **E**ncapsulation : Protéger les données à l'intérieur de l'objet (attributs privés).

### 4. L'IA dans la Programmation : Allié, pas Remplaçant
Le cours intègre l'IA générative. Voici comment l'utiliser professionnellement :
- **Spécification technique** : Un bon prompt est un cahier des charges précis. Si l'IA se trompe, c'est que votre logique (prompt) est floue.
- **Revue de code** : Demandez à l'IA d'expliquer l'erreur, pas juste de donner le code. Cela développe votre "littératie d'erreur".

---

## PARTIE 3 : MNÉMOTECHNIQUES DE SURVIE

1. **B.I.F. (Boucle / Indice / Fin)** : Pour ne jamais rater un parcours de tableau.
   - `B` : Où commence ma boucle ?
   - `I` : Quel est mon indice (ex: `i`) ?
   - `F` : Où s'arrête-t-elle (`len(tab)`) ?

2. **C.O.H.P. (Classe / Objet / Héritage / Polymorphisme)** : Les piliers de la POO.

3. **V.A.L.E.U.R.** (Révisé) :
   - **V**ariable nommée clairement.
   - **A**ffectation correcte.
   - **L**ecture du type (`int`/`float`).
   - **E**st-ce que j'ai bien mis les `:` ?
   - **U**ne indentation parfaite.
   - **R**ésultat affiché ou retourné.

---
*Ce document a été conçu en analysant les critères d'évaluation du collège Bois de Boulogne (LEA.1U).*
