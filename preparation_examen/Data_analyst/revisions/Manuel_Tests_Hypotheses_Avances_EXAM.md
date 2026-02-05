# MANUEL TESTS D'HYPOTHÈSES AVANCÉS - VERSION EXAMEN
## Data Analyst DPO - UniBank Haiti
### Concepts, Décisions, Scénarios Banking

---

## TABLE DES MATIÈRES

1. [Puissance Statistique et Taille d'Effet](#1-puissance-statistique-et-taille-deffet)
2. [Tests Post-Hoc Détaillés](#2-tests-post-hoc-détaillés)
3. [Ajustements pour Comparaisons Multiples](#3-ajustements-pour-comparaisons-multiples)
4. [Tests Exacts](#4-tests-exacts)
5. [Analyse de Survie (Bases)](#5-analyse-de-survie-bases)
6. [Corrélation Partielle](#6-corrélation-partielle)
7. [Régression Logistique Simple](#7-régression-logistique-simple)

---

## 1. PUISSANCE STATISTIQUE ET TAILLE D'EFFET

### 1.1 Les 4 Éléments Interconnectés

```
α (Seuil) ←→ Puissance (1-β)
    ↕             ↕
Taille échantillon (n) ←→ Taille d'effet (δ)
```

#### Relations
- **Augmenter n** → Augmente puissance
- **Augmenter α** → Augmente puissance (mais plus de faux positifs)
- **Effet plus grand** → Augmente puissance
- **Puissance standard**: 80% (0.80)

---

### 1.2 Puissance Statistique (1-β)

#### Définition
> Probabilité de DÉTECTER un vrai effet quand il existe

#### Formule Intuitive
```
Puissance = P(Rejeter H₀ | H₁ vraie)
         = 1 - β (erreur Type II)
```

#### Interprétation par Valeur
```
Puissance < 50%: Très faible (comme lancer pièce)
50-70%: Faible
70-80%: Acceptable
80-90%: Bon
> 90%: Excellent
```

#### Exemple Banking

**Contexte**: Détecter différence de 2% dans taux de défaut

```
Baseline: 5%
Effet attendu: +2% (donc 7%)

Si puissance = 80%:
→ 80% de chances de détecter cette différence SI elle existe
→ 20% de risque de la manquer (erreur Type II)
```

---

### 1.3 Taille d'Effet (Effect Size)

#### Pourquoi Important?

**Significativité statistique ≠ Importance pratique**

```
Exemple 1: n=10,000
Différence: 100 HTG sur solde moyen de 100,000 HTG
p = 0.001 (TRÈS significatif)
Mais 0.1% de différence = NÉGLIGEABLE pratiquement

Exemple 2: n=20
Différence: 10,000 HTG sur solde moyen de 50,000 HTG
p = 0.15 (NON significatif)
Mais 20% de différence = IMPORTANTE pratiquement
```

#### Cohen's d (Différence de Moyennes)

**Formule**:
```
d = (x̄₁ - x̄₂) / s_pooled

Où s_pooled = √[(s₁² + s₂²) / 2]
```

**Interprétation**:
```
|d| < 0.2: Effet NÉGLIGEABLE
0.2 ≤ |d| < 0.5: Effet FAIBLE
0.5 ≤ |d| < 0.8: Effet MODÉRÉ
|d| ≥ 0.8: Effet FORT
```

**Exemple**:
```
Groupe A: x̄ = 50,000 HTG, s = 10,000
Groupe B: x̄ = 55,000 HTG, s = 12,000

d = (55,000 - 50,000) / √[(10,000² + 12,000²)/2]
d = 5,000 / √(122,000,000)
d = 5,000 / 11,045
d = 0.45 (Effet FAIBLE à MODÉRÉ)
```

---

#### Omega² (ANOVA)

**Définition**: Proportion de variance expliquée par le facteur

**Formule**:
```
ω² = (SSB - (k-1)×MSW) / (SST + MSW)

Où:
SSB = Somme carrés ENTRE
SST = Somme carrés TOTALE
MSW = Moyenne carrés À L'INTÉRIEUR
k = Nombre de groupes
```

**Interprétation**:
```
ω² < 0.01: Effet négligeable
0.01 ≤ ω² < 0.06: Effet faible
0.06 ≤ ω² < 0.14: Effet modéré
ω² ≥ 0.14: Effet fort
```

---

#### Phi (φ) pour Chi-Carré

**Formule (table 2×2)**:
```
φ = √(χ² / n)
```

**Interprétation**:
```
|φ| < 0.1: Association négligeable
0.1 ≤ |φ| < 0.3: Association faible
0.3 ≤ |φ| < 0.5: Association modérée
|φ| ≥ 0.5: Association forte
```

---

### 1.4 Calcul de la Puissance

#### Formule Approximative (Test t)

```
Puissance ≈ Φ[δ√(n/2) - Z_(α/2)]

Où:
δ = Taille d'effet (Cohen's d)
n = Taille TOTALE échantillon
Φ = Fonction distribution normale
Z_(α/2) = Valeur critique (1.96 pour α=0.05 bilatéral)
```

#### Exemple Pratique

**Question**: Quelle puissance pour détecter d=0.5 avec n=100 par groupe?

```
δ = 0.5
n_total = 200
α = 0.05 (bilatéral) → Z = 1.96

Puissance ≈ Φ[0.5 × √(200/2) - 1.96]
         ≈ Φ[0.5 × 10 - 1.96]
         ≈ Φ[5 - 1.96]
         ≈ Φ[3.04]
         ≈ 0.998 (99.8%)
```

**Conclusion**: Excellente puissance! On détectera presque certainement un effet d=0.5.

---

### 1.5 Calcul Taille d'Échantillon Nécessaire

#### Formule (Test t, 2 groupes)

```
n = 2 × [(Z_α/2 + Z_β) / δ]²

Où:
Z_α/2 = 1.96 (pour α=0.05 bilatéral)
Z_β = 0.84 (pour puissance 80%)
δ = Taille d'effet (Cohen's d)
```

#### Exemple Banking

**Question**: Combien de clients pour détecter différence de 5,000 HTG (d=0.5) avec 80% de puissance?

```
n = 2 × [(1.96 + 0.84) / 0.5]²
n = 2 × [2.8 / 0.5]²
n = 2 × [5.6]²
n = 2 × 31.36
n = 62.72 ≈ 63 par groupe
n_total = 126 clients
```

---

### 1.6 Scénario Banking Complet

**Contexte DPO**: Tester nouvelle campagne anti-fraude

**Données Actuelles**:
- Taux fraude actuel: 2%
- Objectif campagne: Réduire à 1% (MDE = 1%)

**Question 1**: Quelle taille d'échantillon pour 80% de puissance?

```
p₁ = 0.02, p₂ = 0.01
δ = |p₁ - p₂| = 0.01
p̄ = (0.02 + 0.01)/2 = 0.015

n ≈ 2 × [(1.96 + 0.84)² × p̄(1-p̄)] / δ²
n ≈ 2 × [7.84 × 0.015 × 0.985] / 0.0001
n ≈ 2,309 transactions par groupe
n_total ≈ 4,618 transactions minimum
```

**Question 2**: Avec seulement 1,000 par groupe, quelle puissance?

```
Puissance ≈ 40% (insuffisant!)
```

**Décision Business**:
- Option A: Collecter plus de données (4,618 minimum)
- Option B: Accepter puissance réduite (risque manquer l'effet)
- Option C: Allonger durée test pour atteindre n nécessaire

---

## 2. TESTS POST-HOC DÉTAILLÉS

### 2.1 Pourquoi Post-Hoc?

#### Problème
ANOVA dit "au moins une différence" mais ne dit PAS laquelle!

```
Exemple: 4 agences
ANOVA: F=8.5, p=0.001 → Au moins 1 différence

Mais quelles paires diffèrent?
Nord-Sud? Nord-Est? Nord-Ouest?
Sud-Est? Sud-Ouest? Est-Ouest?
→ 6 comparaisons possibles!
```

---

### 2.2 Test de Tukey HSD (Honestly Significant Difference)

#### Quand Utiliser
- Après ANOVA significative
- Comparer TOUTES les paires
- Échantillons de tailles égales

#### Formule
```
HSD = q_α × √(MSW / n)

Où:
q_α = Valeur de Tukey (table)
MSW = Moyenne carrés À L'INTÉRIEUR (de l'ANOVA)
n = Taille commune des groupes
```

#### Règle de Décision
```
Si |x̄ᵢ - x̄ⱼ| > HSD → Différence significative
```

#### Exemple Banking

**Contexte**: Comparer soldes moyens entre 4 agences (n=30 chacune)

**Résultats ANOVA**:
```
Nord: 25,000 HTG
Sud:  30,000 HTG
Est:  28,000 HTG
Ouest: 32,000 HTG

MSW = 25,000,000 HTG²
F = 8.45, p < 0.001
```

**Calcul HSD**:
```
q(0.05, 4, 116) ≈ 3.70
HSD = 3.70 × √(25,000,000 / 30)
HSD = 3.70 × 913
HSD = 3,378 HTG
```

**Comparaisons**:
```
Nord-Sud:  |25K-30K| = 5,000 > 3,378 ✓ SIGNIFICATIF
Nord-Est:  |25K-28K| = 3,000 < 3,378 ✗ Non significatif
Nord-Ouest:|25K-32K| = 7,000 > 3,378 ✓ SIGNIFICATIF
Sud-Est:   |30K-28K| = 2,000 < 3,378 ✗ Non significatif
Sud-Ouest: |30K-32K| = 2,000 < 3,378 ✗ Non significatif
Est-Ouest: |28K-32K| = 4,000 > 3,378 ✓ SIGNIFICATIF
```

**Conclusion**:
- Nord diffère de Sud ET Ouest
- Est diffère de Ouest
- Les autres paires ne diffèrent pas significativement

**Graphique Mental**:
```
Groupes Homogènes:
Groupe A: Nord
Groupe B: Est, Sud
Groupe C: Sud, Ouest
```

---

### 2.3 Test de Bonferroni

#### Principe
Ajuster α pour chaque comparaison

#### Formule
```
α_ajusté = α / m

Où m = nombre de comparaisons
```

#### Quand Utiliser
- Peu de comparaisons planifiées (< 10)
- Veut minimiser Erreur Type I

#### Exemple

**4 groupes → 6 comparaisons possibles**
```
α_original = 0.05
α_ajusté = 0.05 / 6 = 0.0083

Utiliser α=0.0083 pour chaque test t individuel
```

**Avantage**: Très conservateur (peu de faux positifs)  
**Inconvénient**: Perd de la puissance (peut manquer vrais effets)

---

### 2.4 Test de Scheffé

#### Quand Utiliser
- Comparaisons complexes (ex: A+B vs C+D)
- Après coup (non planifié)

#### Formule
```
S = √[(k-1) × F_critique]

Différence significative si:
|Contraste| > S × √(MSW × Σ(c²ᵢ/nᵢ))
```

**Avantage**: Le plus flexible (tout type de comparaison)  
**Inconvénient**: Le plus conservateur (moins de puissance)

---

### 2.5 Test de Dunn (Post-hoc pour Kruskal-Wallis)

#### Quand Utiliser
Après Kruskal-Wallis significatif (version non-paramétrique)

#### Principe
Compare rangs moyens entre paires, avec ajustement Bonferroni

#### Exemple

**Contexte**: Satisfaction (ordinal) entre 3 segments

**Résultats Kruskal-Wallis**:
```
H = 12.5, p = 0.002
→ Au moins une différence
```

**Test de Dunn**:
```
Premium vs Standard: p_ajusté = 0.001 ✓
Premium vs Bronze:   p_ajusté = 0.008 ✓
Standard vs Bronze:  p_ajusté = 0.15  ✗
```

---

## 3. AJUSTEMENTS POUR COMPARAISONS MULTIPLES

### 3.1 Problème du Multiple Testing

#### Inflation de l'Erreur Type I

**Principe**:
```
Pour 1 test: P(Erreur Type I) = α = 0.05 (5%)

Pour m tests indépendants:
P(Au moins 1 erreur) = 1 - (1-α)^m

Exemples:
m=5:  1 - 0.95⁵ = 0.226 (22.6%)
m=10: 1 - 0.95¹⁰ = 0.401 (40.1%)
m=20: 1 - 0.95²⁰ = 0.642 (64.2%)
```

**Danger**: Plus on teste, plus on trouve de "faux positifs"!

---

### 3.2 Méthodes de Correction

#### Tableau Comparatif

| Méthode | α_ajusté | Puissance | Quand utiliser |
|---------|----------|-----------|----------------|
| **Bonferroni** | α/m | Faible | Peu de tests (<10), tests planifiés |
| **Holm** | α/(m-i+1) | Moyenne | Alternative à Bonferroni |
| **Benjamini-Hochberg** | (i/m)×α | Élevée | Beaucoup de tests, exploration |

---

#### Méthode de Bonferroni

**Formule**:
```
α_ajusté = α / m
```

**Exemple Banking**:
```
Tester 10 KPIs bancaires
α = 0.05
α_ajusté = 0.05 / 10 = 0.005

Rejeter H₀ seulement si p < 0.005
```

**Avantage**: Simple, très conservateur  
**Inconvénient**: Peut manquer vrais effets (perte de puissance)

---

#### Méthode de Holm (Sequential Bonferroni)

**Procédure**:
1. Ordonner p-values: p₁ ≤ p₂ ≤ ... ≤ pₘ
2. Comparer:
   - p₁ < α/m ?
   - p₂ < α/(m-1) ?
   - p₃ < α/(m-2) ?
   - Continuer jusqu'au premier NON

**Exemple**:
```
5 tests, α=0.05
p-values: 0.001, 0.008, 0.015, 0.03, 0.06

Test 1: 0.001 < 0.05/5 = 0.01 ✓ Rejeter
Test 2: 0.008 < 0.05/4 = 0.0125 ✓ Rejeter
Test 3: 0.015 < 0.05/3 = 0.0167 ✓ Rejeter
Test 4: 0.03 < 0.05/2 = 0.025 ✗ STOP ici
Test 5: Non testé

Conclusion: Tests 1, 2, 3 significatifs
```

**Avantage**: Plus puissant que Bonferroni  
**Inconvénient**: Plus complexe

---

#### Méthode de Benjamini-Hochberg (FDR)

**Principe**: Contrôle le taux de Fausses Découvertes (False Discovery Rate)

**Procédure**:
1. Ordonner p-values: p₁ ≤ p₂ ≤ ... ≤ pₘ
2. Trouver le plus grand i tel que: pᵢ ≤ (i/m) × α
3. Rejeter H₀ pour tests 1, 2, ..., i

**Exemple**:
```
10 tests, α=0.05
p-values ordonnées:
p₁=0.001, p₂=0.003, p₃=0.008, p₄=0.012,
p₅=0.025, p₆=0.04, p₇=0.06, p₈=0.08,
p₉=0.15, p₁₀=0.30

Vérification:
i=1: 0.001 ≤ (1/10)×0.05 = 0.005 ✓
i=2: 0.003 ≤ (2/10)×0.05 = 0.01 ✓
i=3: 0.008 ≤ (3/10)×0.05 = 0.015 ✓
i=4: 0.012 ≤ (4/10)×0.05 = 0.02 ✓
i=5: 0.025 ≤ (5/10)×0.05 = 0.025 ✓
i=6: 0.04 ≤ (6/10)×0.05 = 0.03 ✗

Plus grand i = 5
→ Rejeter tests 1, 2, 3, 4, 5
```

**Avantage**: Le plus puissant, bon pour exploration  
**Inconvénient**: Accepte plus de faux positifs (contrôle FDR, pas FWER)

---

### 3.3 Scénario Banking: A/B/C/D Test

**Contexte**: Tester 4 versions d'email marketing

**Données**:
| Version | Conversions | Total | Taux | p-value vs A |
|---------|-------------|-------|------|--------------|
| A (contrôle) | 100 | 1000 | 10% | - |
| B | 120 | 1000 | 12% | 0.03 |
| C | 130 | 1000 | 13% | 0.01 |
| D | 105 | 1000 | 10.5% | 0.45 |

**Sans correction**:
```
B et C significatifs à α=0.05
```

**Avec Bonferroni** (3 comparaisons):
```
α_ajusté = 0.05/3 = 0.0167

B: 0.03 > 0.0167 ✗ Non significatif
C: 0.01 < 0.0167 ✓ Significatif
D: 0.45 > 0.0167 ✗ Non significatif

→ Seule version C significativement meilleure
```

**Décision Business**: Déployer version C, elle surperforme significativement le contrôle (+30% conversion).

---

## 4. TESTS EXACTS

### 4.1 Test Exact de Fisher

#### Quand Utiliser
- Table 2×2
- Effectifs PETITS (attendus < 5)
- Alternative EXACTE au Chi-carré

#### Principe
Calcule probabilité EXACTE (pas approximation)

#### Formule
```
p = (a+b)!(c+d)!(a+c)!(b+d)! / (n! × a! × b! × c! × d!)

Pour table:
        Y    N
Exposé  a    b
Non-exp c    d
```

#### Exemple Banking

**Contexte**: Test fraude sur petit échantillon

**Données**:
|          | Fraude | Pas Fraude | Total |
|----------|--------|------------|-------|
| Nouveau  | 3      | 7          | 10    |
| Ancien   | 1      | 14         | 15    |
| **Total**| 4      | 21         | 25    |

**Chi-carré**: Attendu = (10×4)/25 = 1.6 < 5 → PAS VALIDE

**Test Exact de Fisher**:
```
p_exact = 0.31

Conclusion: Pas de différence significative entre nouveaux et anciens clients
```

---

### 4.2 Test Binomial Exact

#### Quand Utiliser
- Tester UNE proportion
- Petit échantillon (n < 30)
- Alternative exacte au test Z

#### Principe
Utilise distribution binomiale (pas approximation normale)

#### Exemple Banking

**Contexte**: Sur 15 dossiers audités, 5 ont des erreurs (33%). Le taux acceptable est 20%.

**Test Binomial Exact**:
```
H₀: p = 0.20
H₁: p > 0.20

p_exact = P(X ≥ 5 | n=15, p=0.20)
p_exact = 0.188

Conclusion: p = 0.188 > 0.05
Ne peut pas conclure taux anormalement élevé
```

**Comparaison Test Z** (pour montrer différence):
```
Test Z donnerait p ≈ 0.15 (moins précis avec petit n)
```

---

## 5. ANALYSE DE SURVIE (BASES)

### 5.1 Concepts Fondamentaux

#### Définition
Analyse du TEMPS jusqu'à un événement

#### Applications Banking
- Temps jusqu'à défaut de paiement
- Durée de vie d'un compte
- Temps avant churn client
- Délai avant activation produit

#### Caractéristiques Uniques
1. **Censure**: Observations incomplètes (ex: client n'a pas encore quitté à la fin de l'étude)
2. **Temps d'observation variable**
3. **Événement binaire** (arrivé ou non)

---

### 5.2 Fonction de Survie S(t)

#### Définition
```
S(t) = P(T > t) = Probabilité de survivre au-delà du temps t
```

#### Propriétés
```
S(0) = 1 (tous "vivants" au début)
S(∞) = 0 (tous "morts" éventuellement)
Fonction décroissante
```

#### Exemple Banking

**Contexte**: Survie des comptes (temps avant fermeture)

```
S(3 mois) = 0.95 → 95% des comptes actifs après 3 mois
S(12 mois) = 0.80 → 80% actifs après 1 an
S(24 mois) = 0.65 → 65% actifs après 2 ans
```

---

### 5.3 Estimateur de Kaplan-Meier

#### Principe
Estime S(t) en tenant compte de la censure

#### Formule
```
S(t) = ∏[1 - (dᵢ/nᵢ)]

Pour tous i où tᵢ ≤ t

Où:
dᵢ = Nombre d'événements au temps tᵢ
nᵢ = Nombre à risque juste avant tᵢ
```

#### Exemple Banking Simplifié

**Contexte**: Survie de 10 prêts (temps jusqu'à défaut)

**Données**:
```
Prêt 1: Défaut mois 3
Prêt 2: Censuré mois 5 (remboursé)
Prêt 3: Défaut mois 6
Prêt 4: Actif mois 12 (fin étude)
Prêt 5: Défaut mois 3
...
```

**Calcul**:
```
Temps 3 mois:
- 2 défauts
- 10 à risque
- S(3) = 1 × (1 - 2/10) = 0.80

Temps 6 mois:
- 1 défaut
- 7 à risque (10 - 2 défauts - 1 censuré)
- S(6) = 0.80 × (1 - 1/7) = 0.686

→ 68.6% des prêts survivent 6 mois
```

---

### 5.4 Test du Log-Rank

#### Définition
Compare courbes de survie entre DEUX groupes

#### Quand Utiliser
- Comparer temps de survie entre 2 segments
- Exemple: Défaut Premium vs Standard

#### Hypothèses
```
H₀: Les courbes de survie sont identiques
H₁: Les courbes diffèrent
```

#### Principe
Compare nombre d'événements OBSERVÉS vs ATTENDUS à chaque temps

#### Exemple Banking

**Contexte**: Comparer défaut entre Anciens vs Nouveaux clients

**Résultats**:
```
Log-Rank χ² = 8.45
p-value = 0.004

Conclusion: Les courbes de survie diffèrent significativement
→ Nouveaux clients ont taux de défaut plus élevé
```

**Graphique Mental**:
```
Survie
100% ──────┐
           │ Anciens (meilleure survie)
 80% ──────┼────┐
           │    │
 60% ───────────┼─ Nouveaux
           │    │
 40% ───────────┴───
     0   6   12  18 Mois
```

---

### 5.5 Temps Médian de Survie

#### Définition
Temps auquel S(t) = 0.50 (50% ont connu l'événement)

#### Calcul
Trouver t tel que S(t) = 0.50

#### Exemple

**Contexte**: Durée moyenne avant churn

```
S(6 mois) = 0.75
S(12 mois) = 0.45
S(18 mois) = 0.30

Temps médian ≈ 11 mois (interpolation)
→ 50% des clients partent avant 11 mois
```

**Interprétation Business**:
- Temps critique = 11 mois
- Programme rétention à cibler à 9-10 mois

---

## 6. CORRÉLATION PARTIELLE

### 6.1 Définition

#### Principe
Corrélation entre X et Y APRÈS avoir retiré l'effet d'une variable Z

```
Corrélation Partielle r(X,Y|Z) = Corrélation entre:
- Résidus de X après régression sur Z
- Résidus de Y après régression sur Z
```

#### Pourquoi Important?

**Exemple**: Corrélation glace ↔ noyades

```
Corrélation simple: r = 0.8 (forte!)
Mais variable cachée: Température

Corrélation partielle (contrôlant température): r = 0.05 (négligeable)
→ La température EXPLIQUE la corrélation apparente
```

---

### 6.2 Formule

```
r(X,Y|Z) = (r_XY - r_XZ × r_YZ) / √[(1-r²_XZ) × (1-r²_YZ)]

Où:
r_XY = Corrélation simple X-Y
r_XZ = Corrélation simple X-Z
r_YZ = Corrélation simple Y-Z
```

---

### 6.3 Exemple Banking Complet

**Contexte DPO**: Analyser relation Solde ↔ Nombre Transactions

**Hypothèse**: Variable cachée = Ancienneté client

**Données**:
```
r(Solde, Transactions) = 0.65 (forte corrélation)
r(Solde, Ancienneté) = 0.70
r(Transactions, Ancienneté) = 0.75
```

**Calcul Corrélation Partielle**:
```
r(Solde, Trans | Ancienneté) = (0.65 - 0.70×0.75) / √[(1-0.70²)×(1-0.75²)]
                               = (0.65 - 0.525) / √[0.51 × 0.4375]
                               = 0.125 / √0.223
                               = 0.125 / 0.472
                               = 0.26
```

**Interprétation**:
```
Corrélation simple: 0.65 (forte)
Corrélation partielle: 0.26 (faible)

→ La relation Solde-Transactions est LARGEMENT due à l'ancienneté
→ Clients anciens ont + de solde ET + de transactions
→ Contrôler ancienneté réduit fortement la corrélation
```

**Décision Business**:
- Ne pas baser stratégie sur corrélation simple Solde-Transactions
- Segmenter par ancienneté d'abord
- Analyser patterns DANS chaque segment d'ancienneté

---

### 6.4 Scénario: Variable de Confusion

**Contexte**: Relation Score Crédit ↔ Montant Prêt

**Observation Initiale**:
```
r(Score, Montant) = 0.80 (forte)
Conclusion naïve: Score élevé → Gros prêts
```

**Variable Cachée**: Revenu

**Analyse**:
```
r(Score, Revenu) = 0.85
r(Montant, Revenu) = 0.90

Corrélation partielle:
r(Score, Montant | Revenu) = 0.15 (faible!)
```

**Vérité**:
- Revenu ÉLEVÉ → Score ÉLEVÉ (peuvent rembourser)
- Revenu ÉLEVÉ → Prêt ÉLEVÉ (capacité emprunt)
- Relation directe Score-Montant est FAIBLE

**Impact**: Modèle de scoring doit inclure REVENU explicitement

---

## 7. RÉGRESSION LOGISTIQUE SIMPLE

### 7.1 Principe

#### Différence avec Régression Linéaire

```
Régression Linéaire:
Y continue = β₀ + β₁X + ε

Régression Logistique:
Y binaire (0/1) → P(Y=1) = ?
```

#### Fonction Logit
```
logit(p) = ln[p/(1-p)] = β₀ + β₁X

Où:
p = P(Y=1)
p/(1-p) = Odds
```

#### Transformation Inverse
```
p = e^(β₀+β₁X) / (1 + e^(β₀+β₁X))
```

---

### 7.2 Interprétation des Coefficients

#### Coefficient β₁

```
exp(β₁) = Odds Ratio (OR)
```

**Interprétation**:
```
OR = 1: X n'a pas d'effet
OR > 1: Augmentation de X augmente probabilité Y=1
OR < 1: Augmentation de X diminue probabilité Y=1
```

#### Exemple Banking

**Modèle**: Prédire Défaut en fonction du Score

```
logit(P_défaut) = 5 - 0.01 × Score

β₁ = -0.01
OR = exp(-0.01) = 0.990

Interprétation:
Pour chaque point de score supplémentaire,
l'odds de défaut diminue de 1% (×0.99)
```

**Calcul Pratique**:
```
Score 600:
logit = 5 - 0.01×600 = -1
P = e^(-1) / (1+e^(-1)) = 0.27 (27% défaut)

Score 700:
logit = 5 - 0.01×700 = -2
P = e^(-2) / (1+e^(-2)) = 0.12 (12% défaut)
```

---

### 7.3 Exemple Complet: Modèle Défaut

**Contexte DPO**: Prédire défaut avec Score et Ratio Dette/Revenu

**Modèle**:
```
logit(P_défaut) = 3 - 0.008×Score + 2×RatioDette
```

**Coefficients**:
```
Intercept: β₀ = 3
Score: β₁ = -0.008 → OR = exp(-0.008) = 0.992
RatioDette: β₂ = 2 → OR = exp(2) = 7.39
```

**Interprétation**:
1. **Score**: +1 point → Odds défaut ×0.992 (↓0.8%)
2. **RatioDette**: +0.1 (10%) → Odds défaut ×e^(2×0.1) = ×1.22 (↑22%)

**Prédiction Client Type**:
```
Score = 650
RatioDette = 0.4 (40%)

logit = 3 - 0.008×650 + 2×0.4
      = 3 - 5.2 + 0.8
      = -1.4

P_défaut = e^(-1.4) / (1+e^(-1.4))
         = 0.198 (19.8%)
```

**Décision Crédit**:
```
Seuil acceptable: 15%
P_observé: 19.8%
→ REFUSER le prêt (risque trop élevé)
```

---

### 7.4 Test de Significativité

#### Test de Wald

**Hypothèses**:
```
H₀: βᵢ = 0 (variable n'a pas d'effet)
H₁: βᵢ ≠ 0
```

**Statistique**:
```
z = β̂ᵢ / SE(β̂ᵢ)

Suit loi normale standard
```

**Exemple**:
```
β̂₁ = -0.008
SE = 0.002

z = -0.008 / 0.002 = -4.0
p-value < 0.001

Conclusion: Score a effet SIGNIFICATIF
```

---

### 7.5 Qualité du Modèle

#### Pseudo R² (McFadden)

```
R²_McFadden = 1 - (Log L_modèle / Log L_null)

Interprétation:
> 0.2: Bon ajustement
> 0.4: Très bon
```

#### AIC (Akaike Information Criterion)

```
AIC = -2×Log L + 2×k

Où k = nombre de paramètres

Plus bas = Meilleur modèle
```

#### Courbe ROC et AUC

**AUC (Area Under Curve)**:
```
0.5: Pas mieux que hasard
0.7-0.8: Acceptable
0.8-0.9: Excellent
> 0.9: Exceptionnel
```

**Exemple Banking**:
```
Modèle Défaut:
AUC = 0.85

Interprétation: 85% de chances que modèle range
correctement paire (défaut, non-défaut)
→ Excellent pouvoir prédictif
```

---

### 7.6 Scénario Complet: Modèle Approbation Crédit

**Contexte**: Construire modèle approbation automatique

**Variables**:
- Score crédit (600-850)
- Revenu annuel (HTG)
- Ratio Dette/Revenu (0-1)
- Ancienneté emploi (années)

**Modèle Estimé**:
```
logit(P_défaut) = 8.5
                  - 0.01×Score
                  + 2.5×RatioDette
                  - 0.0001×Revenu
                  - 0.15×Ancienneté
```

**Tests de Significativité**:
```
Score: p < 0.001 ✓✓✓
RatioDette: p < 0.001 ✓✓✓
Revenu: p = 0.03 ✓
Ancienneté: p = 0.18 ✗ (Non significatif)
```

**Décision**: Retirer Ancienneté du modèle

**Modèle Final**:
```
logit(P_défaut) = 8
                  - 0.01×Score
                  + 2.5×RatioDette
                  - 0.0001×Revenu

AUC = 0.87 (Excellent)
```

**Seuils Décision**:
```
P_défaut < 5%: Approbation AUTO
5% ≤ P < 15%: Revue MANUELLE
P ≥ 15%: Refus AUTO
```

**Application Client**:
```
Client A:
Score = 750
RatioDette = 0.25
Revenu = 500,000 HTG

logit = 8 - 0.01×750 + 2.5×0.25 - 0.0001×500,000
      = 8 - 7.5 + 0.625 - 50
      = -48.875

P = e^(-48.875) / (1 + e^(-48.875)) ≈ 0 (0%)
→ APPROBATION AUTOMATIQUE
```

---

## RÉSUMÉ EXÉCUTIF

### Points Clés à Retenir

1. **Puissance Statistique**
   - Standard: 80%
   - Augmente avec n et taille d'effet
   - Calculer AVANT de collecter données

2. **Taille d'Effet**
   - Plus important que p-value
   - Cohen's d: <0.2 (faible), 0.2-0.8 (modéré), >0.8 (fort)
   - Toujours rapporter avec résultats

3. **Tests Post-Hoc**
   - Tukey HSD: Toutes comparaisons, tailles égales
   - Bonferroni: Conservateur, peu de tests
   - Dunn: Pour Kruskal-Wallis

4. **Comparaisons Multiples**
   - Bonferroni: α/m (très conservateur)
   - Holm: Séquentiel (meilleur)
   - BH: FDR (plus puissant, exploration)

5. **Tests Exacts**
   - Fisher: Table 2×2, petits effectifs
   - Binomial: Proportion, petit n

6. **Analyse Survie**
   - Kaplan-Meier: Estimer S(t)
   - Log-Rank: Comparer courbes
   - Temps médian: Quand 50% événement

7. **Corrélation Partielle**
   - Retire effet variable de confusion
   - Peut réduire fortement corrélation simple
   - Essentiel pour causalité

8. **Régression Logistique**
   - Y binaire
   - OR = exp(β)
   - Prédiction: P(Y=1)
   - Évaluer: AUC, Pseudo R²

---

**TU ES PRÊT ALEXANDRO! 💪🔥**
