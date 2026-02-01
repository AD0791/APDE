# MANUEL STATISTIQUES DESCRIPTIVES - VERSION EXAMEN
## Data Analyst DPO - UniBank Haiti
### Concepts, Formules, Interprétation, Décisions

---

## TABLE DES MATIÈRES

1. [Types de Variables et Niveaux de Mesure](#1-types-de-variables)
2. [Mesures de Tendance Centrale](#2-mesures-de-tendance-centrale)
3. [Mesures de Dispersion](#3-mesures-de-dispersion)
4. [Mesures de Position](#4-mesures-de-position)
5. [Mesures de Forme](#5-mesures-de-forme)
6. [Visualisations Appropriées](#6-visualisations-appropriées)
7. [Détection d'Outliers](#7-détection-doutliers)
8. [Scénarios Banking](#8-scénarios-banking)

---

## 1. TYPES DE VARIABLES

### 1.1 Classification Hiérarchique

```
VARIABLES
│
├── QUALITATIVES (Catégorielles)
│   ├── Nominales (pas d'ordre)
│   │   ├── Binaires: 2 catégories
│   │   └── Polytomiques: 3+ catégories
│   └── Ordinales (ordre naturel)
│
└── QUANTITATIVES (Numériques)
    ├── Discrètes (entiers dénombrables)
    └── Continues (valeurs mesurables)
```

---

### 1.2 Tableau Comparatif Détaillé

| Type | Définition | Opérations | Statistiques | Exemples Banking |
|------|-----------|------------|--------------|------------------|
| **Nominale** | Catégories sans ordre | =, ≠ | Mode, Fréquences | Type compte, Agence, Région |
| **Ordinale** | Catégories ordonnées | <, >, =, ≠ | Mode, Médiane | Rating (AAA>AA>A), Satisfaction (1-5) |
| **Discrète** | Valeurs entières | +, -, ×, ÷ | Toutes | Nb transactions, Nb produits |
| **Continue** | Mesures précises | +, -, ×, ÷ | Toutes | Solde HTG, Taux %, Âge |

---

### 1.3 Mnémotechnique: N-O-I-R

```
N - Nominale: Noms sans ordre
O - Ordinale: Ordre naturel
I - Intervalle: Intervalles égaux, zéro arbitraire
R - Ratio: Ratios possibles, zéro absolu
```

#### Exemples par Niveau

**Nominale**: Type compte  
- Épargne, Courant, DAT
- Aucun ordre logique
- On peut seulement compter: 40% Épargne, 35% Courant, 25% DAT

**Ordinale**: Satisfaction  
- Très insatisfait < Insatisfait < Neutre < Satisfait < Très satisfait
- Ordre clair MAIS distance entre niveaux NON égale
- Médiane appropriée, moyenne NON

**Intervalle**: Température °C  
- 20°C vs 30°C: différence = 10°C
- MAIS 30°C n'est PAS "2 fois plus chaud" que 15°C
- Zéro arbitraire (0°C ≠ absence chaleur)

**Ratio**: Solde HTG  
- 100,000 HTG est VRAIMENT 2× plus que 50,000 HTG
- Zéro absolu (0 HTG = aucun argent)
- Toutes opérations mathématiques valides

---

### 1.4 Règle du Choix de Statistique

```
Type Variable → Statistique Appropriée

NOMINALE → MODE uniquement
ORDINALE → MODE, MÉDIANE
DISCRÈTE/CONTINUE → MODE, MÉDIANE, MOYENNE

Mnémotechnique:
"Mode pour Mots, Médiane pour rangs Ordonnés, Moyenne pour Mesures"
```

---

## 2. MESURES DE TENDANCE CENTRALE

### 2.1 La Moyenne (Mean)

#### Définition
**Centre de gravité** des données

#### Formule
```
x̄ = Σxᵢ / n = (x₁ + x₂ + ... + xₙ) / n
```

#### Propriétés
✅ Utilise TOUTES les valeurs  
✅ Minimise Σ(xᵢ - x̄)²  
❌ Sensible aux OUTLIERS  
❌ Peut être trompeur si distribution asymétrique

#### Exemple Banking

**Contexte**: Soldes comptes  
Données: 10K, 15K, 18K, 20K, 22K, 500K HTG

```
Moyenne = (10+15+18+20+22+500) / 6 = 97.5K HTG

⚠️ PROBLÈME: 97.5K ne représente PAS le client "typique"!
L'outlier (500K) fausse complètement la moyenne.
```

#### Quand Utiliser
- Distribution SYMÉTRIQUE
- SANS outliers importants
- Données continues

---

### 2.2 La Médiane (Median)

#### Définition
Valeur CENTRALE qui sépare données en 2 moitiés égales

#### Procédure de Calcul
```
1. ORDONNER les données
2. Si n impair: Médiane = valeur centrale
3. Si n pair: Médiane = moyenne des 2 valeurs centrales
```

#### Formule Position
```
Position = (n + 1) / 2
```

#### Exemple

**Contexte**: Même données (10K, 15K, 18K, 20K, 22K, 500K)

```
Données ordonnées: 10, 15, 18, 20, 22, 500
n = 6 (pair)
Position centrale = entre 3ème et 4ème valeurs
Médiane = (18K + 20K) / 2 = 19K HTG

✅ 19K représente MIEUX le client typique
```

#### Propriétés
✅ ROBUSTE aux outliers  
✅ Bonne pour distributions asymétriques  
✅ Applicable aux données ORDINALES  
❌ N'utilise pas toutes les valeurs  
❌ Moins efficace statistiquement si normalité

#### Quand Utiliser
- Distribution ASYMÉTRIQUE
- Présence d'OUTLIERS
- Données ordinales
- Revenus, prix immobiliers, soldes

---

### 2.3 Le Mode

#### Définition
Valeur la plus FRÉQUENTE

#### Types
```
- Unimodale: 1 seul pic
- Bimodale: 2 pics
- Multimodale: 3+ pics
- Uniforme: Aucun mode
```

#### Exemple Banking

**Contexte**: Type de transaction le plus fréquent

```
Retraits ATM: 450
Transferts: 320
Paiements: 280
Dépôts: 150

Mode = Retraits ATM (le plus fréquent)
```

#### Propriétés
✅ Seule mesure pour données NOMINALES  
✅ Facile à comprendre  
❌ Peut ne pas exister  
❌ Peut être multiple

#### Quand Utiliser
- Variables CATÉGORIELLES
- Identifier valeur la plus commune
- Décisions opérationnelles (ex: produit le plus vendu)

---

### 2.4 Comparaison et Choix

#### Tableau de Décision

| Situation | Mesure Recommandée | Raison |
|-----------|-------------------|--------|
| Distribution symétrique, sans outliers | **Moyenne** | Utilise toute l'info |
| Distribution asymétrique | **Médiane** | Robuste |
| Présence outliers | **Médiane** | Non influencée |
| Données ordinales | **Médiane** ou **Mode** | Moyenne non applicable |
| Données nominales | **Mode** | Seule option |
| Comparaisons statistiques | **Moyenne** | Tests paramétriques |

---

#### Règle Pratique: Relation Moyenne-Médiane

```
Distribution SYMÉTRIQUE:
Moyenne ≈ Médiane

Distribution ASYMÉTRIQUE DROITE (positive):
Moyenne > Médiane
(Outliers élevés tirent moyenne vers le haut)

Distribution ASYMÉTRIQUE GAUCHE (négative):
Moyenne < Médiane
(Outliers faibles tirent moyenne vers le bas)
```

#### Graphique Mental

```
Symétrique:
        /\
       /  \
    Mode=Médiane=Moyenne

Asymétrique Droite:
      /\___
     /     ---__
  Mode  Médiane  Moyenne →

Asymétrique Gauche:
        ___/\
    ___--    \
  ← Moyenne  Médiane  Mode
```

---

## 3. MESURES DE DISPERSION

### 3.1 L'Étendue (Range)

#### Définition
```
Étendue = Maximum - Minimum
```

#### Exemple
```
Soldes: 5K, 10K, 15K, 20K, 100K
Étendue = 100K - 5K = 95K HTG
```

#### Propriétés
✅ Très simple à calculer  
✅ Facile à comprendre  
❌ EXTRÊMEMENT sensible aux outliers  
❌ Ignore distribution intermédiaire  
❌ Augmente avec taille échantillon

#### Usage
- Première exploration rapide
- Vérifier plausibilité des données
- Identifier potentiels outliers

---

### 3.2 La Variance (Variance)

#### Définition
**Moyenne des carrés des écarts à la moyenne**

#### Formule Population
```
σ² = Σ(xᵢ - μ)² / N
```

#### Formule Échantillon
```
s² = Σ(xᵢ - x̄)² / (n-1)

⚠️ Division par (n-1) et NON n (correction de Bessel)
Raison: Estimateur non biaisé
```

#### Exemple Banking

**Contexte**: Variabilité des soldes (en milliers HTG)

```
Données: 10, 15, 20, 25, 30
Moyenne: x̄ = 20

Écarts: -10, -5, 0, 5, 10
Carrés: 100, 25, 0, 25, 100

s² = (100+25+0+25+100) / (5-1)
   = 250 / 4
   = 62.5 K²HTG²

⚠️ Unités: Carrés! (K²HTG²) → Pas directement interprétable
```

#### Propriétés
✅ Base mathématique solide  
✅ Utilisée dans tests statistiques  
❌ Unités au carré (difficile interpréter)  
❌ Sensible aux outliers

---

### 3.3 L'Écart-Type (Standard Deviation)

#### Définition
**Racine carrée de la variance** → Même unité que les données

#### Formule
```
s = √s² = √[Σ(xᵢ - x̄)² / (n-1)]
```

#### Même Exemple
```
s = √62.5 = 7.9K HTG

✅ Unités: KHTG (interprétable!)
Interprétation: En moyenne, les soldes s'écartent de 7.9K de la moyenne
```

#### Règle 68-95-99.7 (Loi Normale)

```
Dans une distribution NORMALE:
- 68% des données dans [μ - σ, μ + σ]
- 95% dans [μ - 2σ, μ + 2σ]
- 99.7% dans [μ - 3σ, μ + 3σ]
```

**Application**:
```
Solde moyen: 20K, écart-type: 8K

68% des clients ont solde entre:
20 - 8 = 12K et 20 + 8 = 28K

95% entre:
20 - 16 = 4K et 20 + 16 = 36K
```

#### Propriétés
✅ Même unité que données  
✅ Interprétation intuitive  
✅ Base de nombreux tests  
❌ Sensible aux outliers

---

### 3.4 Le Coefficient de Variation (CV)

#### Définition
**Écart-type relatif** (sans unité) permettant de comparer dispersions

#### Formule
```
CV = (s / x̄) × 100%
```

#### Interprétation
```
CV < 15%: Faible variabilité (données homogènes)
15% ≤ CV < 30%: Variabilité modérée
CV ≥ 30%: Forte variabilité (données hétérogènes)
```

#### Exemple Banking Comparatif

**Contexte**: Comparer variabilité entre produits

```
Comptes Épargne:
Moyenne = 15,000 HTG
Écart-type = 3,000 HTG
CV = (3,000/15,000) × 100% = 20%

Comptes Premium:
Moyenne = 150,000 HTG
Écart-type = 45,000 HTG
CV = (45,000/150,000) × 100% = 30%
```

**Interprétation**:
- En valeur absolue: Premium plus variable (45K vs 3K)
- En relatif: Premium plus variable AUSSI (30% vs 20%)
- Premium clientèle PLUS hétérogène

#### Quand Utiliser CV
- Comparer variabilités de variables **différentes unités**
- Comparer variabilités de variables **différentes échelles**
- Évaluer homogénéité d'un groupe

---

### 3.5 L'Intervalle Interquartile (IQR)

#### Définition
```
IQR = Q3 - Q1
```

**Mesure la dispersion de 50% CENTRAUX des données**

#### Propriétés
✅ **ROBUSTE** aux outliers  
✅ Approprié pour distributions asymétriques  
✅ Utilisé pour détecter outliers  
❌ Ignore 50% des données (extrêmes)

#### Exemple

```
Données ordonnées: 5, 8, 10, 12, 15, 18, 20, 25, 100

Q1 (25ème percentile) = 10
Q3 (75ème percentile) = 20

IQR = 20 - 10 = 10K HTG
```

**Interprétation**: 50% des clients centraux ont soldes variant de 10K HTG

---

## 4. MESURES DE POSITION

### 4.1 Quartiles

#### Définition
Divisent données ordonnées en 4 parties ÉGALES

```
Q1 (25%): 25% des données sont ≤ Q1
Q2 (50%): Médiane
Q3 (75%): 75% des données sont ≤ Q3
```

#### Calcul Positions
```
Q1: Position = 0.25 × (n+1)
Q2: Position = 0.50 × (n+1)
Q3: Position = 0.75 × (n+1)

Si position non entière → Interpoler
```

#### Exemple Banking

```
15 soldes ordonnés (en K): 5, 7, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 35, 40, 100

Position Q1 = 0.25 × 16 = 4 → Q1 = 10K
Position Q2 = 0.50 × 16 = 8 → Q2 = 20K
Position Q3 = 0.75 × 16 = 12 → Q3 = 30K
```

**Interprétation**:
- 25% clients ont ≤ 10K
- 50% clients ont ≤ 20K
- 75% clients ont ≤ 30K

---

### 4.2 Percentiles

#### Définition
Divisent données en 100 parties égales

```
Pₓ: x% des données sont ≤ Pₓ
```

#### Calcul Position
```
Position = (x/100) × (n+1)
```

#### Exemples Courants

```
P10 (10ème percentile): 10% en dessous
P90 (90ème percentile): 90% en dessous
P95, P99: Souvent utilisés pour outliers
```

#### Application Banking: Credit Scoring

```
Scores clients: 550 à 850

P10 = 600 → 10% clients ont score ≤ 600 (risque élevé)
P50 = 720 → Score médian
P90 = 810 → 10% clients ont score ≥ 810 (excellent)
```

**Segmentation**:
```
< P25: Segment Bronze
P25-P75: Segment Silver
> P75: Segment Gold
```

---

### 4.3 Déciles

#### Définition
Divisent données en 10 parties égales

```
D1, D2, ..., D9
Dₓ = P₁₀ₓ
```

#### Usage Banking
Segmentation client en 10 déciles de valeur

```
D10 (top 10%): Clients VIP
D1 (bottom 10%): Clients à risque
```

---

### 4.4 Five-Number Summary (Résumé à 5 Nombres)

#### Composants
```
1. Minimum
2. Q1 (25%)
3. Médiane (Q2, 50%)
4. Q3 (75%)
5. Maximum
```

#### Exemple Banking

```
Montants transactions:
Min = 100 HTG
Q1 = 500 HTG
Médiane = 1,500 HTG
Q3 = 5,000 HTG
Max = 50,000 HTG
```

**Utilité**: Base pour **Box Plot** (graphique en boîte)

---

## 5. MESURES DE FORME

### 5.1 Asymétrie (Skewness)

#### Définition
Mesure le **manque de symétrie** de la distribution

#### Formule
```
Skewness = [n / ((n-1)(n-2))] × Σ[(xᵢ-x̄)/s]³
```

#### Interprétation
```
Skewness = 0: Distribution SYMÉTRIQUE
Skewness > 0: Asymétrie DROITE (positive)
            → Queue allongée vers droite
            → Moyenne > Médiane
Skewness < 0: Asymétrie GAUCHE (négative)
            → Queue allongée vers gauche
            → Moyenne < Médiane
```

#### Seuils Pratiques
```
|Skew| < 0.5: Approximativement symétrique
0.5 ≤ |Skew| < 1: Modérément asymétrique
|Skew| ≥ 1: Fortement asymétrique
```

#### Exemple Banking

**Distribution Revenus Clients**:
```
Skewness = +2.3 (fortement asymétrique droite)

Interprétation:
- Majorité clients revenus moyens/faibles
- Quelques clients à TRÈS hauts revenus
- Queue longue vers droite
- Moyenne >> Médiane
```

**Impact**:
- Utiliser MÉDIANE (pas moyenne) pour décrire client "typique"
- Envisager transformation (ex: log) pour analyses
- Tests non-paramétriques possiblement plus appropriés

---

### 5.2 Aplatissement (Kurtosis)

#### Définition
Mesure **épaisseur des queues** et **pointu du pic** de la distribution

#### Formule
```
Kurtosis = [n(n+1) / ((n-1)(n-2)(n-3))] × Σ[(xᵢ-x̄)/s]⁴ - [3(n-1)² / ((n-2)(n-3))]
```

#### Interprétation
```
Kurtosis = 0: Normale (Mesokurtique)
Kurtosis > 0: Queues LOURDES (Leptokurtique)
            → Plus d'outliers que normal
            → Pic plus pointu
Kurtosis < 0: Queues LÉGÈRES (Platykurtique)
            → Moins d'outliers
            → Distribution plus plate
```

#### Seuils Pratiques
```
|Kurt| < 3: Distribution proche de normale
|Kurt| ≥ 3: Distribution avec queues lourdes
|Kurt| ≥ 10: Queues TRÈS lourdes (beaucoup d'extrêmes)
```

#### Exemple Banking

**Distribution Montants Transactions**:
```
Kurtosis = +8.5 (queues très lourdes)

Interprétation:
- Beaucoup de transactions "normales" (pic)
- MAIS aussi beaucoup de transactions EXTRÊMES
- Présence fréquente d'outliers
```

**Implications**:
- Risque opérationnel: Événements extrêmes fréquents
- Besoin de procédures spéciales pour gros montants
- Surveillance renforcée des transactions atypiques

---

### 5.3 Combinaison Skewness + Kurtosis

#### Patterns Typiques

```
Banking - Revenus:
Skew = +2, Kurt = +5
→ Asymétrique droite avec queues lourdes
→ Majorité revenus moyens, quelques TRÈS riches

Banking - Âge clients:
Skew ≈ 0, Kurt ≈ 0
→ Distribution relativement normale
→ Clientèle équilibrée par âge

Banking - Montants fraudes:
Skew = +3, Kurt = +15
→ Fortement asymétrique, queues TRÈS lourdes
→ Beaucoup petites fraudes, quelques ÉNORMES
```

---

## 6. VISUALISATIONS APPROPRIÉES

### 6.1 Tableau de Choix

| Type Variable | Type Graphique | Usage |
|---------------|----------------|-------|
| **Nominale** | Bar chart, Pie chart | Fréquences catégories |
| **Ordinale** | Bar chart ordonné | Respecter ordre |
| **Continue (1 var)** | Histogramme, Box plot, Density plot | Distribution |
| **Continue (2 var)** | Scatter plot | Relation |
| **Série temporelle** | Line chart | Évolution temps |
| **Comparaison groupes** | Box plots côte-à-côte | Comparer distributions |

---

### 6.2 Histogramme

#### Définition
Représente distribution d'une variable continue via **classes** (bins)

#### Éléments Clés
```
- Axe X: Classes (intervalles)
- Axe Y: Fréquences ou Densité
- Barres: Aire proportionnelle à fréquence
```

#### Choix Nombre de Classes

**Règle de Sturges**:
```
k = 1 + 3.322 × log₁₀(n)

Exemple: n = 100
k = 1 + 3.322 × 2 ≈ 7 classes
```

**Règle pratique**: √n ou entre 5-20 classes

#### Interprétation

**Symétrique**:
```
    /\
   /  \
  /    \
```
→ Distribution normale

**Asymétrique Droite**:
```
  /\___
 /     ---
```
→ Queue vers droite (revenus, prix)

**Bimodale**:
```
  /\    /\
 /  \  /  \
```
→ 2 populations distinctes

#### Exemple Banking

**Histogramme Soldes Comptes**:
```
Si asymétrique droite avec pic à 10-20K:
→ Majorité clients ont soldes faibles
→ Quelques clients hauts soldes (queue)
→ Utiliser MÉDIANE pour analyses
```

---

### 6.3 Box Plot (Boîte à Moustaches)

#### Structure
```
      Outliers (×)
         │
    ────┬──── Max (non-outlier)
        │
    ┌───┤
    │   │ Q3
    │   ├─── Médiane
    │   │
    │   │ Q1
    └───┤
        │
    ────┴──── Min (non-outlier)
         │
      Outliers (×)

Moustaches: 1.5 × IQR au-delà de Q1/Q3
```

#### Avantages
✅ Montre distribution ET outliers  
✅ Compact (facile comparer groupes)  
✅ Identifie asymétrie visuellement  
✅ Robuste

#### Interprétation

**Boîte longue**: Grande variabilité (IQR élevé)  
**Boîte courte**: Faible variabilité  
**Médiane décentrée**: Distribution asymétrique  
**Moustaches inégales**: Asymétrie

#### Exemple Banking

**Comparer Soldes: Premium vs Standard**

```
Premium: Médiane élevée, grande boîte, plusieurs outliers élevés
Standard: Médiane basse, petite boîte, peu outliers

→ Premium plus variable ET plus élevé
→ Segmentation justifiée
```

---

### 6.4 Scatter Plot (Nuage de Points)

#### Usage
Relation entre 2 variables CONTINUES

#### Patterns Typiques

**Corrélation Positive**:
```
        ×
      ×  ×
    ×  ×
  ×  ×
×  ×
```
→ Score ↑ → Montant prêt ↑

**Corrélation Négative**:
```
×  ×
  ×  ×
    ×  ×
      ×  ×
        ×
```
→ Taux défaut ↑ → Score ↓

**Aucune Corrélation**:
```
  ×   ×
×   ×   ×
  ×   ×
    ×   ×
```
→ Variables indépendantes

**Non-linéaire**:
```
    ×××
  ××   ××
××       ××
```
→ Relation courbe (ex: rendement vs risque)

---

## 7. DÉTECTION D'OUTLIERS

### 7.1 Définition

**Outlier**: Valeur **anormalement éloignée** des autres observations

#### Types
```
- Outlier Univarié: Extrême sur UNE variable
- Outlier Multivarié: Combinaison anormale de plusieurs variables
```

---

### 7.2 Méthode IQR (Recommandée)

#### Règle
```
Outlier si:
x < Q1 - 1.5×IQR  OU  x > Q3 + 1.5×IQR

Outlier extrême si:
x < Q1 - 3×IQR  OU  x > Q3 + 3×IQR
```

#### Exemple Banking

```
Soldes (K HTG): 5, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 100

Q1 = 11, Q3 = 26.5, IQR = 15.5

Borne inférieure = 11 - 1.5×15.5 = -12.25 (pas de problème)
Borne supérieure = 26.5 + 1.5×15.5 = 49.75

100 > 49.75 → OUTLIER détecté!
```

---

### 7.3 Méthode Z-Score

#### Principe
Mesure combien d'écarts-types un point est éloigné de la moyenne

#### Formule
```
Z = (x - x̄) / s
```

#### Règle
```
|Z| > 3: Outlier probable
|Z| > 2: À surveiller
```

#### Exemple

```
Montant = 150K, Moyenne = 20K, Écart-type = 15K

Z = (150 - 20) / 15 = 8.67

|Z| = 8.67 >> 3 → OUTLIER CLAIR
```

---

### 7.4 Gestion des Outliers

#### Options

| Action | Quand | Impact |
|--------|-------|--------|
| **Garder** | Valeur légitime et importante | Aucun |
| **Transformer** | Log, sqrt pour réduire influence | Réduit asymétrie |
| **Cap/Floor** | Remplacer par seuil (ex: P95) | Modéré |
| **Supprimer** | Erreur de mesure confirmée | Forte perte info |
| **Analyser séparément** | Segment distinct | Analyse approfondie |

#### Règle d'Or
**TOUJOURS investiguer AVANT de supprimer!**

#### Exemple Banking

**Outlier: Solde 10M HTG**

**Investigation**:
1. Erreur saisie? Non, transaction confirmée
2. Fraude? Non, client VIP vérifié
3. Compte entreprise? OUI!

**Action**: Analyser SÉPARÉMENT comptes particuliers vs entreprises

---

## 8. SCÉNARIOS BANKING COMPLETS

### Scénario 1: Analyse Soldes Comptes Épargne

**Données** (n=1000):
```
Moyenne: 25,000 HTG
Médiane: 18,000 HTG
Mode: 15,000 HTG
Écart-type: 30,000 HTG
Q1: 10,000 HTG
Q3: 30,000 HTG
Min: 500 HTG
Max: 500,000 HTG
Skewness: +2.8
Kurtosis: +12.5
```

**Analyse Complète**:

1. **Tendance Centrale**:
```
Moyenne (25K) >> Médiane (18K)
→ Distribution ASYMÉTRIQUE DROITE
→ Utiliser MÉDIANE (18K) pour client "typique"
```

2. **Dispersion**:
```
CV = 30K / 25K = 120% (TRÈS élevé!)
→ Clientèle TRÈS hétérogène
→ Segmentation nécessaire

IQR = 30K - 10K = 20K
→ 50% centraux varient de 20K
```

3. **Forme**:
```
Skew = +2.8 (fortement asymétrique)
→ Queue longue vers droite
→ Quelques clients à très hauts soldes

Kurt = +12.5 (queues très lourdes)
→ Beaucoup d'outliers élevés
→ Événements extrêmes fréquents
```

4. **Outliers** (Méthode IQR):
```
Borne sup = 30K + 1.5×20K = 60K
Max = 500K >> 60K
→ Nombreux outliers au-dessus de 60K
```

**Conclusions Business**:
- Clientèle biaisée vers soldes FAIBLES
- Petite minorité avec soldes TRÈS ÉLEVÉS
- Créer segments: Standard (<30K), Premium (30-100K), VIP (>100K)
- Offres différenciées par segment
- Client médian (18K) cible pour produits de masse

---

### Scénario 2: Comparaison Performance Agences

**Contexte**: Comparer transactions moyennes entre 3 agences

**Données**:
```
Agence Nord (n=200):
Moyenne = 850 HTG, Médiane = 800 HTG
Écart-type = 300 HTG, CV = 35%

Agence Sud (n=200):
Moyenne = 1,200 HTG, Médiane = 1,150 HTG
Écart-type = 400 HTG, CV = 33%

Agence Est (n=200):
Moyenne = 750 HTG, Médiane = 700 HTG
Écart-type = 250 HTG, CV = 33%
```

**Analyse**:

1. **Tendance Centrale**:
```
Sud (1,200) > Nord (850) > Est (750)
→ Sud performe le MIEUX
→ Est à améliorer
```

2. **Variabilité**:
```
CV similaires (33-35%)
→ Hétérogénéité comparable
→ Variabilité relative similaire

Écart-type absolu: Sud (400) > Nord (300) > Est (250)
→ Sud plus variable en valeur absolue (montants plus élevés)
```

3. **Symétrie**:
```
Toutes: Moyenne ≈ Médiane
→ Distributions approximativement symétriques
→ Moyennes utilisables
```

**Recommandations**:
- Étudier POURQUOI Sud performe mieux (clientèle? agents? localisation?)
- Appliquer best practices Sud aux autres agences
- Fixer objectifs: Nord à 1,000 HTG, Est à 900 HTG
- CV similaires → Processus homogènes (bon signe)

---

### Scénario 3: Profiling Client pour Segmentation

**Objectif**: Segmenter clients selon comportement transactionnel

**Variables Analysées**:
```
1. Nb transactions/mois
2. Montant moyen transaction
3. Solde compte
4. Ancienneté (mois)
```

**Statistiques Descriptives**:

| Variable | Moyenne | Médiane | Écart-type | CV | Min | Max |
|----------|---------|---------|------------|----|----|-----|
| Nb Trans | 8 | 6 | 5 | 63% | 0 | 50 |
| Montant  | 1,500 | 1,000 | 1,200 | 80% | 50 | 20,000 |
| Solde    | 25,000 | 15,000 | 30,000 | 120% | 100 | 500,000 |
| Ancienneté | 24 | 18 | 20 | 83% | 1 | 120 |

**Analyse**:

1. **Nb Transactions**:
```
Médiane (6) < Moyenne (8)
→ Asymétrie droite
→ Majorité clients peu actifs (≤6 trans/mois)
→ Quelques très actifs (up to 50)

Segmentation:
- Faible: <3 trans/mois (25% - bottom quartile)
- Moyen: 3-12 trans/mois (50% - middle)
- Élevé: >12 trans/mois (25% - top quartile)
```

2. **Montant**:
```
CV = 80% (très hétérogène)
Asymétrique droite (médiane < moyenne)
→ Beaucoup petites transactions
→ Quelques grosses transactions

Segmentation par montant:
- Micro: <500 HTG
- Standard: 500-2,000 HTG
- Large: >2,000 HTG
```

3. **Solde**:
```
CV = 120% (EXTRÊMEMENT hétérogène)
Médiane (15K) << Moyenne (25K)
→ Distribution très asymétrique
→ Majorité soldes faibles
→ Petite minorité soldes élevés

Segmentation:
- Bronze: <10K (Q1)
- Silver: 10-30K (Q1-Q3)
- Gold: 30-100K
- Platinum: >100K
```

**Stratégie Finale**:
Créer matrice 3D: Activité × Montant × Solde
→ Identifier segments clés (ex: Actifs + Gros montants + Solde élevé = VIP)

---

## RÉSUMÉ EXÉCUTIF

### Formules Essentielles

```
Moyenne: x̄ = Σx / n
Variance: s² = Σ(x-x̄)² / (n-1)
Écart-type: s = √s²
CV: (s/x̄) × 100%
IQR: Q3 - Q1
Outlier: < Q1-1.5×IQR OU > Q3+1.5×IQR
Z-score: (x-x̄) / s
```

### Règles de Décision

```
Type Variable → Statistique:
- Nominale → Mode
- Ordinale → Médiane
- Continue + Symétrique + Sans outliers → Moyenne
- Continue + Asymétrique OU Outliers → Médiane

Distribution:
- Moyenne ≈ Médiane → Symétrique
- Moyenne > Médiane → Asymétrique droite
- Moyenne < Médiane → Asymétrique gauche

Variabilité:
- CV < 15%: Faible
- 15-30%: Modérée
- > 30%: Forte (hétérogène)
```

### Checklist Analyse Descriptive

☐ Identifier type de variables  
☐ Calculer tendance centrale (choisir appropriée)  
☐ Calculer dispersion (au moins écart-type ET IQR)  
☐ Vérifier asymétrie et kurtosis  
☐ Détecter outliers (IQR + investigation)  
☐ Créer visualisations appropriées  
☐ Interpréter dans contexte BUSINESS  
☐ Proposer ACTIONS concrètes

---

**PRÊT POUR L'EXAMEN! 💪🚀**
