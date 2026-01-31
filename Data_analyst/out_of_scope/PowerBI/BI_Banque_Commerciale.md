# Business Intelligence pour Banques Commerciales

## Guide Complet - Contexte UniBank Haiti

---

## Partie 1: Vue d'Ensemble BI Bancaire

### 1.1 Rôle de la BI dans une Banque

```
┌─────────────────────────────────────────────────────────────┐
│                    DÉCISIONS STRATÉGIQUES                   │
│  Expansion │ Produits │ Tarification │ Risque │ Conformité │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐    ┌──────────────┐    ┌─────────────┐   │
│   │  REPORTING  │    │  ANALYTICS   │    │  PRÉDICTIF  │   │
│   │   (Quoi?)   │    │ (Pourquoi?)  │    │  (Quand?)   │   │
│   └─────────────┘    └──────────────┘    └─────────────┘   │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                     DATA WAREHOUSE                          │
│  Données intégrées, historisées, nettoyées                 │
├─────────────────────────────────────────────────────────────┤
│                    SOURCES DE DONNÉES                       │
│  Core Banking │ Canaux │ CRM │ Risque │ Externe │ Régul.   │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Domaines Analytiques Bancaires

| Domaine | Objectifs | KPIs Clés |
|---------|-----------|-----------|
| **Finance** | Rentabilité, performance | ROE, ROA, NIM, CIR |
| **Risque** | Gestion crédit, liquidité | NPL, CAR, LCR |
| **Commercial** | Ventes, acquisition | Cross-sell, CAC, LTV |
| **Client** | Satisfaction, rétention | NPS, Churn, CLV |
| **Opérations** | Efficacité, qualité | SLA, temps traitement |
| **Conformité** | Réglementation | Ratios BRH, AML alerts |

---

## Partie 2: Métriques Bancaires Détaillées

### 2.1 Indicateurs de Rentabilité

#### Return on Equity (ROE)
```
ROE = (Résultat Net / Capitaux Propres Moyens) × 100

Décomposition DuPont:
ROE = (Résultat/PNB) × (PNB/Actifs) × (Actifs/Capitaux Propres)
    = Marge Nette × Rotation Actifs × Levier

Benchmark bancaire: 12-18%
Interprétation: Rendement pour les actionnaires
```

#### Return on Assets (ROA)
```
ROA = (Résultat Net / Total Actifs Moyens) × 100

Benchmark: 1-2%
Interprétation: Efficacité de l'utilisation des actifs
```

#### Net Interest Margin (NIM)
```
NIM = (Revenus d'Intérêts - Charges d'Intérêts) / Actifs Productifs Moyens × 100

Revenus d'intérêts: Intérêts sur prêts, placements
Charges d'intérêts: Intérêts sur dépôts, emprunts
Actifs productifs: Prêts + Placements

