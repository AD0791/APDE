# Test Business Intelligence - Test 1

**Sujet:** BI et Métriques Bancaires  
**Niveau:** Intermédiaire  
**Nombre de questions:** 25

---

## Questions et Réponses

**Q1.** Qu'est-ce que la Business Intelligence et quel est son rôle dans une banque?

**R1.**
**Business Intelligence (BI):** Ensemble de technologies, pratiques et applications pour collecter, intégrer, analyser et présenter les données métier.

**Rôle dans une banque:**
- **Reporting réglementaire:** Conformité BRH, Bâle
- **Pilotage:** Tableaux de bord pour la direction
- **Analyse de risque:** Suivi du portefeuille de crédit
- **Commercial:** Segmentation, campagnes
- **Opérationnel:** Efficacité des processus

---

**Q2.** Quels sont les composants d'une architecture BI moderne?

**R2.**
```
1. SOURCES DE DONNÉES
   └── Core banking, CRM, fichiers externes

2. ETL (Extract, Transform, Load)
   └── Nettoyage, transformation, chargement

3. DATA WAREHOUSE
   └── Stockage centralisé, historisé

4. DATA MARTS
   └── Sous-ensembles par domaine (risque, commercial)

5. COUCHE SÉMANTIQUE
   └── Modèles, mesures, dimensions

6. VISUALISATION
   └── Power BI, Tableau, rapports
```

---

**Q3.** Calculez et interprétez le ROE (Return on Equity).

**R3.**
**Formule:**
```
ROE = Résultat Net / Capitaux Propres × 100
```

**Exemple:**
```
Résultat Net = 150M HTG
Capitaux Propres = 1,000M HTG
ROE = 150 / 1,000 × 100 = 15%
```

**Interprétation:**
- ROE de 15% = Pour chaque 100 HTG de capital, la banque génère 15 HTG de profit
- Benchmark: 12-18% pour banques bien gérées

---

**Q4.** Calculez et interprétez le ROA (Return on Assets).

**R4.**
**Formule:**
```
ROA = Résultat Net / Total Actifs × 100
```

**Exemple:**
```
Résultat Net = 150M HTG
Total Actifs = 10,000M HTG
ROA = 150 / 10,000 × 100 = 1.5%
```

**Interprétation:**
- ROA de 1.5% = La banque génère 1.5 HTG de profit pour chaque 100 HTG d'actifs
- Benchmark: 1-2% pour banques commerciales

---

**Q5.** Qu'est-ce que le NIM (Net Interest Margin)?

**R5.**
**Formule:**
```
NIM = (Revenus d'Intérêts - Charges d'Intérêts) / Actifs Productifs × 100
```

**Exemple:**
```
Revenus d'intérêts = 800M HTG
Charges d'intérêts = 300M HTG
Actifs productifs = 8,000M HTG
NIM = (800 - 300) / 8,000 × 100 = 6.25%
```

**Interprétation:**
- Mesure l'efficacité de l'intermédiation bancaire
- Plus élevé = meilleure gestion des taux

---

**Q6.** Calculez le NPL Ratio (Non-Performing Loans).

**R6.**
**Formule:**
```
NPL Ratio = Prêts Non Performants / Total Portefeuille × 100
```

**Définition NPL:** Prêts en retard de paiement > 90 jours ou douteux.

**Exemple:**
```
NPL = 200M HTG
Total Prêts = 5,000M HTG
NPL Ratio = 200 / 5,000 × 100 = 4%
```

**Benchmark:** < 5% généralement acceptable

---

**Q7.** Qu'est-ce que le Coverage Ratio et pourquoi est-il important?

**R7.**
**Formule:**
```
Coverage Ratio = Provisions pour Créances Douteuses / NPL × 100
```

**Exemple:**
```
Provisions = 150M HTG
NPL = 200M HTG
Coverage = 150 / 200 × 100 = 75%
```

**Interprétation:**
- 75% signifie que 75% des NPL sont couverts par des provisions
- Minimum recommandé: 100% (100% des pertes anticipées couvertes)

---

**Q8.** Calculez le CIR (Cost-to-Income Ratio).

