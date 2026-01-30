# Étude de Cas Complète - Business Intelligence Bancaire
## UniBank Haiti - Analyse de Performance

---

## Contexte

Vous êtes Data Analyst chez UniBank Haiti. Le comité de direction vous demande de préparer une analyse complète de la performance de la banque pour le dernier trimestre, avec des recommandations d'amélioration.

---

## Données Disponibles

```
BILAN_MENSUEL
- mois, total_actifs, total_passifs, capitaux_propres
- prets_bruts, provisions, prets_nets
- depots_vue, depots_terme, depots_epargne
- cash, titres_gouvernement, autres_actifs
- rwa (Risk Weighted Assets)

COMPTE_RESULTAT
- mois, revenus_interets, charges_interets
- commissions_nettes, autres_revenus
- charges_personnel, charges_admin, autres_charges
- dotation_provisions, resultat_net

PORTEFEUILLE_PRETS
- pret_id, client_id, agence_id, secteur
- montant_initial, solde_restant, taux
- date_octroi, date_echeance, jours_retard
- classification (Performing/Watch/Substandard/Doubtful/Loss)

AGENCES
- agence_id, nom, region, type (succursale/agence)
- depots, prets, nb_clients, nb_employes
```

---

## PARTIE 1: Calcul des KPIs

### Question 1.1: Indicateurs de Rentabilité

Calculez les indicateurs suivants pour le trimestre:
- ROE
- ROA  
- NIM
- CIR

**Données du trimestre:**
```
Résultat Net: 45M HTG
Capitaux Propres (moyenne): 320M HTG
Total Actifs (moyenne): 2,800M HTG
Revenus d'intérêts: 180M HTG
Charges d'intérêts: 65M HTG
Actifs productifs (moyenne): 2,400M HTG
Charges d'exploitation: 85M HTG
PNB: 145M HTG
```

### Solution 1.1

```python
# Calculs
roe = (45 / 320) * 100  # = 14.06%
roa = (45 / 2800) * 100  # = 1.61%
nim = ((180 - 65) / 2400) * 100  # = 4.79%
cir = (85 / 145) * 100  # = 58.62%

# Interprétation
print(f"ROE: {roe:.2f}% - {'✓ Bon' if roe >= 12 else '✗ À améliorer'} (benchmark: 12-18%)")
print(f"ROA: {roa:.2f}% - {'✓ Bon' if roa >= 1 else '✗ À améliorer'} (benchmark: 1-2%)")
print(f"NIM: {nim:.2f}% - {'✓ Bon' if nim >= 3 else '✗ À améliorer'} (benchmark: 3-5%)")
print(f"CIR: {cir:.2f}% - {'✓ Bon' if cir <= 55 else '⚠ À surveiller'} (benchmark: 45-55%)")
```

**Analyse:**
- ROE (14.06%): Dans la fourchette cible, bonne rentabilité pour les actionnaires
- ROA (1.61%): Acceptable, utilisation efficace des actifs
- NIM (4.79%): Bonne marge d'intermédiation
- CIR (58.62%): Légèrement au-dessus de la cible, optimisation des coûts nécessaire

---

### Question 1.2: Indicateurs de Risque

Calculez:
- NPL Ratio
- Provision Coverage
- Cost of Risk

**Données:**
```
Encours total prêts: 1,800M HTG
Prêts > 90 jours (NPL): 81M HTG
Provisions totales: 95M HTG
Dotations provisions (trimestre): 12M HTG
```

### Solution 1.2

```python
npl_ratio = (81 / 1800) * 100  # = 4.5%
coverage = (95 / 81) * 100  # = 117.3%
cost_of_risk = (12 * 4 / 1800) * 100  # = 2.67% (annualisé)

print(f"NPL Ratio: {npl_ratio:.1f}% - {'✓' if npl_ratio < 5 else '✗'} (seuil: 5%)")
print(f"Coverage: {coverage:.1f}% - {'✓' if coverage >= 100 else '✗'} (min: 100%)")
print(f"Cost of Risk: {cost_of_risk:.2f}% annualisé")
```

**Analyse:**
- NPL Ratio (4.5%): Proche mais encore sous le seuil de 5%, surveillance accrue nécessaire
- Coverage (117.3%): Provisions suffisantes pour couvrir les pertes attendues
- Cost of Risk (2.67%): Dans la norme pour le marché haïtien

---

### Question 1.3: Indicateurs de Solvabilité et Liquidité

Calculez:
- CAR (Capital Adequacy Ratio)
- Loan-to-Deposit Ratio

**Données:**
```
Capital Tier 1: 280M HTG
Capital Tier 2: 40M HTG
RWA: 2,200M HTG
Total Prêts: 1,800M HTG
Total Dépôts: 2,100M HTG
```

### Solution 1.3