Benchmark: 3-5%
```

#### Cost-to-Income Ratio (CIR)
```
CIR = (Charges d'Exploitation / Produit Net Bancaire) × 100

Charges: Personnel, loyers, IT, marketing
PNB: NIM + Commissions + Autres revenus

Benchmark: 45-55% (plus bas = plus efficace)
```

#### Produit Net Bancaire (PNB)
```
PNB = Marge d'Intérêts + Commissions Nettes + Autres Revenus

Décomposition:
- Marge d'intérêts: 60-70%
- Commissions: 20-30%
- Autres: 5-10%
```

### 2.2 Indicateurs de Qualité des Actifs

#### NPL Ratio (Non-Performing Loans)
```
NPL Ratio = (Encours NPL / Total Encours Prêts) × 100

Définition NPL:
- Retard > 90 jours, ou
- Probabilité de non-remboursement élevée

Classification standard:
- Performing (0-30 jours)
- Watch (31-60 jours)
- Substandard (61-90 jours)
- Doubtful (91-180 jours)
- Loss (>180 jours)

Benchmark: < 5%
```

#### Provision Coverage Ratio
```
Coverage = (Provisions Totales / Encours NPL) × 100

Provisions:
- Spécifiques: Pour prêts identifiés
- Générales: Pour risque inhérent

Benchmark: > 100%
Interprétation: Capacité à absorber les pertes
```

#### Cost of Risk
```
CoR = (Dotations aux Provisions / Encours Moyen) × 100

Interprétation: Coût annualisé du risque de crédit
Benchmark: 1-3%
```

### 2.3 Indicateurs de Liquidité

#### Loan-to-Deposit Ratio (LDR)
```
LDR = (Total Prêts / Total Dépôts) × 100

Optimal: 80-90%
< 80%: Sous-utilisation des ressources
> 100%: Dépendance au financement de marché
```

#### Liquidity Coverage Ratio (LCR) - Bâle III
```
LCR = (HQLA / Sorties Nettes 30 jours) × 100

HQLA: High Quality Liquid Assets (cash, titres d'État)
Sorties nettes: Estimées sur scénario de stress

Exigence: ≥ 100%
```

#### Net Stable Funding Ratio (NSFR)
```
NSFR = (ASF / RSF) × 100

ASF: Available Stable Funding (sources stables)
RSF: Required Stable Funding (besoins)

Exigence: ≥ 100%
```

### 2.4 Indicateurs de Capital (Solvabilité)

#### Capital Adequacy Ratio (CAR)
```
CAR = (Fonds Propres Réglementaires / RWA) × 100

Fonds propres:
- Tier 1: Capital de base (actions, réserves)
- Tier 2: Capital complémentaire (dettes subordonnées)

RWA: Risk-Weighted Assets

Exigence BRH: ≥ 12%
Exigence Bâle III: ≥ 8% (+ buffers)
```

#### Tier 1 Ratio
```
Tier 1 = (Capital Tier 1 / RWA) × 100

Exigence: ≥ 6%
```

#### Leverage Ratio
```
Leverage = (Tier 1 / Total Expositions) × 100

Non pondéré par le risque
Exigence: ≥ 3%
```

---

## Partie 3: Dashboards Bancaires

### 3.1 Dashboard Exécutif (Direction Générale)

```
┌────────────────────────────────────────────────────────────────┐
│         TABLEAU DE BORD DIRECTION - UniBank Haiti             │
│                    Janvier 2025                               │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐  │
│  │  PNB   │  │  ROE   │  │  NPL   │  │  CAR   │  │  CIR   │  │
│  │ 245M   │  │ 14.2%  │  │ 4.1%   │  │ 15.2%  │  │ 52%    │  │
│  │  ▲+8%  │  │  ▲+1.2 │  │  ▼-0.3 │  │  ▲+0.5 │  │  ▼-2   │  │
│  └────────┘  └────────┘  └────────┘  └────────┘  └────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │      Évolution PNB et Résultat Net (12 mois)            │ │
│  │  [LINE CHART: PNB vs Résultat avec trend]               │ │
│  └──────────────────────────────────────────────────────────┘ │
│                                                                │
│  ┌─────────────────────────┐ ┌────────────────────────────┐  │
│  │  Structure PNB         │ │  Performance Agences       │  │
│  │  [PIE: NII/Fees/Other] │ │  [BAR: par agence]         │  │
│  └─────────────────────────┘ └────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Alertes                                                 │ │
│  │  ⚠️ NPL ratio proche du seuil (4.1% vs 5%)              │ │
│  │  ✅ CAR confortable (15.2% vs 12%)                       │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

### 3.2 Dashboard Risque de Crédit

```
┌────────────────────────────────────────────────────────────────┐
│              TABLEAU DE BORD RISQUE DE CRÉDIT                 │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Portefeuille Total: 5.2 Mrd HTG   |   NPL: 213M HTG (4.1%)  │
│                                                                │
│  ┌────────────────────────────────────────────────────────┐   │
│  │  Classification du Portefeuille                        │   │
│  │  ████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░   │   │
│  │  Performing 85%  | Watch 7%  | Substandard 4% | Loss 4%│   │
│  └────────────────────────────────────────────────────────┘   │
│                                                                │
│  ┌────────────────────────┐  ┌────────────────────────────┐  │
│  │  NPL par Secteur      │  │  Vintage Analysis          │  │
│  │  Agriculture: 6.2%    │  │  [HEATMAP: cohorte/mois]   │  │
│  │  Commerce: 3.8%       │  │                            │  │
│  │  Services: 2.9%       │  │                            │  │
│  └────────────────────────┘  └────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Top 10 Expositions                                      │ │
│  │  Client A: 150M (2.9%) | Client B: 120M (2.3%) | ...    │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

### 3.3 Dashboard Commercial

```
┌────────────────────────────────────────────────────────────────┐
│              TABLEAU DE BORD COMMERCIAL                        │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  Nouveaux clients: 1,234  |  Attrition: 2.1%  |  NPS: +45    │
│                                                                │
│  ┌────────────────────────┐  ┌────────────────────────────┐  │
│  │  Pipeline Crédit      │  │  Cross-sell Ratio          │  │
│  │  Demandes: 500        │  │  Actuel: 2.3 prod/client   │  │
│  │  Approuvées: 350      │  │  Objectif: 3.0             │  │
│  │  Décaissées: 280      │  │  [GAUGE CHART]             │  │
│  │  [FUNNEL CHART]       │  │                            │  │
│  └────────────────────────┘  └────────────────────────────┘  │
│                                                                │
│  ┌──────────────────────────────────────────────────────────┐ │
│  │  Performance par Agent de Crédit                         │ │
│  │  [RANKING TABLE: agent, decaissements, NPL]             │ │
│  └──────────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────────┘
```

---

## Partie 4: Reporting Réglementaire

### 4.1 Exigences BRH (Banque de la République d'Haïti)

| Rapport | Fréquence | Contenu |
|---------|-----------|---------|
| **Bilan** | Mensuel | Actifs, passifs, fonds propres |
| **Résultats** | Mensuel | PNB, charges, résultat |
| **Ratios prudentiels** | Mensuel | CAR, liquidité, concentration |
| **Grands risques** | Mensuel | Expositions > 10% FP |
| **Provisions** | Trimestriel | Classification portefeuille |
| **AML** | En continu | Transactions suspectes |

### 4.2 Calcul des Ratios Réglementaires

```python
def calculate_regulatory_ratios(data):
    """Calcul des ratios réglementaires BRH"""
    
    ratios = {}
    
    # Ratio de solvabilité (CAR)
    tier1 = data['capital_tier1']
    tier2 = data['capital_tier2']
    rwa = data['risk_weighted_assets']
    ratios['CAR'] = (tier1 + tier2) / rwa * 100
    ratios['CAR_compliant'] = ratios['CAR'] >= 12
    
    # Ratio de liquidité
    liquid_assets = data['cash'] + data['gov_securities']
    demand_deposits = data['demand_deposits']
    ratios['liquidity'] = liquid_assets / demand_deposits * 100
    ratios['liquidity_compliant'] = ratios['liquidity'] >= 20
    
    # Ratio des grands risques
    largest_exposure = data['largest_single_exposure']
    equity = data['total_equity']
    ratios['large_exposure'] = largest_exposure / equity * 100
    ratios['large_exposure_compliant'] = ratios['large_exposure'] <= 15
    
    # Loan-to-deposit
    ratios['LDR'] = data['total_loans'] / data['total_deposits'] * 100
    
    return ratios
```

### 4.3 Alertes Réglementaires

```dax
// DAX: Alerte si ratio proche du seuil
Alerte CAR = 
VAR Ratio = [CAR Ratio]
VAR Seuil = 12
VAR Buffer = 2
RETURN
SWITCH(
    TRUE(),
    Ratio < Seuil, "🔴 CRITIQUE: Sous le minimum",
    Ratio < Seuil + Buffer, "🟡 ATTENTION: Proche du seuil",
    "🟢 OK"
)
```

---

## Partie 5: Analyse Spécifique Contexte Haïtien

### 5.1 Défis Uniques

| Défi | Impact | Approche BI |
|------|--------|-------------|
| **Économie informelle** | Évaluation du risque | Données alternatives |
| **Volatilité HTG/USD** | Risque de change | Monitoring quotidien |
| **Diaspora** | Flux de transferts | Analyse des remittances |
| **Inclusion financière** | Expansion marché | Segmentation géographique |
| **Infrastructure** | Disponibilité data | Qualité des données |

### 5.2 KPIs Spécifiques Haïti

```python
haiti_kpis = {
    # Mix de devises
    'HTG_deposit_share': 'Dépôts HTG / Total Dépôts',
    
    # Concentration géographique
    'PAP_concentration': 'Activité PAP / Total',
    
    # Digitalisation
    'digital_transactions_pct': 'Tx digitales / Total Tx',
    'mobile_banking_users': 'Utilisateurs mobile banking',
    
    # Transferts
    'remittance_volume': 'Volume transferts diaspora',
    
    # Inclusion
    'first_time_banked': 'Nouveaux au système bancaire'
}
```

### 5.3 Analyse Multi-devises

```dax
// Exposition au risque de change
Exposition USD = 
VAR ActifsUSD = CALCULATE(SUM(Bilan[Montant]), Bilan[Devise] = "USD")
VAR PassifsUSD = CALCULATE(SUM(Passif[Montant]), Passif[Devise] = "USD")
RETURN ActifsUSD - PassifsUSD

// Position de change en %
Position Change = DIVIDE(
    [Exposition USD],
    [Total Fonds Propres]
) * 100
```

---

## Partie 6: Segmentation Client Bancaire

### 6.1 Critères de Segmentation

| Segment | Critères | Caractéristiques |
|---------|----------|------------------|
| **Mass Market** | Solde < 100K | Volume, faible marge |
| **Mass Affluent** | 100K - 1M | Potentiel cross-sell |
| **Affluent** | 1M - 10M | Conseil personnalisé |
| **Private Banking** | > 10M | Service dédié |
| **PME** | Entreprises < 50 emp | Besoins mixtes |
| **Corporate** | Grandes entreprises | Sur mesure |

### 6.2 Mesures DAX par Segment

```dax
// Rentabilité par segment
Rentabilite Segment = 
VAR Revenus = [PNB Segment]
VAR Couts = [Couts Segment]
VAR Provisions = [Provisions Segment]
RETURN
DIVIDE(Revenus - Couts - Provisions, [Capital Alloue])

// LTV simplifié
Customer LTV = 
VAR RevenuAnnuel = [Revenu Client]
VAR DureeRelation = DATEDIFF([Date Ouverture], TODAY(), YEAR)
VAR MargeNette = 0.15
RETURN
RevenuAnnuel * DureeRelation * MargeNette
```

### 6.3 Matrice de Migration

```sql
-- Suivi de la migration entre segments
WITH segment_history AS (
    SELECT 
        client_id,
        segment,
        date_effective,
        LAG(segment) OVER (PARTITION BY client_id ORDER BY date_effective) as segment_prec
    FROM client_segments
)
SELECT 
    segment_prec as de_segment,
    segment as vers_segment,
    COUNT(*) as nb_clients
FROM segment_history
WHERE segment_prec IS NOT NULL
GROUP BY segment_prec, segment
ORDER BY nb_clients DESC;
```

---

## Partie 7: Expected Loss et Provisions

### 7.1 Modèle IFRS 9

```
Expected Credit Loss (ECL) = PD × LGD × EAD

PD: Probability of Default
LGD: Loss Given Default
EAD: Exposure at Default

Stages:
- Stage 1: 12-month ECL (performing)
- Stage 2: Lifetime ECL (deteriorated)
- Stage 3: Lifetime ECL (impaired/NPL)
```

### 7.2 Calcul en DAX

```dax
// Expected Loss par prêt
EL = SUMX(
    Prets,
    Prets[EAD] * Prets[PD] * Prets[LGD]
)

// Provision Coverage
Coverage = DIVIDE(
    SUM(Provisions[Montant]),
    CALCULATE(SUM(Prets[Solde]), Prets[JoursRetard] > 90)
) * 100

// Migration de stage
Migration Stage 2 = CALCULATE(
    COUNTROWS(Prets),
    Prets[Stage] = 2,
    Prets[Stage Precedent] = 1
)
```

---

## Partie 8: Anti-Money Laundering (AML)

### 8.1 Indicateurs de Surveillance

```python
aml_indicators = {
    # Seuils de déclaration
    'threshold_reporting': 50000,  # USD équivalent
    
    # Red flags
    'structuring': 'Multiple tx juste sous le seuil',
    'unusual_activity': 'Tx >> moyenne historique',
    'high_risk_countries': 'Tx avec pays à risque',
    'shell_companies': 'Entreprises sans activité visible'
}
```

### 8.2 Alertes AML en SQL

```sql
-- Détection de structuration (smurfing)
SELECT 
    client_id,
    DATE(date_tx) as jour,
    COUNT(*) as nb_tx,
    SUM(montant) as total_jour
FROM transactions
WHERE montant BETWEEN 45000 AND 49999
GROUP BY client_id, DATE(date_tx)
HAVING COUNT(*) >= 3
ORDER BY total_jour DESC;

-- Activité inhabituelle
WITH client_stats AS (
    SELECT 
        client_id,
        AVG(montant) as avg_montant,
        STDDEV(montant) as std_montant
    FROM transactions
    WHERE date_tx >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY client_id
)
SELECT t.*
FROM transactions t
JOIN client_stats s ON t.client_id = s.client_id
WHERE t.montant > s.avg_montant + 3 * s.std_montant
AND t.date_tx >= CURRENT_DATE - INTERVAL '30 days';
```

---

## Questions d'Entretien BI Bancaire

1. **Quels sont les principaux KPIs d'une banque commerciale?**
   → ROE, ROA, NPL ratio, CAR, NIM, CIR

2. **Expliquez le NPL ratio et son importance.**
   → Prêts > 90 jours / Total prêts; indicateur de qualité des actifs

3. **Qu'est-ce que le CAR et pourquoi est-il réglementé?**
   → Fonds propres / RWA; assure la solvabilité face aux pertes

4. **Comment segmentez-vous les clients d'une banque?**
   → Par valeur (RFM), comportement, produits, cycle de vie

5. **Quels sont les défis BI spécifiques au marché haïtien?**
   → Économie informelle, risque de change, infrastructure data

---

## Checklist BI Banque Commerciale

```
□ Maîtriser les indicateurs de rentabilité (ROE, ROA, NIM)
□ Comprendre les ratios de risque (NPL, provisions)
□ Connaître les exigences réglementaires (CAR, liquidité)
□ Savoir construire des dashboards exécutifs
□ Comprendre la segmentation client bancaire
□ Maîtriser le reporting réglementaire
□ Connaître les spécificités du marché haïtien
□ Comprendre les enjeux AML/Compliance
```

---

**Rappel:** La BI bancaire doit toujours équilibrer trois objectifs: maximiser la rentabilité, gérer les risques, et assurer la conformité réglementaire.