**R8.**
**Formule:**
```
CIR = Charges d'Exploitation / PNB × 100
```

**PNB (Produit Net Bancaire):** Revenus nets de la banque

**Exemple:**
```
Charges = 400M HTG
PNB = 800M HTG
CIR = 400 / 800 × 100 = 50%
```

**Interprétation:**
- CIR de 50% = 50 centimes de coûts pour chaque gourde de revenu
- Cible: < 55% pour efficacité

---

**Q9.** Qu'est-ce que le CAR (Capital Adequacy Ratio)?

**R9.**
**Formule:**
```
CAR = Fonds Propres Réglementaires / Actifs Pondérés par le Risque × 100
```

**Composants:**
- Tier 1: Capital de base (actions, réserves)
- Tier 2: Capital complémentaire (dette subordonnée)
- RWA: Actifs × coefficient de risque

**Minimum réglementaire:** 8% (Bâle), souvent 12% pour BRH

---

**Q10.** Qu'est-ce que le LDR (Loan-to-Deposit Ratio)?

**R10.**
**Formule:**
```
LDR = Total Prêts / Total Dépôts × 100
```

**Exemple:**
```
Prêts = 6,000M HTG
Dépôts = 8,000M HTG
LDR = 6,000 / 8,000 × 100 = 75%
```

**Interprétation:**
- 75% = 75% des dépôts sont prêtés
- Trop bas (<60%): Sous-utilisation des ressources
- Trop haut (>100%): Risque de liquidité

---

**Q11.** Quels KPIs commerciaux sont essentiels pour une banque?

**R11.**
| KPI | Formule | Usage |
|-----|---------|-------|
| **CAC** | Coûts Marketing / Nouveaux Clients | Efficacité acquisition |
| **CLV** | Revenu Moyen × Durée Relation | Valeur client |
| **Churn** | Clients Perdus / Total Clients | Rétention |
| **Cross-sell** | Clients Multi-produits / Total | Pénétration |
| **NPS** | % Promoteurs - % Détracteurs | Satisfaction |

---

**Q12.** Comment calculer le taux de croissance des dépôts?

**R12.**
**YoY (Year-over-Year):**
```
Croissance = (Dépôts_N - Dépôts_N-1) / Dépôts_N-1 × 100
```

**MoM (Month-over-Month):**
```
Croissance_MoM = (Dépôts_M - Dépôts_M-1) / Dépôts_M-1 × 100
```

**En DAX:**
```dax
Croissance YoY = 
DIVIDE(
    [Total Dépôts] - CALCULATE([Total Dépôts], SAMEPERIODLASTYEAR(Calendrier[Date])),
    CALCULATE([Total Dépôts], SAMEPERIODLASTYEAR(Calendrier[Date]))
)
```

---

**Q13.** Qu'est-ce qu'un reporting réglementaire et quels sont les principaux rapports pour la BRH?

**R13.**
**Reporting réglementaire:** Rapports obligatoires soumis au régulateur (BRH).

**Principaux rapports:**
1. **Ratio de solvabilité (CAR):** Mensuel
2. **Ratio de liquidité:** Hebdomadaire/Mensuel
3. **Concentration des risques:** Grands engagements
4. **Qualité du portefeuille:** NPL, provisions
5. **AML/KYC:** Déclarations de soupçons

---

**Q14.** Comment structurer un dashboard exécutif pour le CEO?

**R14.**
**Principes:**
- Maximum **4-6 KPIs** visibles
- **Tendances** (vs juste les chiffres)
- **Comparaison** vs objectif et N-1
- **Alertes visuelles** (couleurs)

**Structure suggérée:**
```
┌─────────────────┬─────────────────┬─────────────────┐
│   ROE: 15%      │   NPL: 4.2%     │   CIR: 52%      │
│   ↑ vs obj 14%  │   ↑ vs 3.8%     │   ↓ vs 55%      │
├─────────────────┴─────────────────┴─────────────────┤
│              ÉVOLUTION PNB (12 mois)                │
│              [Line chart avec trend]                │
├─────────────────────────────────────────────────────┤
│   Dépôts: +8% YoY  │  Prêts: +5% YoY  │  Clients: +3%│
└─────────────────────────────────────────────────────┘
```

