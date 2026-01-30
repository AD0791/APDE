# Test Indicateurs et Indices - Test 1

**Sujet:** Indicateurs et Indices - Théorie et Pratique  
**Niveau:** Intermédiaire  
**Nombre de questions:** 20

---

## Questions et Réponses

**Q1.** Quelle est la différence entre un indicateur et un indice?

**R1.**
| Indicateur | Indice |
|------------|--------|
| Mesure directe d'un phénomène | Synthèse de plusieurs indicateurs |
| Valeur absolue ou relative | Généralement relatif à une base |
| Ex: Taux de défaut = 5% | Ex: IPC base 100 = 115 |

---

**Q2.** Quels sont les critères SMART pour un bon indicateur?

**R2.**
- **S**pécifique: Clair et précis
- **M**esurable: Quantifiable objectivement
- **A**tteignable: Réaliste
- **R**elevant: Pertinent pour l'objectif
- **T**emporel: Délimité dans le temps

---

**Q3.** Quelle est la différence entre indicateur de stock et de flux?

**R3.**
| Stock | Flux |
|-------|------|
| Valeur à un instant T | Cumul sur une période |
| Ex: Solde des dépôts au 31/12 | Ex: Volume de dépôts en 2024 |
| Photo | Film |
| Bilan | Compte de résultat |

---

**Q4.** Comment calculer un indice simple (élémentaire)?

**R4.**
**Indice de prix:**
```
I_t/0 = (P_t / P_0) × 100

Exemple:
Prix 2020 (base): 100 HTG
Prix 2024: 125 HTG
I_2024 = (125 / 100) × 100 = 125
→ Augmentation de 25% depuis 2020
```

---

**Q5.** Comment calculer un taux de croissance?

**R5.**
```
Taux = (V_t - V_t-1) / V_t-1 × 100

Exemple:
Dépôts 2023: 10,000M HTG
Dépôts 2024: 11,500M HTG
Taux = (11,500 - 10,000) / 10,000 × 100 = 15%
```

---

**Q6.** Qu'est-ce que l'indice de Laspeyres?

**R6.**
**Indice de Laspeyres:** Pondéré par les quantités de la période de base.

```
L = Σ(P_t × Q_0) / Σ(P_0 × Q_0) × 100
```

**Caractéristique:** Surestime généralement l'inflation (effet substitution non pris en compte).

---

**Q7.** Qu'est-ce que l'indice de Paasche?

**R7.**
**Indice de Paasche:** Pondéré par les quantités de la période courante.

```
P = Σ(P_t × Q_t) / Σ(P_0 × Q_t) × 100
```

**Caractéristique:** Sous-estime généralement l'inflation.

---

**Q8.** Qu'est-ce que l'indice de Fisher?

**R8.**
**Indice de Fisher:** Moyenne géométrique de Laspeyres et Paasche.

```
F = √(L × P)
```

**Avantage:** Combine les propriétés des deux, considéré comme le meilleur compromis.

---

**Q9.** Comment calculer le ROE (Return on Equity) décomposé (DuPont)?

**R9.**
**Décomposition DuPont:**
```
ROE = Marge Nette × Rotation × Levier

ROE = (RN/CA) × (CA/Actifs) × (Actifs/CP)
    = RN/CP

Où:
- Marge nette = RN/CA
- Rotation des actifs = CA/Actifs
- Levier financier = Actifs/CP
```

---

**Q10.** Quels sont les principaux KPIs de profitabilité bancaire?

**R10.**
| KPI | Formule | Benchmark |
|-----|---------|-----------|
| **ROE** | RN / Capitaux Propres | 12-18% |
| **ROA** | RN / Total Actifs | 1-2% |
| **NIM** | Marge Intérêts / Actifs Productifs | 3-6% |
| **CIR** | Charges Exploit. / PNB | < 55% |

---

**Q11.** Quels sont les principaux KPIs de qualité d'actifs?

**R11.**
| KPI | Formule | Cible |
|-----|---------|-------|
| **NPL Ratio** | NPL / Total Prêts | < 5% |
| **Coverage Ratio** | Provisions / NPL | > 100% |
| **Cost of Risk** | Provisions Année / Encours Moyen | < 2% |
| **Write-off Ratio** | Passages en Perte / Encours | < 1% |

---

**Q12.** Comment interpréter le ratio de solvabilité (CAR)?

**R12.**
```
CAR = Fonds Propres Réglementaires / RWA × 100

Composantes:
- Tier 1: Capital de base (min 6%)
- Tier 2: Capital complémentaire
- Total: Min 8% (Bâle), souvent 12% (BRH)
```

