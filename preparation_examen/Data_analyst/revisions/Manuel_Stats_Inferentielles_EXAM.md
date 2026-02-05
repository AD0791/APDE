# MANUEL STATISTIQUES INFÉRENTIELLES - VERSION EXAMEN ÉCRIT
## Data Analyst DPO - UniBank Haiti
### Format optimisé pour révision et examen manuscrit

---

## TABLE DES MATIÈRES

1. [Concepts Fondamentaux](#1-concepts-fondamentaux)
2. [Échantillonnage](#2-échantillonnage)
3. [Intervalles de Confiance](#3-intervalles-de-confiance)
4. [Tests d'Hypothèses - Vue d'Ensemble](#4-tests-dhypothèses---vue-densemble)
5. [Test t de Student](#5-test-t-de-student)
6. [Test Z pour Proportions](#6-test-z-pour-proportions)
7. [Test du Chi-Carré](#7-test-du-chi-carré)
8. [ANOVA](#8-anova)
9. [Tests Non-Paramétriques](#9-tests-non-paramétriques)
10. [Arbres de Décision](#10-arbres-de-décision)

---

## 1. CONCEPTS FONDAMENTAUX

### 1.1 Population vs Échantillon

#### Définitions
- **Population (N)**: Ensemble COMPLET de tous les éléments étudiés
- **Échantillon (n)**: Sous-ensemble REPRÉSENTATIF de la population

#### Exemple Bancaire DPO
```
Population: Tous les clients UniBank (500,000)
Échantillon: 1,000 clients sélectionnés pour enquête satisfaction
```

#### Paramètres vs Statistiques

| Mesure | Population | Échantillon | Symbole |
|--------|-----------|-------------|---------|
| Moyenne | μ (mu) | x̄ (x-bar) | Formule: Σx/n |
| Écart-type | σ (sigma) | s | √[Σ(x-μ)²/n] |
| Proportion | p | p̂ (p-hat) | Succès/Total |

**Principe clé:** On calcule des **statistiques** sur l'**échantillon** pour ESTIMER les **paramètres** de la **population**.

---

### 1.2 Pourquoi Échantillonner?

#### Raisons Pratiques
1. **Coût**: Étudier 500K clients coûterait des millions
2. **Temps**: Analyse complète prendrait des années
3. **Destructif**: Certains tests détruisent l'objet (audit approfondi)
4. **Impossibilité**: Population infinie ou inaccessible

#### Exemple DPO UniBank
Au lieu d'auditer TOUS les dossiers de crédit (50,000), on en sélectionne 500 de manière aléatoire pour détecter les non-conformités RGPD.

---

### 1.3 Théorème Central Limite (TCL)

#### Énoncé
> Pour n ≥ 30, la distribution des moyennes d'échantillons tend vers une **distribution normale**, QUELLE QUE SOIT la distribution de la population.

#### Formule
```
Moyenne des échantillons: μx̄ = μ
Erreur standard: σx̄ = σ / √n
```

#### Implications Pratiques
1. Plus n augmente → Plus l'estimation est précise
2. Doubler la précision → Multiplier n par 4
3. Permet d'utiliser la loi normale pour l'inférence

#### Graphique Mental
```
Population        Échantillons (n=100)     Distribution des moyennes
(asymétrique) →   Tirer 1000 fois    →    (NORMALE!)
    ___                                          /\
   /  |                                         /  \
  /   |__                                     /    \
```

---

## 2. ÉCHANTILLONNAGE

### 2.1 Types d'Échantillonnage

#### Échantillonnage Probabiliste (Recommandé)

| Méthode | Description | Quand utiliser | Exemple DPO |
|---------|-------------|----------------|-------------|
| **Aléatoire Simple** | Chaque individu a même probabilité | Population homogène | Tirer 100 clients au hasard |
| **Stratifié** | Diviser en groupes, puis échantillonner | Population hétérogène | 50 clients par agence |
| **Par Grappes** | Sélectionner des groupes entiers | Réduire coûts géographiques | Sélectionner 5 agences complètes |
| **Systématique** | Sélection à intervalle régulier | Liste ordonnée disponible | Chaque 50ème transaction |

#### Échantillonnage Non-Probabiliste (À éviter)
- **Convenance**: Prendre ce qui est facile (BIAIS!)
- **Quota**: Remplir des quotas arbitraires
- **Jugement**: Expert choisit (SUBJECTIF!)

### 2.2 Taille d'Échantillon

#### Formule Générale (Proportion)
```
n = Z² × p(1-p) / E²

Où:
- Z = Score Z pour niveau de confiance (1.96 pour 95%)
- p = Proportion estimée (0.5 si inconnue)
- E = Marge d'erreur désirée
```

#### Exemple Calculé
**Objectif**: Estimer le taux de défaut avec marge d'erreur ±3% et 95% de confiance

```
n = (1.96)² × 0.5(1-0.5) / (0.03)²
n = 3.84 × 0.25 / 0.0009
n = 1067 clients minimum
```

#### Règle Pratique
- **n ≥ 30**: Minimum absolu pour TCL
- **n ≥ 100**: Bon pour estimations
- **n ≥ 1000**: Excellent pour précision fine

---

## 3. INTERVALLES DE CONFIANCE

### 3.1 Définition

**Intervalle de Confiance (IC)**: Plage de valeurs où se trouve le VRAI paramètre avec un certain niveau de confiance.

#### Interprétation CORRECTE
"On est confiant à 95% que le VRAI taux de défaut se situe entre 4% et 6%"

#### Interprétation INCORRECTE (Ne JAMAIS dire)
❌ "Il y a 95% de chances que le taux soit entre 4% et 6%"  
Le paramètre est FIXE, c'est notre ESTIMATION qui varie!

### 3.2 Formules par Type

#### IC pour une Moyenne (n ≥ 30)
```
IC = x̄ ± Z × (s / √n)

Où:
- x̄ = Moyenne échantillon
- Z = 1.96 (pour 95%), 1.645 (pour 90%), 2.576 (pour 99%)
- s = Écart-type échantillon
- n = Taille échantillon
```

#### IC pour une Moyenne (n < 30)
```
IC = x̄ ± t × (s / √n)

Utiliser table t de Student avec (n-1) degrés de liberté
```

#### IC pour une Proportion
```
IC = p̂ ± Z × √[p̂(1-p̂)/n]

Où p̂ = proportion observée (x/n)
```

### 3.3 Exemple Bancaire Complet

#### Contexte
DPO veut estimer le solde moyen des comptes épargne

**Données échantillon (n=100)**:
- Moyenne: 25,000 HTG
- Écart-type: 8,000 HTG

#### Calcul IC 95%
```
IC = 25,000 ± 1.96 × (8,000 / √100)
IC = 25,000 ± 1.96 × 800
IC = 25,000 ± 1,568
IC = [23,432 HTG ; 26,568 HTG]
```

#### Interprétation
"Nous sommes confiants à 95% que le solde moyen de TOUS les comptes épargne se situe entre 23,432 HTG et 26,568 HTG"

---

## 4. TESTS D'HYPOTHÈSES - VUE D'ENSEMBLE

### 4.1 Principe Général

#### Les 2 Hypothèses
```
H₀ (Hypothèse Nulle): Pas d'effet, pas de différence
H₁ (Hypothèse Alternative): Il y a un effet ou une différence
```

#### Exemple Banking
```
H₀: Le taux de défaut = 5% (pas de changement)
H₁: Le taux de défaut ≠ 5% (il y a changement)
```

### 4.2 Les 6 Étapes OBLIGATOIRES

```
1. FORMULER H₀ et H₁ clairement
2. CHOISIR α (risque Type I) = 0.05 généralement
3. SÉLECTIONNER le test approprié
4. CALCULER la statistique de test
5. TROUVER la p-value
6. DÉCIDER: Si p < α → Rejeter H₀, sinon Garder H₀
```

### 4.3 Types de Tests

| Test | H₁ | Quand utiliser | Exemple |
|------|-----|----------------|---------|
| **Bilatéral** | μ ≠ μ₀ | Différence dans N'IMPORTE QUELLE direction | "Le taux a-t-il CHANGÉ?" |
| **Unilatéral >** | μ > μ₀ | Augmentation attendue | "Le taux a-t-il AUGMENTÉ?" |
| **Unilatéral <** | μ < μ₀ | Diminution attendue | "Le taux a-t-il DIMINUÉ?" |

### 4.4 Les 2 Types d'Erreurs

| Décision | H₀ Vraie | H₀ Fausse |
|----------|----------|-----------|
| **Rejeter H₀** | ❌ **Erreur Type I** (α) | ✅ Correct |
| **Garder H₀** | ✅ Correct | ❌ **Erreur Type II** (β) |

#### Expliqué simplement
- **Erreur Type I** (α = 5%): Faux positif - On crie au loup alors qu'il n'y en a pas
- **Erreur Type II** (β): Faux négatif - On ne voit pas le loup alors qu'il est là
- **Puissance** (1-β): Probabilité de détecter le loup quand il est là

#### Contexte Banking
```
Erreur Type I: Déclarer qu'un client est à risque alors qu'il est sain
Erreur Type II: Ne pas détecter un client réellement à risque
```

### 4.5 La p-value Expliquée

#### Définition
> **p-value**: Probabilité d'observer un résultat AUSSI EXTRÊME que celui obtenu, SI H₀ est vraie.

#### Règle de Décision
```
p-value ≤ α (0.05) → Rejeter H₀ (Résultat SIGNIFICATIF)
p-value > α → Garder H₀ (Pas assez de preuves)
```

#### Interprétation par Valeur
```
p > 0.10: Aucune preuve contre H₀
0.05 < p ≤ 0.10: Preuve faible
0.01 < p ≤ 0.05: Preuve modérée
p ≤ 0.01: Preuve forte contre H₀
```

#### ⚠️ ATTENTION: Pièges de la p-value
1. p faible ≠ Effet important (peut être significatif mais négligeable)
2. p élevé ≠ H₀ est vraie (juste pas assez de preuves)
3. Significativité statistique ≠ Significativité pratique

---

## 5. TEST t DE STUDENT

### 5.1 Test t pour UN Échantillon

#### Définition
Compare la moyenne d'UN échantillon à une valeur de référence

#### Quand l'utiliser
- Comparer moyenne échantillon vs valeur fixe
- Données continues
- Distribution normale OU n ≥ 30
- Écart-type population INCONNU

#### Hypothèses
```
H₀: μ = μ₀
H₁: μ ≠ μ₀  (ou > ou <)
```

#### Formule
```
t = (x̄ - μ₀) / (s / √n)

Où:
- x̄ = Moyenne échantillon
- μ₀ = Valeur de référence
- s = Écart-type échantillon
- n = Taille échantillon

Degrés de liberté: df = n - 1
```

#### Exemple Banking Complet

**Contexte DPO**:  
Le solde moyen des comptes Premium devrait être 50,000 HTG. On vérifie sur un échantillon.

**Données (n=40)**:
- Moyenne observée: 52,500 HTG
- Écart-type: 12,000 HTG

**Étape 1**: Hypothèses
```
H₀: μ = 50,000 HTG
H₁: μ ≠ 50,000 HTG (bilatéral)
α = 0.05
```

**Étape 2**: Calcul
```
t = (52,500 - 50,000) / (12,000 / √40)
t = 2,500 / (12,000 / 6.32)
t = 2,500 / 1,898
t = 1.32
```

**Étape 3**: Décision
```
df = 40 - 1 = 39
Valeur critique t(0.025, 39) ≈ 2.02
|t| = 1.32 < 2.02 → Ne pas rejeter H₀
```

**Conclusion**: Le solde moyen ne diffère PAS significativement de 50,000 HTG au seuil de 5%.

#### Conditions d'Application
✅ Variable continue  
✅ Échantillon aléatoire  
✅ Distribution approximativement normale (ou n ≥ 30)  
✅ Observations indépendantes

---

### 5.2 Test t pour DEUX Échantillons Indépendants

#### Définition
Compare les moyennes de DEUX groupes distincts

#### Quand l'utiliser
- Comparer 2 moyennes
- Groupes indépendants (ex: Hommes vs Femmes)
- Données continues et normales

#### Hypothèses
```
H₀: μ₁ = μ₂  (les moyennes sont égales)
H₁: μ₁ ≠ μ₂  (les moyennes diffèrent)
```

#### Formule (variances égales)
```
t = (x̄₁ - x̄₂) / √[s²pooled × (1/n₁ + 1/n₂)]

s²pooled = [(n₁-1)s₁² + (n₂-1)s₂²] / (n₁ + n₂ - 2)

df = n₁ + n₂ - 2
```

#### Exemple Banking

**Contexte**: Comparer soldes moyens Premium vs Standard

**Données**:
- Premium (n₁=50): x̄₁ = 45,000 HTG, s₁ = 10,000 HTG
- Standard (n₂=50): x̄₂ = 15,000 HTG, s₂ = 8,000 HTG

**Étape 1**: Hypothèses
```
H₀: μ_Premium = μ_Standard
H₁: μ_Premium ≠ μ_Standard
α = 0.05
```

**Étape 2**: Variance poolée
```
s²pooled = [(49×10,000²) + (49×8,000²)] / 98
s²pooled = [4.9B + 3.1B] / 98
s²pooled = 81,632,653
s_pooled = 9,035 HTG
```

**Étape 3**: Calcul t
```
t = (45,000 - 15,000) / √[81,632,653 × (1/50 + 1/50)]
t = 30,000 / (9,035 × 0.2)
t = 30,000 / 1,807
t = 16.60
```

**Étape 4**: Décision
```
df = 98
Valeur critique ≈ 1.98
|t| = 16.60 >> 1.98 → Rejeter H₀ fortement!
```

**Conclusion**: Les soldes moyens diffèrent SIGNIFICATIVEMENT entre Premium et Standard (p < 0.001).

#### Test de Welch (variances inégales)
Si test de Levene montre variances différentes → Utiliser formule de Welch (pas poolée)

---

### 5.3 Test t pour Échantillons APPARIÉS

#### Définition
Compare DEUX mesures sur les MÊMES individus (avant/après)

#### Quand l'utiliser
- Mesures avant/après
- Mesures répétées
- Paires appariées (jumeaux, etc.)

#### Principe
On calcule les DIFFÉRENCES pour chaque sujet, puis test t sur ces différences.

#### Hypothèses
```
H₀: μ_diff = 0  (pas de changement)
H₁: μ_diff ≠ 0  (il y a changement)
```

#### Formule
```
t = d̄ / (s_d / √n)

Où:
- d̄ = Moyenne des différences
- s_d = Écart-type des différences
- n = Nombre de paires
```

#### Exemple Banking

**Contexte**: Formation agents - Ventes avant vs après

**Données (n=25 agents)**:
- Moyenne différence (après - avant): +5 ventes
- Écart-type des différences: 8 ventes

**Étape 1**: Hypothèses
```
H₀: La formation n'a pas d'effet (μ_diff = 0)
H₁: La formation a un effet (μ_diff ≠ 0)
α = 0.05
```

**Étape 2**: Calcul
```
t = 5 / (8 / √25)
t = 5 / (8 / 5)
t = 5 / 1.6
t = 3.13
```

**Étape 3**: Décision
```
df = 25 - 1 = 24
Valeur critique t(0.025, 24) ≈ 2.06
|t| = 3.13 > 2.06 → Rejeter H₀
```

**Conclusion**: La formation a SIGNIFICATIVEMENT augmenté les ventes (p < 0.05).

---

## 6. TEST Z POUR PROPORTIONS

### 6.1 Test Z pour UNE Proportion

#### Définition
Compare une proportion observée à une valeur de référence

#### Quand l'utiliser
- Variable binaire (Succès/Échec)
- Grand échantillon (np ≥ 5 ET n(1-p) ≥ 5)
- Comparer taux observé vs taux théorique

#### Hypothèses
```
H₀: p = p₀
H₁: p ≠ p₀  (ou > ou <)
```

#### Formule
```
Z = (p̂ - p₀) / √[p₀(1-p₀)/n]

Où:
- p̂ = Proportion observée (x/n)
- p₀ = Proportion de référence
- n = Taille échantillon
```

#### Exemple Banking

**Contexte**: Le taux de défaut devrait être 5%. On vérifie.

**Données**:
- Échantillon: n = 1000 prêts
- Défauts observés: 60
- p̂ = 60/1000 = 0.06 (6%)

**Étape 1**: Hypothèses
```
H₀: p = 0.05 (taux normal)
H₁: p > 0.05 (taux anormalement élevé)
α = 0.05 (unilatéral)
```

**Étape 2**: Vérification conditions
```
np₀ = 1000 × 0.05 = 50 ≥ 5 ✓
n(1-p₀) = 1000 × 0.95 = 950 ≥ 5 ✓
```

**Étape 3**: Calcul
```
Z = (0.06 - 0.05) / √[0.05×0.95/1000]
Z = 0.01 / √(0.0000475)
Z = 0.01 / 0.00689
Z = 1.45
```

**Étape 4**: Décision
```
Valeur critique Z(0.05) = 1.645
Z = 1.45 < 1.645 → Ne pas rejeter H₀
```

**Conclusion**: Le taux de défaut ne diffère PAS significativement de 5%.

---

### 6.2 Test Z pour DEUX Proportions

#### Définition
Compare les proportions de DEUX groupes indépendants

#### Quand l'utiliser
- Comparer taux entre 2 groupes
- Variables binaires
- Grands échantillons

#### Hypothèses
```
H₀: p₁ = p₂
H₁: p₁ ≠ p₂
```

#### Formule
```
Z = (p̂₁ - p̂₂) / √[p̂(1-p̂) × (1/n₁ + 1/n₂)]

Où p̂ = (x₁ + x₂) / (n₁ + n₂)  (proportion poolée)
```

#### Exemple Banking

**Contexte**: Comparer taux de conversion entre 2 campagnes

**Données**:
- Campagne A: 120 conversions sur 1000 clients (12%)
- Campagne B: 150 conversions sur 1000 clients (15%)

**Étape 1**: Hypothèses
```
H₀: p_A = p_B
H₁: p_A ≠ p_B
α = 0.05
```

**Étape 2**: Proportion poolée
```
p̂ = (120 + 150) / (1000 + 1000) = 270/2000 = 0.135
```

**Étape 3**: Calcul
```
Z = (0.12 - 0.15) / √[0.135×0.865 × (1/1000 + 1/1000)]
Z = -0.03 / √[0.1168 × 0.002]
Z = -0.03 / 0.0153
Z = -1.96
```

**Étape 4**: Décision
```
Valeur critique = ±1.96
|Z| = 1.96 → Juste à la limite! p ≈ 0.05
```

**Conclusion**: La différence est JUSTE significative au seuil de 5%. Campagne B performe mieux.

---

## 7. TEST DU CHI-CARRÉ (χ²)

### 7.1 Test d'Indépendance

#### Définition
Teste si DEUX variables catégorielles sont indépendantes

#### Quand l'utiliser
- 2 variables catégorielles
- Tableau de contingence
- Effectifs attendus ≥ 5 dans chaque cellule

#### Hypothèses
```
H₀: Les variables sont indépendantes
H₁: Les variables sont dépendantes (liées)
```

#### Formule
```
χ² = Σ [(O - E)² / E]

Où:
- O = Fréquence Observée
- E = Fréquence Attendue = (Total ligne × Total colonne) / Total général

df = (nombre lignes - 1) × (nombre colonnes - 1)
```

#### Exemple Banking

**Contexte**: Le canal préféré dépend-il du segment client?

**Tableau Observé**:
|          | Agence | Mobile | Web | Total |
|----------|--------|--------|-----|-------|
| Premium  | 60     | 30     | 10  | 100   |
| Standard | 40     | 50     | 110 | 200   |
| **Total**| 100    | 80     | 120 | 300   |

**Étape 1**: Hypothèses
```
H₀: Canal indépendant du segment
H₁: Canal dépend du segment
α = 0.05
```

**Étape 2**: Calcul des Attendus
```
E(Premium, Agence) = (100 × 100) / 300 = 33.33
E(Premium, Mobile) = (100 × 80) / 300 = 26.67
E(Premium, Web) = (100 × 120) / 300 = 40.00
... (faire pour chaque cellule)
```

**Étape 3**: Calcul χ²
```
χ² = (60-33.33)²/33.33 + (30-26.67)²/26.67 + (10-40)²/40 + ...
χ² = 21.33 + 0.42 + 22.50 + ...
χ² ≈ 65.25
```

**Étape 4**: Décision
```
df = (2-1) × (3-1) = 2
Valeur critique χ²(0.05, 2) = 5.99
χ² = 65.25 >> 5.99 → Rejeter H₀ FORTEMENT
```

**Conclusion**: Le canal préféré DÉPEND SIGNIFICATIVEMENT du segment (p < 0.001).

#### Interprétation Business
Les clients Premium préfèrent l'agence, les Standard préfèrent le Web.

---

### 7.2 Test d'Ajustement (Goodness of Fit)

#### Définition
Teste si les données suivent une distribution théorique

#### Quand l'utiliser
- Vérifier uniformité
- Comparer distribution observée vs attendue
- Une seule variable catégorielle

#### Hypothèses
```
H₀: Les données suivent la distribution théorique
H₁: Les données ne suivent pas la distribution
```

#### Exemple Banking

**Contexte**: Les transactions sont-elles uniformes par jour de semaine?

**Données**:
| Jour | Observé | Attendu (uniforme) |
|------|---------|-------------------|
| Lun  | 180     | 700/7 = 100       |
| Mar  | 120     | 100               |
| Mer  | 90      | 100               |
| Jeu  | 85      | 100               |
| Ven  | 150     | 100               |
| Sam  | 50      | 100               |
| Dim  | 25      | 100               |

**Étape 1**: Calcul χ²
```
χ² = (180-100)²/100 + (120-100)²/100 + ... + (25-100)²/100
χ² = 64 + 4 + 1 + 2.25 + 25 + 25 + 56.25
χ² = 177.5
```

**Étape 2**: Décision
```
df = 7 - 1 = 6
Valeur critique χ²(0.05, 6) = 12.59
χ² = 177.5 >> 12.59 → Rejeter H₀
```

**Conclusion**: Les transactions NE SONT PAS uniformes. Il y a clairement plus d'activité en début de semaine.

---

## 8. ANOVA (Analysis of Variance)

### 8.1 ANOVA à UN Facteur

#### Définition
Compare les moyennes de 3 GROUPES OU PLUS

#### Quand l'utiliser
- Comparer 3+ moyennes
- Variable continue
- Groupes indépendants
- Distribution normale dans chaque groupe
- Variances homogènes

#### Hypothèses
```
H₀: μ₁ = μ₂ = μ₃ = ... = μₖ  (toutes les moyennes égales)
H₁: Au moins UNE moyenne diffère
```

#### Principe
ANOVA compare la variation ENTRE groupes vs variation À L'INTÉRIEUR des groupes.

```
F = Variance ENTRE / Variance INTRA

Si F grand → Les groupes diffèrent significativement
```

#### Formule
```
F = MSB / MSW

Où:
MSB = SSB / (k-1)  (Moyenne des carrés ENTRE)
MSW = SSW / (N-k)  (Moyenne des carrés À L'INTÉRIEUR)

df1 = k - 1  (nombre groupes - 1)
df2 = N - k  (total - nombre groupes)
```

#### Exemple Banking

**Contexte**: Les soldes moyens diffèrent-ils entre les 4 agences?

**Données**:
- Agence Nord (n=30): x̄ = 20,000 HTG
- Agence Sud (n=30): x̄ = 25,000 HTG
- Agence Est (n=30): x̄ = 22,000 HTG
- Agence Ouest (n=30): x̄ = 28,000 HTG

**Étape 1**: Hypothèses
```
H₀: Les 4 agences ont le même solde moyen
H₁: Au moins une agence diffère
α = 0.05
```

**Étape 2**: Calcul ANOVA
(Calculs simplifiés)
```
Supposons F = 12.45
df1 = 4 - 1 = 3
df2 = 120 - 4 = 116
```

**Étape 3**: Décision
```
Valeur critique F(0.05, 3, 116) ≈ 2.68
F = 12.45 > 2.68 → Rejeter H₀
```

**Conclusion**: Les soldes moyens diffèrent SIGNIFICATIVEMENT entre agences.

---

### 8.2 Tests Post-Hoc (Après ANOVA)

#### Problème
ANOVA dit "au moins une différence" mais ne dit PAS laquelle!

#### Solution: Tests Post-Hoc

| Test | Usage | Avantage |
|------|-------|----------|
| **Tukey HSD** | Toutes comparaisons | Contrôle erreur familiale |
| **Bonferroni** | Peu de comparaisons | Très conservateur |
| **Scheffé** | Comparaisons complexes | Flexible |

#### Procédure Tukey HSD

**Formule**:
```
HSD = q × √(MSW / n)

Où q = valeur de Tukey (table)
```

**Exemple**: Comparer Agence Nord vs Sud
```
Différence = |20,000 - 25,000| = 5,000 HTG
HSD = 3.70 × √(25,000,000 / 30) = 3,377 HTG

5,000 > 3,377 → Différence significative!
```

---

## 9. TESTS NON-PARAMÉTRIQUES

### 9.1 Quand Utiliser les Tests Non-Paramétriques?

#### Situations
1. **Distribution non normale** (asymétrique, bimodale)
2. **Petit échantillon** (n < 30)
3. **Données ordinales** (ranking, échelles)
4. **Outliers importants**
5. **Variances très inégales**

#### Avantages
- Moins d'hypothèses
- Robustes aux outliers
- Applicables aux données ordinales

#### Inconvénients
- Moins de puissance statistique
- Moins sensibles aux petits effets

---

### 9.2 Correspondance Tests Paramétriques ↔ Non-Paramétriques

| Paramétrique | Non-Paramétrique | Usage |
|--------------|------------------|-------|
| Test t (1 échantillon) | **Wilcoxon signé-rang** | 1 médiane vs valeur |
| Test t (2 échantillons indép.) | **Mann-Whitney U** | Comparer 2 médianes |
| Test t (appariés) | **Wilcoxon signé-rang** | Avant/après |
| ANOVA | **Kruskal-Wallis** | Comparer 3+ médianes |
| Corrélation Pearson | **Spearman** | Corrélation ordinale |

---

### 9.3 Test de Mann-Whitney U

#### Définition
Teste si DEUX groupes indépendants ont la même distribution

#### Hypothèses
```
H₀: Les distributions sont identiques
H₁: Une distribution est décalée par rapport à l'autre
```

#### Principe
1. Combiner les données des 2 groupes
2. Attribuer des rangs
3. Comparer sommes des rangs

#### Exemple Banking

**Contexte**: Satisfaction clients Premium vs Standard

**Données** (échelle 1-5):
- Premium: 5, 4, 5, 4, 3
- Standard: 3, 2, 3, 2, 1

**Étape 1**: Ranger TOUTES les valeurs
```
1(S), 2(S), 2(S), 3(P), 3(S), 3(S), 4(P), 4(P), 5(P), 5(P)
Rangs: 1, 2.5, 2.5, 5, 5, 5, 7.5, 7.5, 9.5, 9.5
```

**Étape 2**: Somme des rangs
```
Premium: 5 + 7.5 + 7.5 + 9.5 + 9.5 = 39
Standard: 1 + 2.5 + 2.5 + 5 + 5 = 16
```

**Étape 3**: Calcul U
```
U₁ = n₁n₂ + n₁(n₁+1)/2 - R₁
U₁ = 5×5 + 5×6/2 - 39 = 25 + 15 - 39 = 1

U₂ = n₁n₂ - U₁ = 25 - 1 = 24
U = min(U₁, U₂) = 1
```

**Étape 4**: Décision
```
Valeur critique U(0.05, 5, 5) = 2
U = 1 < 2 → Rejeter H₀
```

**Conclusion**: Premium a une satisfaction SIGNIFICATIVEMENT supérieure.

---

### 9.4 Test de Kruskal-Wallis

#### Définition
Version non-paramétrique de l'ANOVA (3+ groupes)

#### Quand l'utiliser
- Comparer 3+ groupes
- Distribution non normale
- Données ordinales

#### Hypothèses
```
H₀: Toutes les distributions sont identiques
H₁: Au moins une distribution diffère
```

#### Formule
```
H = [12 / N(N+1)] × Σ[R²ᵢ/nᵢ] - 3(N+1)

Où:
- N = Total observations
- Rᵢ = Somme des rangs groupe i
- nᵢ = Taille groupe i

Suit approximativement χ² avec df = k-1
```

#### Exemple Banking

**Contexte**: Comparer scores satisfaction 3 agences

**Données rangées**:
- Agence A: Somme rangs = 150, n = 10
- Agence B: Somme rangs = 200, n = 10
- Agence C: Somme rangs = 115, n = 10

**Calcul**:
```
H = [12 / 30×31] × [(150²/10) + (200²/10) + (115²/10)] - 3×31
H ≈ 6.45
```

**Décision**:
```
χ²(0.05, 2) = 5.99
H = 6.45 > 5.99 → Rejeter H₀
```

**Conclusion**: Les distributions de satisfaction diffèrent entre agences.

---

### 9.5 Corrélation de Spearman

#### Définition
Mesure la force d'une relation MONOTONE entre 2 variables

#### Différence avec Pearson
- **Pearson (r)**: Relation LINÉAIRE, données normales
- **Spearman (ρ)**: Relation MONOTONE, basée sur RANGS

#### Quand utiliser
- Données ordinales
- Relation non linéaire mais monotone
- Présence d'outliers
- Distribution non normale

#### Formule
```
ρ = 1 - [6Σd²ᵢ / n(n²-1)]

Où dᵢ = différence de rangs pour chaque observation
```

#### Interprétation (identique à Pearson)
```
|ρ| < 0.3: Corrélation faible
0.3 ≤ |ρ| ≤ 0.7: Corrélation modérée
|ρ| > 0.7: Corrélation forte
```

#### Exemple Banking

**Contexte**: Relation entre score crédit et montant prêt accordé

**Données**:
| Client | Score | Montant | Rang Score | Rang Montant | d | d² |
|--------|-------|---------|------------|--------------|---|-----|
| 1      | 750   | 50K     | 5          | 5            | 0 | 0   |
| 2      | 650   | 30K     | 3          | 3            | 0 | 0   |
| 3      | 800   | 60K     | 6          | 6            | 0 | 0   |
| 4      | 600   | 20K     | 2          | 2            | 0 | 0   |
| 5      | 550   | 15K     | 1          | 1            | 0 | 0   |
| 6      | 700   | 40K     | 4          | 4            | 0 | 0   |

**Calcul**:
```
Σd² = 0
ρ = 1 - [6×0 / 6(36-1)] = 1 - 0 = 1.0
```

**Conclusion**: Corrélation PARFAITE positive → Plus le score est élevé, plus le montant accordé est important.

---

## 10. ARBRES DE DÉCISION

### 10.1 Arbre Global: Quel Test Choisir?

```
┌─────────────────────────────────┐
│ QUELLE EST VOTRE QUESTION?      │
└─────────────────────────────────┘
              │
    ┌─────────┴─────────┐
    │                   │
COMPARER            TESTER
GROUPES             ASSOCIATION
    │                   │
    ▼                   ▼
┌─────────┐      ┌──────────────┐
│ Combien │      │ 2 Variables  │
│ groupes?│      │ Catégorielles│
└─────────┘      └──────────────┘
    │                   │
    ├─ 1 groupe ──────► Test t (1 échantillon)
    │                   ou Wilcoxon
    │
    ├─ 2 groupes ─────┐
    │                 │
    │            ┌────┴────┐
    │            │ Type?   │
    │            └────┬────┘
    │                 │
    │         ┌───────┴───────┐
    │         │               │
    │    Indépendants    Appariés
    │         │               │
    │     t-test ind.     t-test app.
    │     Mann-Whitney    Wilcoxon
    │
    └─ 3+ groupes ────► ANOVA
                        Kruskal-Wallis

ASSOCIATION
    │
    ▼
┌────────────────┐
│ Type variables?│
└────────────────┘
    │
    ├─ 2 Catégorielles ──► Chi-carré
    │
    ├─ 2 Continues ──────► Pearson / Spearman
    │
    └─ Continues + Catégorielle ──► Régression / ANOVA
```

---

### 10.2 Arbre: Test Paramétrique ou Non-Paramétrique?

```
┌─────────────────────────┐
│ Données Normales?       │
└─────────────────────────┘
         │
    ┌────┴────┐
    │         │
   OUI       NON ──────────► Tests NON-PARAMÉTRIQUES
    │                       (Mann-Whitney, Wilcoxon,
    │                        Kruskal-Wallis, Spearman)
    ▼
┌─────────────────┐
│ n ≥ 30?         │
└─────────────────┘
    │
    ├─ OUI ──► Tests PARAMÉTRIQUES
    │           (t-test, ANOVA, Pearson)
    │
    └─ NON ──┐
             │
      ┌──────┴──────┐
      │ Outliers    │
      │ importants? │
      └──────┬──────┘
             │
        ┌────┴────┐
        │         │
       OUI       NON
        │         │
   NON-PARAM.  PARAMÉTRIQUE
              (avec précaution)
```

---

### 10.3 Arbre: Comparer 2 Moyennes

```
┌────────────────────────────┐
│ Comparer 2 MOYENNES        │
└────────────────────────────┘
              │
    ┌─────────┴─────────┐
    │                   │
Indépendants       Appariés
    │                   │
    ▼                   ▼
┌─────────┐      ┌──────────┐
│ Normal? │      │ Normal?  │
└─────────┘      └──────────┘
    │                   │
┌───┴───┐           ┌───┴───┐
│       │           │       │
OUI    NON         OUI    NON
│       │           │       │
▼       ▼           ▼       ▼
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│Variances │  │Mann-     │  │t-test    │  │Wilcoxon  │
│égales?   │  │Whitney U │  │apparié   │  │signed    │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
    │
┌───┴───┐
│       │
OUI    NON
│       │
▼       ▼
t-test  Welch
indép.  t-test
```

---

### 10.4 Arbre: Comparer 3+ Groupes

```
┌─────────────────────────────┐
│ Comparer 3+ GROUPES         │
└─────────────────────────────┘
              │
    ┌─────────┴─────────┐
    │                   │
Distribution         Distribution
Normale              NON Normale
    │                   │
    ▼                   ▼
┌──────────┐      ┌──────────────┐
│Variances │      │ Kruskal-     │
│égales?   │      │ Wallis       │
└──────────┘      └──────────────┘
    │                   │
┌───┴───┐          p < α?
│       │               │
OUI    NON              ▼
│       │         ┌──────────┐
▼       ▼         │ Tests    │
ANOVA   Welch     │ Post-hoc │
        ANOVA     │ (Dunn)   │
    │             └──────────┘
p < α?
    │
    ▼
┌──────────┐
│ Tests    │
│ Post-hoc │
│ (Tukey)  │
└──────────┘
```

---

### 10.5 Arbre: Tests de Proportions

```
┌────────────────────────────┐
│ Tester PROPORTIONS         │
└────────────────────────────┘
              │
    ┌─────────┴─────────┐
    │                   │
1 Proportion      2+ Proportions
    │                   │
    ▼                   ▼
┌──────────┐      ┌──────────────┐
│np ≥ 5 ET │      │ Groupes      │
│n(1-p)≥5? │      │ indépendants?│
└──────────┘      └──────────────┘
    │                   │
    ├─ OUI ──► Test Z   │
    │                   ├─ OUI ──► Test Z (2 prop)
    └─ NON ──► Test     │          ou Chi-carré
              Exact     │
              Binomial  └─ NON ──► McNemar
                                  (appariés)
```

---

### 10.6 Arbre: Tests d'Association

```
┌────────────────────────────┐
│ Tester ASSOCIATION         │
└────────────────────────────┘
              │
    ┌─────────┴─────────┐
    │                   │
2 Catégorielles    2 Continues
    │                   │
    ▼                   ▼
┌──────────┐      ┌──────────┐
│Effectifs │      │ Normal?  │
│attendus  │      └──────────┘
│≥ 5?      │            │
└──────────┘      ┌─────┴─────┐
    │             │           │
┌───┴───┐        OUI         NON
│       │         │           │
OUI    NON        ▼           ▼
│       │    ┌──────────┐  ┌──────────┐
▼       ▼    │Linéaire? │  │Spearman  │
Chi²    Fisher└──────────┘  │(monotone)│
exact         │           └──────────┘
         ┌────┴────┐
         │         │
        OUI       NON
         │         │
         ▼         ▼
    Pearson    Spearman
    (linéaire)
```

---

## 11. SCÉNARIOS BANCAIRES TYPES

### Scénario 1: Audit Conformité RGPD

**Contexte**:  
Le DPO doit vérifier si le taux de non-conformité est acceptable (<5%)

**Question**: Sur 500 dossiers audités, 35 sont non-conformes (7%). Est-ce significativement supérieur à 5%?

**Test à utiliser**: Test Z pour une proportion (unilatéral droit)

**Hypothèses**:
```
H₀: p ≤ 0.05 (taux acceptable)
H₁: p > 0.05 (taux inacceptable)
α = 0.05
```

**Calcul**:
```
p̂ = 35/500 = 0.07
Z = (0.07 - 0.05) / √[0.05×0.95/500]
Z = 0.02 / 0.00975
Z = 2.05

Valeur critique Z(0.05) = 1.645
Z = 2.05 > 1.645 → Rejeter H₀
```

**Décision**: Le taux de non-conformité est SIGNIFICATIVEMENT supérieur à 5% (p = 0.02). Action corrective nécessaire!

**Graphique Mental**:
```
    Taux acceptable     Zone critique
    ────────────│──────────────►
         5%          7%
              ↑
         Taux observé
         (ALERTE!)
```

---

### Scénario 2: Comparaison Performance Agences

**Contexte**:  
Comparer le solde moyen des comptes entre 3 agences

**Données**:
- Nord (n=50): x̄ = 25,000 HTG, s = 10,000
- Sud (n=50): x̄ = 30,000 HTG, s = 12,000
- Est (n=50): x̄ = 28,000 HTG, s = 11,000

**Question**: Les soldes moyens diffèrent-ils?

**Test à utiliser**: ANOVA à un facteur

**Hypothèses**:
```
H₀: μ_Nord = μ_Sud = μ_Est
H₁: Au moins une moyenne diffère
α = 0.05
```

**Résultat (simplifié)**:
```
F = 8.45, p = 0.0003
```

**Décision**: Les agences diffèrent significativement (p < 0.001)

**Post-hoc Tukey**:
```
Nord vs Sud: Différence significative (p = 0.001)
Nord vs Est: Pas de différence (p = 0.12)
Sud vs Est: Pas de différence (p = 0.35)
```

**Conclusion Business**: L'agence Sud a des soldes significativement plus élevés que le Nord. Analyser pourquoi (clientèle plus aisée? meilleurs agents?).

---

### Scénario 3: A/B Test Campagne Email

**Contexte**:  
Tester 2 versions d'email pour promouvoir un nouveau produit

**Données**:
- Version A (n=1000): 120 conversions (12%)
- Version B (n=1000): 150 conversions (15%)

**Question**: Version B est-elle significativement meilleure?

**Test à utiliser**: Test Z pour deux proportions

**Hypothèses**:
```
H₀: p_A = p_B
H₁: p_B > p_A (unilatéral)
α = 0.05
```

**Calcul**:
```
p̂ = (120+150)/2000 = 0.135
Z = (0.15-0.12) / √[0.135×0.865×(1/1000+1/1000)]
Z = 0.03 / 0.0153
Z = 1.96

Valeur critique = 1.645
Z = 1.96 > 1.645 → Rejeter H₀
```

**Décision**: Version B est significativement meilleure (p = 0.025)

**Impact Business**:
```
Lift = (15% - 12%) / 12% × 100% = 25%

Sur 10,000 clients:
- Version A: 1,200 conversions
- Version B: 1,500 conversions
- Gain: +300 clients (soit +25%)
```

**Recommandation**: Déployer la Version B!

---

### Scénario 4: Effet Formation Agents

**Contexte**:  
Vérifier si une formation améliore les ventes des agents

**Données** (n=20 agents):
- Ventes AVANT formation: Moyenne = 15 produits/mois
- Ventes APRÈS formation: Moyenne = 18 produits/mois
- Moyenne des différences: +3 produits
- Écart-type des différences: 5 produits

**Question**: La formation a-t-elle un effet significatif?

**Test à utiliser**: Test t apparié

**Hypothèses**:
```
H₀: μ_diff = 0 (pas d'effet)
H₁: μ_diff > 0 (amélioration)
α = 0.05
```

**Calcul**:
```
t = 3 / (5 / √20)
t = 3 / 1.118
t = 2.68

df = 19
Valeur critique t(0.05, 19) = 1.729
t = 2.68 > 1.729 → Rejeter H₀
```

**Décision**: La formation améliore significativement les ventes (p = 0.007)

**Taille d'effet**:
```
Cohen's d = 3 / 5 = 0.6 (effet MODÉRÉ à FORT)
```

**ROI Formation**:
```
Coût formation: 500 USD/agent
Gain moyen: +3 produits × 50 USD commission = +150 USD/mois
ROI = 150/500 = 30% par mois → Rentable dès le 4ème mois!
```

---

### Scénario 5: Satisfaction Client par Segment

**Contexte**:  
Comparer la satisfaction (échelle 1-5) entre segments

**Données**:
- Premium: 4.5, 5, 4, 5, 4.5 (Médiane = 4.5)
- Standard: 3, 3.5, 3, 4, 3.5 (Médiane = 3.5)

**Question**: Les satisfactions diffèrent-elles?

**Test à utiliser**: Mann-Whitney U (données ordinales)

**Hypothèses**:
```
H₀: Les distributions sont identiques
H₁: Premium > Standard
α = 0.05
```

**Résultat**:
```
U = 2, p = 0.016
```

**Décision**: Premium a une satisfaction significativement supérieure (p = 0.016)

**Action Business**: Analyser ce qui différencie l'expérience Premium pour l'améliorer chez Standard.

---

## 12. PIÈGES FRÉQUENTS À ÉVITER

### Piège 1: Confondre Corrélation et Causalité

❌ **Erreur**: "Il y a corrélation entre ice cream et noyades, donc l'ice cream cause les noyades!"

✅ **Correct**: "Corrélation ne prouve PAS causalité. Variable cachée = température estivale."

---

### Piège 2: Ignorer la Taille d'Effet

❌ **Erreur**: "p = 0.001 donc résultat très important!"

✅ **Correct**: "p < 0.05 = significatif, MAIS effet peut être négligeable. Calculer Cohen's d ou différence pratique."

**Exemple**:
```
Différence significative de 10 HTG sur solde moyen de 100,000 HTG
→ Significatif statistiquement
→ Négligeable pratiquement (0.01%)
```

---

### Piège 3: Multiple Testing (Comparaisons Multiples)

❌ **Erreur**: Faire 20 tests à α=0.05 sans correction → 1 faux positif attendu!

✅ **Correct**: Appliquer correction de Bonferroni: α_ajusté = 0.05/20 = 0.0025

---

### Piège 4: p-Hacking (Chercher la Significativité)

❌ **Erreur**: Tester plein de variables jusqu'à trouver p < 0.05

✅ **Correct**: Définir hypothèses AVANT de voir les données

---

### Piège 5: Échantillon Non Représentatif

❌ **Erreur**: Enquête satisfaction en interrogeant seulement clients en agence

✅ **Correct**: Échantillonnage aléatoire de TOUS les clients (agence + digital)

---

### Piège 6: Interprétation Incorrecte IC

❌ **Erreur**: "Il y a 95% de chances que μ soit dans [23K, 27K]"

✅ **Correct**: "On est confiant à 95% que μ est dans [23K, 27K]"

---

### Piège 7: Utiliser Test Paramétrique sans Vérifier Conditions

❌ **Erreur**: t-test sur données très asymétriques avec n=15

✅ **Correct**: Vérifier normalité (Shapiro-Wilk) OU utiliser Mann-Whitney

---

### Piège 8: Confondre Moyenne et Médiane

❌ **Erreur**: "Solde moyen = 50K donc clients typiques ont 50K"

✅ **Correct**: Si distribution asymétrique → Médiane plus représentative

**Exemple**:
```
Soldes: 5K, 6K, 7K, 8K, 500K
Moyenne = 105K (faussée par outlier)
Médiane = 7K (représentative)
```

---

## 13. FORMULES ESSENTIELLES À MÉMORISER

### Erreur Standard
```
SE = s / √n
```

### Intervalles de Confiance
```
IC 95% (moyenne) = x̄ ± 1.96 × (s/√n)
IC 95% (proportion) = p̂ ± 1.96 × √[p̂(1-p̂)/n]
```

### Taille d'Échantillon (Proportion)
```
n = Z² × p(1-p) / E²

Pour 95% confiance, E=3%, p=0.5:
n = (1.96)² × 0.25 / (0.03)² ≈ 1067
```

### Test t
```
t = (x̄ - μ₀) / (s/√n)
df = n - 1
```

### Test Z (Proportion)
```
Z = (p̂ - p₀) / √[p₀(1-p₀)/n]
```

### Chi-Carré
```
χ² = Σ[(O - E)² / E]
df = (lignes-1) × (colonnes-1)
```

### Corrélation Pearson
```
r = Σ[(x-x̄)(y-ȳ)] / √[Σ(x-x̄)² × Σ(y-ȳ)²]
```

### Cohen's d (Taille d'effet)
```
d = (x̄₁ - x̄₂) / s_pooled

Interprétation:
d < 0.2: Faible
0.2 ≤ d < 0.8: Modéré
d ≥ 0.8: Fort
```

---

## 14. CHECKLIST EXAMEN

### Avant de Répondre
☐ Identifier le TYPE de variables (continue, catégorielle, ordinale)  
☐ Identifier le NOMBRE de groupes à comparer  
☐ Vérifier si données APPARIÉES ou INDÉPENDANTES  
☐ Choisir le TEST approprié (voir arbres de décision)

### Pendant le Test Statistique
☐ Formuler clairement H₀ et H₁  
☐ Choisir α (généralement 0.05)  
☐ Vérifier CONDITIONS d'application  
☐ Calculer CORRECTEMENT la statistique  
☐ Comparer à valeur critique OU interpréter p-value  
☐ Prendre DÉCISION (rejeter ou garder H₀)

### Interprétation Business
☐ Traduire résultat statistique en LANGAGE BUSINESS  
☐ Évaluer TAILLE D'EFFET (pas juste significativité)  
☐ Mentionner LIMITATIONS  
☐ Proposer ACTIONS concrètes

---

## 15. DERNIERS CONSEILS

### Pour l'Examen Écrit

1. **Écrire proprement**: Les formules doivent être LISIBLES
2. **Montrer les étapes**: Même si calcul simple, montrer le raisonnement
3. **Unités**: TOUJOURS inclure les unités (HTG, %, etc.)
4. **Arrondir intelligemment**: 2 décimales pour statistiques, 4 pour p-values
5. **Conclusion en français**: Toujours conclure en langage clair

### Gestion du Temps

- **Lire TOUTES les questions d'abord** (5 min)
- **Commencer par questions faciles** (confiance)
- **Allouer temps proportionnel aux points**
- **Garder 10 min à la fin pour relecture**

### Si Blocage

1. Passer à question suivante
2. Revenir après
3. Écrire ce que vous savez (points partiels!)
4. Justifier vos choix même si incertain

---

**BONNE CHANCE ALEXANDRO! 🚀**

Tu as tout ce qu'il faut pour RÉUSSIR! 💪