---

**Q15.** Comment analyser la concentration du portefeuille de crédit?

**R15.**
**Dimensions d'analyse:**
1. **Par secteur:** Agriculture, Commerce, Services...
2. **Par région/agence**
3. **Par taille de prêt**
4. **Par client:** Top 10 expositions

**Métriques:**
```python
# Indice de Herfindahl-Hirschman (HHI)
hhi = (df.groupby('secteur')['montant'].sum() ** 2).sum() / df['montant'].sum() ** 2

# Top 10 concentration
top_10 = df.nlargest(10, 'exposition')['exposition'].sum() / df['exposition'].sum()
```

**Risque:** Forte concentration = vulnérabilité si un secteur/client fait défaut

---

**Q16.** Quels indicateurs AML (Anti-Money Laundering) surveiller?

**R16.**
| Indicateur | Seuil/Alerte |
|------------|--------------|
| Transactions > seuil de déclaration | Généralement 500K HTG |
| Transactions fractionnées | Structuration pour éviter seuil |
| Transactions cash inhabituelles | Ratio cash élevé |
| Transactions cross-border | Pays à risque |
| Activité vs profil | Incohérence avec KYC |

---

**Q17.** Comment calculer l'Expected Loss (EL)?

**R17.**
**Formule:**
```
EL = PD × LGD × EAD
```

**Où:**
- **PD (Probability of Default):** Probabilité de défaut
- **LGD (Loss Given Default):** Perte en cas de défaut (% non récupéré)
- **EAD (Exposure at Default):** Montant exposé au moment du défaut

**Exemple:**
```
Prêt: 1,000,000 HTG
PD: 5%
LGD: 45%
EAD: 1,000,000 HTG

EL = 0.05 × 0.45 × 1,000,000 = 22,500 HTG
```

---

**Q18.** Comment analyser la rentabilité par produit?

**R18.**
```python
rentabilite = df.groupby('produit').agg({
    'revenus': 'sum',
    'couts': 'sum',
    'client_id': 'nunique'
})
rentabilite['marge'] = rentabilite['revenus'] - rentabilite['couts']
rentabilite['marge_pct'] = rentabilite['marge'] / rentabilite['revenus'] * 100
rentabilite['revenu_par_client'] = rentabilite['revenus'] / rentabilite['client_id']
```

**KPIs par produit:**
- Marge nette
- Revenu par client
- Coût d'acquisition
- Taux de croissance

---

**Q19.** Qu'est-ce que l'analyse de vintage?