**Interprétation:**
- CAR > 15%: Confortable
- 12-15%: Adéquat
- 8-12%: Attention
- < 8%: Non conforme

---

**Q13.** Comment construire un indice composite?

**R13.**
**Étapes:**
1. Sélectionner les composantes (variables)
2. Normaliser (Z-score ou min-max)
3. Déterminer les pondérations
4. Agréger (moyenne pondérée ou géométrique)

```python
# Exemple: Score de santé financière
def composite_score(df, weights):
    # Normalisation
    df_norm = (df - df.min()) / (df.max() - df.min())
    
    # Pondération
    score = sum(df_norm[col] * w for col, w in weights.items())
    return score

weights = {'roe': 0.3, 'npl': -0.3, 'car': 0.2, 'ldr': 0.2}
```

---

**Q14.** Quelle est la différence entre indicateurs leading et lagging?

**R14.**
| Leading (Avancés) | Lagging (Retardés) |
|-------------------|---------------------|
| Prédisent le futur | Confirment le passé |
| Ex: Nouvelles demandes | Ex: NPL réalisé |
| Ex: Confiance consommateurs | Ex: PIB |
| Utiles pour anticiper | Utiles pour valider |

---

**Q15.** Comment calculer le Customer Lifetime Value (CLV)?

**R15.**
**Formule simplifiée:**
```
CLV = ARPU × Durée × Marge

ARPU = Average Revenue Per User (mensuel ou annuel)
Durée = 1 / Churn Rate
Marge = Marge bénéficiaire

Exemple:
ARPU = 2,000 HTG/mois
Churn = 2%/mois → Durée = 50 mois
Marge = 30%
CLV = 2,000 × 50 × 0.30 = 30,000 HTG
```

---

**Q16.** Comment interpréter le ratio LDR (Loan-to-Deposit)?

**R16.**
```
LDR = Total Prêts / Total Dépôts × 100

Interprétation:
< 60%: Sous-utilisation des dépôts
60-80%: Zone optimale
80-100%: Utilisation agressive
> 100%: Dépendance au refinancement
```

---

**Q17.** Comment calculer le coût moyen des ressources?

**R17.**
```
Coût Ressources = Charges d'Intérêts / Ressources Moyennes × 100

Avec:
Ressources = Dépôts + Emprunts + Autres passifs porteurs d'intérêts
Moyennes = (Début + Fin) / 2

Exemple:
Charges intérêts: 300M HTG
Ressources moyennes: 8,000M HTG
Coût = 300 / 8,000 × 100 = 3.75%
```

---

**Q18.** Qu'est-ce que le spread bancaire?

**R18.**
```
Spread = Rendement Actifs - Coût Ressources

Exemple:
Rendement prêts: 12%
Coût dépôts: 4%
Spread = 12% - 4% = 8%
```

**Le spread finance:** frais généraux, provisions, impôts, profit.

---

**Q19.** Comment suivre l'évolution d'un indicateur avec une base mobile?

**R19.**
**Base mobile:** La période de référence change.

```
Indice base mobile = (V_t / V_t-1) × 100

Vs Base fixe:
Indice base fixe = (V_t / V_base) × 100

Conversion:
I_base_fixe_t = I_base_mobile_t × I_base_mobile_t-1 × ... × I_base_mobile_1
```

---

**Q20.** Créez un tableau de bord des KPIs essentiels pour le CEO.

**R20.**
```
┌─────────────────────────────────────────────────────────┐
│                    KPIs ESSENTIELS                      │
├─────────────────────────────────────────────────────────┤
│  PROFITABILITÉ        │  RISQUE                        │
│  ROE: 15% (↑ vs 14%)  │  NPL: 4.2% (↑ vs 3.8%)        │
│  ROA: 1.5%            │  Coverage: 85%                 │
│  NIM: 6.2%            │  CAR: 14%                      │
│  CIR: 52%             │  LDR: 75%                      │
├─────────────────────────────────────────────────────────┤
│  CROISSANCE           │  CLIENTS                       │
│  Dépôts: +8% YoY      │  Clients: +3%                  │
│  Prêts: +5% YoY       │  NPS: 42                       │
│  PNB: +10% YoY        │  Churn: 1.5%                   │
└─────────────────────────────────────────────────────────┘
```

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-8 | À améliorer |
| 9-13 | Intermédiaire |
| 14-17 | Avancé |
| 18-20 | Expert |