```python
car = ((280 + 40) / 2200) * 100  # = 14.55%
ldr = (1800 / 2100) * 100  # = 85.71%

print(f"CAR: {car:.2f}% - {'✓' if car >= 12 else '✗'} (exigence BRH: 12%)")
print(f"LDR: {ldr:.1f}% - {'✓ Optimal' if 80 <= ldr <= 90 else '⚠'}")
```

**Analyse:**
- CAR (14.55%): Confortable, buffer de 2.55% au-dessus du minimum
- LDR (85.71%): Dans la fourchette optimale, bon équilibre prêts/dépôts

---

## PARTIE 2: Analyse du Portefeuille

### Question 2.1: Analyse par Secteur

Analysez le portefeuille de prêts par secteur:

| Secteur | Encours (M) | NPL (M) | Nb Prêts |
|---------|-------------|---------|----------|
| Agriculture | 450 | 45 | 2,500 |
| Commerce | 700 | 21 | 4,200 |
| Services | 400 | 10 | 1,800 |
| Industrie | 250 | 5 | 500 |
| **Total** | **1,800** | **81** | **9,000** |

### Solution 2.1

```python
import pandas as pd

data = {
    'Secteur': ['Agriculture', 'Commerce', 'Services', 'Industrie'],
    'Encours': [450, 700, 400, 250],
    'NPL': [45, 21, 10, 5],
    'Nb_Prets': [2500, 4200, 1800, 500]
}
df = pd.DataFrame(data)

# Calculs
df['NPL_Ratio'] = (df['NPL'] / df['Encours'] * 100).round(1)
df['Part_Portefeuille'] = (df['Encours'] / df['Encours'].sum() * 100).round(1)
df['Pret_Moyen'] = (df['Encours'] / df['Nb_Prets'] * 1000).round(0)  # en milliers

print(df.to_string())
```

**Résultat:**
| Secteur | NPL Ratio | Part Portefeuille | Prêt Moyen (K) |
|---------|-----------|-------------------|----------------|
| Agriculture | 10.0% | 25.0% | 180 |
| Commerce | 3.0% | 38.9% | 167 |
| Services | 2.5% | 22.2% | 222 |
| Industrie | 2.0% | 13.9% | 500 |

**Analyse et Recommandations:**
1. **Agriculture (10% NPL):** Risque élevé, renforcer les critères d'octroi, diversifier les sous-secteurs
2. **Commerce (3%):** Pilier du portefeuille, maintenir la qualité
3. **Services (2.5%):** Bon segment, potentiel de croissance
4. **Industrie (2%):** Meilleure qualité, augmenter l'exposition si possible

---

### Question 2.2: Vintage Analysis

Analysez la performance des cohortes de prêts octroyés:

| Cohorte (trimestre octroi) | Encours Initial | NPL après 12 mois |
|----------------------------|-----------------|-------------------|
| Q1 2023 | 200M | 12M |
| Q2 2023 | 180M | 9M |
| Q3 2023 | 220M | 7M |
| Q4 2023 | 190M | 4M |

### Solution 2.2

```python
cohortes = pd.DataFrame({
    'Cohorte': ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023'],
    'Encours_Initial': [200, 180, 220, 190],
    'NPL_12M': [12, 9, 7, 4]
})

cohortes['Taux_NPL_12M'] = (cohortes['NPL_12M'] / cohortes['Encours_Initial'] * 100).round(1)

print(cohortes.to_string())
```

**Résultat:**
| Cohorte | Taux NPL à 12 mois |
|---------|-------------------|
| Q1 2023 | 6.0% |
| Q2 2023 | 5.0% |
| Q3 2023 | 3.2% |
| Q4 2023 | 2.1% |

**Interprétation:**
- Amélioration significative de la qualité des octrois
- Les mesures de renforcement du scoring semblent efficaces
- Q1 2023 peut nécessiter une attention particulière (restructuration)

---

## PARTIE 3: Requêtes SQL

### Question 3.1

Écrivez une requête SQL pour calculer le NPL ratio par agence et identifier les agences problématiques (NPL > 5%).

### Solution 3.1

```sql
WITH agence_stats AS (
    SELECT 
        a.agence_id,
        a.nom,
        a.region,
        SUM(p.solde_restant) as total_encours,
        SUM(CASE WHEN p.jours_retard > 90 THEN p.solde_restant ELSE 0 END) as npl_encours
    FROM agences a
    LEFT JOIN portefeuille_prets p ON a.agence_id = p.agence_id
    GROUP BY a.agence_id, a.nom, a.region
)
SELECT 
    agence_id,
    nom,
    region,
    total_encours,
    npl_encours,
    ROUND(npl_encours * 100.0 / NULLIF(total_encours, 0), 2) as npl_ratio,
    CASE 
        WHEN npl_encours * 100.0 / NULLIF(total_encours, 0) > 7 THEN 'CRITIQUE'
        WHEN npl_encours * 100.0 / NULLIF(total_encours, 0) > 5 THEN 'ALERTE'
        ELSE 'OK'
    END as statut
FROM agence_stats
WHERE total_encours > 0
ORDER BY npl_ratio DESC;
```