**R19.**
**Vintage analysis:** Suivi de la performance des prêts par cohorte (date d'octroi).

**Objectif:** Identifier si la qualité des prêts se dégrade dans le temps.

```python
# Créer les cohortes par mois d'octroi
df['vintage'] = df['date_octroi'].dt.to_period('M')

# Taux de défaut par vintage et âge
pivot = df.pivot_table(
    values='defaut',
    index='vintage',
    columns='age_mois',
    aggfunc='mean'
)

# Heatmap
sns.heatmap(pivot, cmap='RdYlGn_r', annot=True, fmt='.1%')
```

---

**Q20.** Comment mesurer l'efficacité des agences?

**R20.**
**KPIs par agence:**
```
Production = Volume de nouveaux prêts / crédits
Collecte = Nouveaux dépôts
Qualité = NPL ratio de l'agence
Efficacité = Nombre de clients / ETP
Rentabilité = PNB / Charges opérationnelles
```

**Dashboard comparatif:**
```python
agence_perf = df.groupby('agence').agg({
    'montant_pret': 'sum',
    'depots': 'sum',
    'defaut': 'mean',
    'client_id': 'nunique',
    'pnb': 'sum',
    'charges': 'sum'
})
agence_perf['rentabilite'] = agence_perf['pnb'] / agence_perf['charges']
```

---

**Q21.** Quels sont les indicateurs de liquidité à surveiller?

**R21.**
| Indicateur | Formule | Cible |
|------------|---------|-------|
| **LCR** | Actifs Liquides / Sorties Nettes 30j | ≥ 100% |
| **NSFR** | Financement Stable / Besoins Stables | ≥ 100% |
| **LDR** | Prêts / Dépôts | 60-90% |
| **Quick Ratio** | (Cash + Équiv.) / Passifs CT | > 1 |

---

**Q22.** Comment construire un cube OLAP pour l'analyse bancaire?

**R22.**
**Dimensions:**
```
- Temps (Année, Trimestre, Mois, Jour)
- Produit (Catégorie, Type, Produit)
- Client (Segment, Région, Client)
- Agence (Région, Zone, Agence)
- Compte (Type, Statut)
```

**Mesures:**
```
- Montants (Solde, Volume, Moyenne)
- Compteurs (Nb clients, Nb transactions)
- Ratios (NPL, Croissance)
```

**Opérations:**
- Drill-down: Année → Mois → Jour
- Roll-up: Client → Segment → Total
- Slice: Filtrer sur une dimension
- Dice: Filtrer sur plusieurs dimensions

---

**Q23.** Comment mettre en place des alertes BI automatisées?

**R23.**
**Types d'alertes:**
1. **Seuil absolu:** NPL > 5%
2. **Variation:** Croissance dépôts < -5% MoM
3. **Anomalie:** Écart > 2σ de la moyenne
4. **Deadline:** Reporting non soumis

**Implémentation Power BI:**
```
1. Data Alert sur visualisation
2. Power Automate pour workflow
3. Email/Teams notification
```

---

**Q24.** Comment gérer la qualité des données BI?

**R24.**
**Framework de Data Quality:**

| Dimension | Description | Vérification |
|-----------|-------------|--------------|
| **Complétude** | Pas de manquants critiques | % NULL |
| **Exactitude** | Valeurs correctes | Règles métier |
| **Cohérence** | Pas de contradictions | Cross-checks |
| **Fraîcheur** | Données à jour | Timestamp |
| **Unicité** | Pas de doublons | Count distinct |

```python
# Rapport qualité
def data_quality_report(df):
    return {
        'completeness': 1 - df.isnull().mean().mean(),
        'duplicates': df.duplicated().sum() / len(df),
        'freshness': (pd.Timestamp.now() - df['date_maj'].max()).days
    }
```

---

**Q25.** Concevez un tableau de bord de suivi du risque crédit pour UniBank.

**R25.**
**Dashboard Risque Crédit:**

```
┌──────────────────────────────────────────────────────────┐
│                   SUIVI RISQUE CRÉDIT                    │
│                     UniBank Haiti                        │
├──────────────────────────────────────────────────────────┤
│  INDICATEURS CLÉS                                        │
│  ┌────────┬────────┬────────┬────────┐                  │
│  │NPL 4.2%│Couv 85%│EL 150M │CAR 14% │                  │
│  │↑ 0.3%  │↓ 5%    │↑ 10M   │stable  │                  │
│  └────────┴────────┴────────┴────────┘                  │
├──────────────────────────────────────────────────────────┤
│  ÉVOLUTION NPL (12 mois)          │  NPL PAR SECTEUR    │
│  [Line chart: NPL + Coverage]     │  [Bar chart]        │
│                                   │  Agri: 8%           │
│                                   │  Commerce: 4%       │
├───────────────────────────────────┼─────────────────────┤
│  CONCENTRATION TOP 10             │  MIGRATION BUCKETS  │
│  [Treemap ou Pareto]              │  [Sankey ou Stacked]│
│  Client A: 5%                     │  Current → 30j → 90j│
│  Client B: 4%                     │                     │
├───────────────────────────────────┴─────────────────────┤
│  VINTAGE ANALYSIS (Heatmap)                              │
│  [Taux défaut par cohorte d'octroi et âge du prêt]      │
└──────────────────────────────────────────────────────────┘
```

**Filtres:** Période, Agence, Produit, Secteur

**Refresh:** Quotidien pour opérationnel, Mensuel pour Board

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-10 | À améliorer |
| 11-17 | Intermédiaire |
| 18-22 | Avancé |
| 23-25 | Expert |
