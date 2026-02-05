# Manuel de Préparation: Indicateurs et Indices

## Introduction

Les indicateurs et indices sont des mesures synthétiques qui permettent de résumer, comparer et suivre des phénomènes complexes. Dans le contexte bancaire, ils sont essentiels pour la prise de décision, le reporting réglementaire et la communication avec les stakeholders.

---

## Partie 1: Théorie des Indicateurs

### 1.1 Définitions Fondamentales

#### Indicateur
**Définition:** Une mesure quantitative ou qualitative qui fournit des informations sur l'état, l'évolution ou la performance d'un phénomène.

**Caractéristiques d'un bon indicateur (SMART):**
- **S**pécifique: Mesure un aspect précis
- **M**esurable: Quantifiable objectivement
- **A**tteignable: Réaliste à collecter
- **R**elevant: Pertinent pour l'objectif
- **T**emporel: Défini dans le temps

#### Indice
**Définition:** Un indicateur composite qui synthétise plusieurs mesures en une seule valeur, souvent exprimée en base 100 ou en pourcentage.

**Différence clé:**
```
Indicateur = mesure simple (ex: nombre de clients)
Indice = mesure composite (ex: indice de satisfaction combinant plusieurs critères)
```

---

### 1.2 Taxonomie des Indicateurs

#### Par Nature

| Type | Description | Exemples Bancaires |
|------|-------------|-------------------|
| **Quantitatif** | Valeurs numériques | Solde moyen, nombre de transactions |
| **Qualitatif** | Catégories ou scores | Rating de crédit (AAA, BB) |
| **Absolu** | Valeur brute | Total des dépôts: 10M HTG |
| **Relatif** | Ratio ou pourcentage | NPL ratio: 5% |
| **Stock** | À un instant T | Encours de crédit au 31/12 |
| **Flux** | Sur une période | Nouveaux prêts du trimestre |

#### Par Fonction

| Type | Description | Exemples |
|------|-------------|----------|
| **Descriptif** | État actuel | Nombre de clients actifs |
| **Diagnostic** | Cause d'une situation | Taux de churn par segment |
| **Prédictif** | Projection future | Probabilité de défaut |
| **Prescriptif** | Action recommandée | Score de propension |

#### Par Temporalité