---

### Question 3.2

Écrivez une requête pour identifier les clients avec le plus haut risque de concentration (exposition > 5% des fonds propres).

### Solution 3.2

```sql
WITH client_exposure AS (
    SELECT 
        c.client_id,
        c.nom,
        SUM(p.solde_restant) as exposition_totale
    FROM clients c
    JOIN portefeuille_prets p ON c.client_id = p.client_id
    GROUP BY c.client_id, c.nom
),
fonds_propres AS (
    SELECT capitaux_propres 
    FROM bilan_mensuel 
    ORDER BY mois DESC 
    LIMIT 1
)
SELECT 
    ce.client_id,
    ce.nom,
    ce.exposition_totale,
    ROUND(ce.exposition_totale * 100.0 / fp.capitaux_propres, 2) as pct_fonds_propres
FROM client_exposure ce
CROSS JOIN fonds_propres fp
WHERE ce.exposition_totale * 100.0 / fp.capitaux_propres > 5
ORDER BY pct_fonds_propres DESC;
```

---

## PARTIE 4: Mesures DAX

### Question 4.1

Créez les mesures DAX suivantes pour un rapport Power BI:
1. NPL Ratio dynamique
2. Variation YoY du PNB
3. Provision Coverage

### Solution 4.1

```dax
// 1. NPL Ratio
NPL Ratio = 
VAR TotalPrets = SUM(Portefeuille[Solde_Restant])
VAR NPL = CALCULATE(
    SUM(Portefeuille[Solde_Restant]),
    Portefeuille[Jours_Retard] > 90
)
RETURN
DIVIDE(NPL, TotalPrets, 0) * 100

// 2. Variation YoY du PNB
PNB Var YoY = 
VAR PNB_Actuel = [PNB]
VAR PNB_N1 = CALCULATE(
    [PNB],
    SAMEPERIODLASTYEAR(Calendrier[Date])
)
RETURN
DIVIDE(PNB_Actuel - PNB_N1, PNB_N1, 0) * 100

// 3. Provision Coverage
Provision Coverage = 
VAR Provisions = SUM(Bilan[Provisions])
VAR NPL = CALCULATE(
    SUM(Portefeuille[Solde_Restant]),
    Portefeuille[Jours_Retard] > 90
)
RETURN
DIVIDE(Provisions, NPL, 0) * 100

// Mesure de couleur conditionnelle
NPL Color = 
VAR Ratio = [NPL Ratio]
RETURN
SWITCH(
    TRUE(),
    Ratio > 7, "#FF0000",  -- Rouge
    Ratio > 5, "#FFA500",  -- Orange
    "#00FF00"              -- Vert
)
```

---

## PARTIE 5: Recommandations

### Question 5.1

Basé sur votre analyse, quelles sont vos 5 principales recommandations pour le comité de direction?

### Solution 5.1

**1. Gestion du Risque Agricole (URGENT)**
- Le secteur Agriculture représente 55% des NPL malgré 25% du portefeuille
- Action: Revoir les critères d'octroi, exiger plus de garanties, diversifier les cultures
- KPI: Réduire le NPL agricole à 7% d'ici 6 mois

**2. Optimisation des Coûts (CIR)**
- CIR à 58.62% vs cible de 55%
- Action: Digitalisation des processus, rationalisation du réseau d'agences
- KPI: Réduire le CIR de 3 points en 12 mois

**3. Surveillance des Agences Sous-performantes**
- Certaines agences dépassent le seuil de 5% NPL
- Action: Audit des processus de crédit, formation des agents
- KPI: Aucune agence > 5% NPL

**4. Diversification du Portefeuille**
- Concentration élevée sur Commerce (39%)
- Action: Développer les secteurs Services et Industrie
- KPI: Atteindre 30% Commerce, 25% Services, 20% Industrie

**5. Renforcement du Capital (Proactif)**
- CAR à 14.55% est confortable mais le NPL augmente
- Action: Constituer une réserve additionnelle
- KPI: Maintenir CAR > 15%

---

## Livrables Attendus

1. **Tableau des KPIs** avec comparaison aux benchmarks
2. **Analyse du portefeuille** par secteur et par cohorte
3. **Dashboard concept** avec les visualisations clés
4. **Note de synthèse** (1-2 pages) pour le comité de direction

---

## Critères d'Évaluation

| Critère | Points |
|---------|--------|
| Exactitude des calculs | 25% |
| Qualité de l'analyse | 30% |
| Pertinence des recommandations | 25% |
| Clarté de la présentation | 20% |