| Type | Description | Usage |
|------|-------------|-------|
| **Leading** | Précède le résultat | Demandes de crédit (prédit l'activité future) |
| **Lagging** | Résultat passé | Taux de défaut réalisé |
| **Coincident** | Simultané | Transactions en cours |

---

### 1.3 Construction d'un Indicateur

#### Étapes de Création

```
1. Définir l'objectif
   ↓
2. Identifier les données sources
   ↓
3. Définir la formule de calcul
   ↓
4. Établir la fréquence de mise à jour
   ↓
5. Définir les seuils et alertes
   ↓
6. Documenter les métadonnées
```

#### Fiche d'Identité d'un Indicateur

```markdown
## Indicateur: Taux de NPL (Non-Performing Loans)

**Définition:** Proportion des prêts en défaut par rapport au portefeuille total
**Formule:** (Encours NPL / Encours Total des Prêts) × 100
**Unité:** Pourcentage
**Fréquence:** Mensuelle
**Source:** Système central de prêts
**Responsable:** Direction des Risques
**Seuils:**
  - Vert: < 3%
  - Orange: 3% - 5%
  - Rouge: > 5%
**Historique:** Depuis janvier 2020
**Limites:** Ne capture pas les prêts restructurés
```

---

## Partie 2: Types d'Indices

### 2.1 Indices Simples

#### Indice Élémentaire
Rapport entre deux valeurs de la même grandeur à deux moments différents.

**Formule:**
```
I(t/0) = (V_t / V_0) × 100
```

**Exemple:**
```
Dépôts 2023: 150M HTG
Dépôts 2020 (base): 100M HTG
Indice = (150/100) × 100 = 150

Interprétation: Les dépôts ont augmenté de 50% par rapport à 2020
```

#### Taux de Variation
```
Taux = ((V_t - V_0) / V_0) × 100

Exemple:
Taux = ((150 - 100) / 100) × 100 = 50%
```

---

### 2.2 Indices Synthétiques (Composites)

#### Indice de Laspeyres
Pondéré par les quantités de la période de base.

**Formule:**
```
I_L = (Σ p_t × q_0) / (Σ p_0 × q_0) × 100
```

**Usage:** Indice des prix à la consommation (IPC)

#### Indice de Paasche
Pondéré par les quantités de la période courante.

**Formule:**
```
I_P = (Σ p_t × q_t) / (Σ p_0 × q_t) × 100
```

#### Indice de Fisher
Moyenne géométrique de Laspeyres et Paasche.

**Formule:**
```
I_F = √(I_L × I_P)
```

**Avantage:** Élimine les biais des deux méthodes

---

### 2.3 Indices Financiers et Bancaires

#### Indices de Performance

| Indice | Formule | Interprétation |
|--------|---------|----------------|
| **ROA** | Résultat Net / Actif Total | Rentabilité des actifs |
| **ROE** | Résultat Net / Capitaux Propres | Rentabilité des fonds propres |
| **NIM** | (Revenus - Charges intérêts) / Actifs productifs | Marge d'intermédiation |
| **CIR** | Charges d'exploitation / PNB | Efficacité opérationnelle |

#### Indices de Risque

| Indice | Formule | Seuil Typique |
|--------|---------|---------------|
| **NPL Ratio** | NPL / Total Prêts | < 5% |
| **Coverage Ratio** | Provisions / NPL | > 100% |
| **CAR** | Capital / RWA | > 8% (Bâle) |
| **LCR** | Actifs liquides / Sorties nettes 30j | > 100% |

#### Indices de Liquidité

| Indice | Formule | Objectif |
|--------|---------|----------|
| **Loan-to-Deposit** | Prêts / Dépôts | 80-90% |
| **Quick Ratio** | (Actif circulant - Stock) / Passif circulant | > 1 |
| **Cash Ratio** | Trésorerie / Passif circulant | > 0.2 |

---

## Partie 3: Application Pratique

### 3.1 KPIs Bancaires Essentiels

#### Catégorie: Rentabilité

```python
# Calcul du ROE
def calculate_roe(net_income, equity):
    """Return on Equity"""
    return (net_income / equity) * 100

# Calcul du ROA
def calculate_roa(net_income, total_assets):
    """Return on Assets"""
    return (net_income / total_assets) * 100

# Net Interest Margin
def calculate_nim(interest_income, interest_expense, earning_assets):
    """Net Interest Margin"""
    return ((interest_income - interest_expense) / earning_assets) * 100
```

#### Catégorie: Qualité des Actifs

```python
# NPL Ratio
def calculate_npl_ratio(npl_amount, total_loans):
    """Non-Performing Loans Ratio"""
    return (npl_amount / total_loans) * 100

# Provision Coverage
def calculate_coverage(provisions, npl_amount):
    """Provision Coverage Ratio"""
    return (provisions / npl_amount) * 100

# Write-off Rate
def calculate_writeoff_rate(writeoffs, avg_loans):
    """Net Charge-off Rate"""
    return (writeoffs / avg_loans) * 100
```

#### Catégorie: Efficacité

```python
# Cost-to-Income Ratio
def calculate_cir(operating_expenses, operating_income):
    """Cost-to-Income Ratio"""
    return (operating_expenses / operating_income) * 100

# Assets per Employee
def calculate_assets_per_employee(total_assets, num_employees):
    """Productivity measure"""
    return total_assets / num_employees
```

---

### 3.2 Indices Composites Personnalisés

#### Création d'un Indice de Santé Client

```python
import pandas as pd
import numpy as np

def calculate_customer_health_index(df):
    """
    Indice composite de santé client
    Composantes:
    - Activité: 30%
    - Rentabilité: 25%
    - Ancienneté: 20%
    - Multi-équipement: 15%
    - Satisfaction: 10%
    """
    
    # Normalisation des composantes (0-100)
    df['activity_score'] = normalize(df['nb_transactions_mensuel'], 0, 50)
    df['profitability_score'] = normalize(df['marge_client'], 0, 10000)
    df['tenure_score'] = normalize(df['anciennete_mois'], 0, 120)
    df['products_score'] = normalize(df['nb_produits'], 1, 5)
    df['satisfaction_score'] = df['nps_score']  # déjà 0-100
    
    # Calcul de l'indice pondéré
    df['health_index'] = (
        df['activity_score'] * 0.30 +
        df['profitability_score'] * 0.25 +
        df['tenure_score'] * 0.20 +
        df['products_score'] * 0.15 +
        df['satisfaction_score'] * 0.10
    )
    
    return df

def normalize(series, min_val, max_val):
    """Normalise une série entre 0 et 100"""
    return ((series.clip(min_val, max_val) - min_val) / (max_val - min_val)) * 100
```

#### Création d'un Indice de Risque de Crédit

```python
def calculate_credit_risk_index(df):
    """
    Indice de risque de crédit composite
    Plus le score est élevé, plus le risque est élevé
    """
    
    # Composantes (normalisées 0-100, où 100 = risque max)
    df['dti_risk'] = normalize_risk(df['debt_to_income'], 0, 0.5)
    df['utilization_risk'] = normalize_risk(df['credit_utilization'], 0, 1)
    df['delinquency_risk'] = df['nb_retards_12m'] * 20  # 5 retards = 100
    df['tenure_risk'] = 100 - normalize(df['anciennete_emploi_mois'], 0, 60)
    
    # Score inverse de crédit (mauvais score = haut risque)
    df['score_risk'] = 100 - normalize(df['score_credit'], 300, 850)
    
    # Indice composite
    weights = {
        'dti_risk': 0.25,
        'utilization_risk': 0.20,
        'delinquency_risk': 0.25,
        'tenure_risk': 0.10,
        'score_risk': 0.20
    }
    
    df['risk_index'] = sum(df[k] * v for k, v in weights.items())
    
    # Classification
    df['risk_category'] = pd.cut(
        df['risk_index'],
        bins=[0, 25, 50, 75, 100],
        labels=['Faible', 'Modéré', 'Élevé', 'Très élevé']
    )
    
    return df
```

---

### 3.3 Analyse Temporelle des Indices

#### Calcul des Variations

```python
def analyze_index_evolution(df, index_col, date_col):
    """Analyse l'évolution d'un indice"""
    
    df = df.sort_values(date_col)
    
    # Variation absolue
    df['variation_abs'] = df[index_col].diff()
    
    # Variation relative (%)
    df['variation_pct'] = df[index_col].pct_change() * 100
    
    # Moyenne mobile
    df['ma_3'] = df[index_col].rolling(window=3).mean()
    df['ma_6'] = df[index_col].rolling(window=6).mean()
    
    # Tendance (régression linéaire)
    from scipy import stats
    x = np.arange(len(df))
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, df[index_col])
    df['trend'] = intercept + slope * x
    
    return df, slope
```

#### Décomposition Saisonnière

```python
from statsmodels.tsa.seasonal import seasonal_decompose

def decompose_index(series, period=12):
    """Décompose un indice en trend, saisonnalité et résidu"""
    
    result = seasonal_decompose(series, model='additive', period=period)
    
    return {
        'trend': result.trend,
        'seasonal': result.seasonal,
        'residual': result.resid,
        'observed': result.observed
    }
```

---

## Partie 4: Indicateurs Spécifiques au Contexte Bancaire Haïtien

### 4.1 Indicateurs Réglementaires BRH

| Indicateur | Définition | Seuil Réglementaire |
|------------|------------|---------------------|
| **Ratio de Solvabilité** | Fonds propres / Actifs pondérés | ≥ 12% |
| **Ratio de Liquidité** | Actifs liquides / Dépôts à vue | ≥ 20% |
| **Ratio des Prêts** | Prêts / Total Actifs | Plafond variable |
| **Concentration Risque** | Exposition max / Fonds propres | ≤ 15% |

### 4.2 Indicateurs de Performance Locale

```python
# Indicateurs spécifiques marché haïtien
def calculate_haiti_specific_kpis(df):
    """KPIs adaptés au contexte haïtien"""
    
    kpis = {}
    
    # Part de marché (estimation)
    kpis['market_share'] = df['total_deposits'] / TOTAL_MARKET_DEPOSITS * 100
    
    # Pénétration digitale
    kpis['digital_penetration'] = df['digital_users'] / df['total_clients'] * 100
    
    # Ratio HTG/USD (gestion du risque de change)
    kpis['currency_mix'] = df['deposits_htg'] / df['total_deposits'] * 100
    
    # Concentration géographique (Port-au-Prince vs provinces)
    kpis['pap_concentration'] = df['deposits_pap'] / df['total_deposits'] * 100
    
    # Taux d'inclusion (clients nouveaux au système)
    kpis['financial_inclusion'] = df['first_time_banked'] / df['new_clients'] * 100
    
    return kpis
```

### 4.3 Indicateurs de Risque Pays

| Indicateur | Description | Impact sur la Banque |
|------------|-------------|---------------------|
| **Inflation** | Variation des prix | Érosion des marges réelles |
| **Taux de change HTG/USD** | Dépréciation | Risque sur prêts en devise |
| **PIB** | Croissance économique | Qualité du portefeuille |
| **Taux directeur BRH** | Politique monétaire | Coût des ressources |

---

## Partie 5: Visualisation et Reporting

### 5.1 Dashboards d'Indicateurs

#### Structure Recommandée

```
┌──────────────────────────────────────────────────────────┐
│  DASHBOARD EXÉCUTIF - INDICATEURS CLÉS                   │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐            │
│  │ ROE    │ │ NPL    │ │ CIR    │ │ CAR    │            │
│  │ 15.2%  │ │ 4.1%   │ │ 52%    │ │ 14.5%  │  ← KPIs   │
│  │   ▲    │ │   ▼    │ │   ▼    │ │   ▲    │            │
│  └────────┘ └────────┘ └────────┘ └────────┘            │
│                                                          │
│  ┌─────────────────────────────────────────────────┐    │
│  │                                                  │    │
│  │  [Graphique: Évolution des KPIs - 12 mois]     │    │
│  │                                                  │    │
│  └─────────────────────────────────────────────────┘    │
│                                                          │
│  ┌───────────────────┐  ┌──────────────────────────┐    │
│  │ Répartition       │  │ Comparaison vs Objectifs │    │
│  │ [Pie chart]       │  │ [Bullet charts]          │    │
│  └───────────────────┘  └──────────────────────────┘    │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### 5.2 Système d'Alertes

```python
def check_kpi_alerts(kpis, thresholds):
    """Vérifie les indicateurs contre les seuils"""
    
    alerts = []
    
    for kpi_name, value in kpis.items():
        threshold = thresholds.get(kpi_name)
        if threshold:
            if threshold['type'] == 'max' and value > threshold['red']:
                alerts.append({
                    'kpi': kpi_name,
                    'value': value,
                    'threshold': threshold['red'],
                    'severity': 'CRITICAL'
                })
            elif threshold['type'] == 'min' and value < threshold['red']:
                alerts.append({
                    'kpi': kpi_name,
                    'value': value,
                    'threshold': threshold['red'],
                    'severity': 'CRITICAL'
                })
    
    return alerts

# Exemple de configuration des seuils
thresholds = {
    'npl_ratio': {'type': 'max', 'green': 3, 'orange': 5, 'red': 7},
    'car': {'type': 'min', 'green': 15, 'orange': 12, 'red': 10},
    'roe': {'type': 'min', 'green': 15, 'orange': 10, 'red': 5}
}
```

---

## Partie 6: Bonnes Pratiques

### 6.1 Principes de Gestion des Indicateurs

1. **Moins c'est plus:** 5-7 KPIs principaux maximum
2. **Cohérence:** Mêmes définitions dans toute l'organisation
3. **Actualité:** Mise à jour régulière et fiable
4. **Contextualisation:** Toujours comparer (période, objectif, marché)
5. **Action:** Chaque indicateur doit mener à une décision

### 6.2 Erreurs à Éviter

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Trop d'indicateurs | Confusion, paralysie | Prioriser les KPIs critiques |
| Indicateurs non alignés | Efforts dispersés | Lier aux objectifs stratégiques |
| Données non fiables | Mauvaises décisions | Validation et audit réguliers |
| Pas de benchmark | Interprétation difficile | Comparer au marché/historique |
| Indicateurs manipulables | Comportements pervers | Utiliser des indicateurs équilibrés |

### 6.3 Gouvernance des Indicateurs

```markdown
## Politique de Gouvernance des KPIs

### Rôles et Responsabilités
- **Data Owner:** Valide la qualité des données sources
- **Méthodologue:** Définit et documente les formules
- **IT:** Assure la collecte et le calcul automatisé
- **Business:** Utilise et interprète les indicateurs

### Cycle de Vie
1. Création: Validation par comité
2. Production: Calcul et diffusion réguliers
3. Révision: Annuelle ou sur changement business
4. Décommissionnement: Procédure formelle

### Documentation Obligatoire
- Fiche d'identité de l'indicateur
- Règles de calcul détaillées
- Sources de données
- Historique des modifications
```

---

## Questions d'Entretien Fréquentes

1. **Quelle est la différence entre un indicateur et un indice?**
   → Indicateur = mesure simple; Indice = mesure composite de plusieurs indicateurs

2. **Qu'est-ce qu'un leading indicator vs lagging indicator?**
   → Leading prédit l'avenir (demandes de crédit); Lagging mesure le passé (défauts réalisés)

3. **Comment créeriez-vous un indice de satisfaction client?**
   → Combiner plusieurs mesures (NPS, plaintes, rétention) avec des pondérations

4. **Quels KPIs sont essentiels pour une banque commerciale?**
   → ROE, ROA, NPL ratio, CAR, CIR, NIM

5. **Comment valider qu'un indicateur est pertinent?**
   → SMART + corrélation avec les résultats business + actionnable

---

## Résumé

### Points Clés sur les Indicateurs
- Un bon indicateur est SMART
- Distinguer stock (instant T) vs flux (période)
- Leading indicators pour anticiper, lagging pour mesurer

### Points Clés sur les Indices
- Permettent de synthétiser plusieurs mesures
- Choix de la pondération est critique
- Base 100 facilite la comparaison temporelle

### Application Bancaire
- KPIs de rentabilité: ROE, ROA, NIM
- KPIs de risque: NPL, CAR, Coverage
- KPIs d'efficacité: CIR, productivité
- Toujours contextualiser avec benchmarks

---

**Rappel final:** Les indicateurs ne sont utiles que s'ils mènent à des actions. Un indicateur sans décision associée est inutile.
