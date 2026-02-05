# Test Business Intelligence - Test 2

**Sujet:** BI et Métriques Bancaires  
**Niveau:** Intermédiaire  
**Nombre de questions:** 20

---

## Questions et Réponses

**Q1.** Quelle est la différence entre un rapport et un dashboard?

**R1.**
| Rapport | Dashboard |
|---------|-----------|
| Détaillé | Synthétique |
| Statique | Interactif |
| Historique | Temps réel/actuel |
| Analyse en profondeur | Vue d'ensemble |
| Format: PDF, Excel | Format: Web, BI tool |

---

**Q2.** Comment calculer le Loan-to-Value (LTV) ratio?

**R2.**
```
LTV = Montant du Prêt / Valeur de la Garantie × 100

Exemple:
Prêt immobilier: 8,000,000 HTG
Valeur maison: 10,000,000 HTG
LTV = 8,000,000 / 10,000,000 × 100 = 80%
```

**Seuils:**
- LTV < 70%: Faible risque
- 70% < LTV < 90%: Risque modéré
- LTV > 90%: Risque élevé

---

**Q3.** Qu'est-ce que le Debt-to-Income (DTI) ratio?

**R3.**
```
DTI = Total Dettes Mensuelles / Revenu Mensuel × 100

Exemple:
Remboursement prêt: 30,000 HTG
Autres dettes: 10,000 HTG
Revenu: 100,000 HTG
DTI = 40,000 / 100,000 × 100 = 40%
```

**Seuils recommandés:**
- DTI < 35%: Acceptable
- 35% < DTI < 43%: Limite
- DTI > 43%: Risqué

---

**Q4.** Comment mesurer la productivité des agences?

**R4.**
```
Productivité = Production / Ressources

Métriques:
- Volume prêts / Employé
- Nb nouveaux comptes / Employé
- PNB / Employé
- Nb transactions / Guichet
```

---

**Q5.** Qu'est-ce que le Net Promoter Score (NPS)?

**R5.**
```
NPS = % Promoteurs - % Détracteurs

Sur échelle 0-10:
- Promoteurs: 9-10
- Passifs: 7-8
- Détracteurs: 0-6
```

**Interprétation:**
- NPS > 50: Excellent
- NPS 30-50: Bon
- NPS 0-30: À améliorer
- NPS < 0: Problème

---

**Q6.** Comment calculer le taux d'attrition (churn)?

**R6.**
```
Churn = Clients Perdus / Clients Début Période × 100

Exemple mensuel:
Clients janvier: 10,000
Clients fermés en janvier: 150
Churn = 150 / 10,000 × 100 = 1.5%
```

---

**Q7.** Qu'est-ce que le PNB (Produit Net Bancaire)?

**R7.**
```
PNB = Revenus d'Exploitation - Charges d'Exploitation Bancaires

Composantes:
+ Marge d'intérêt (revenus int. - charges int.)
+ Commissions nettes
+ Gains sur opérations de marché
- Charges financières
```

---

**Q8.** Comment analyser la migration des clients entre segments?

**R8.**
```sql
-- Matrice de migration
WITH migration AS (
    SELECT 
        c1.segment as segment_avant,
        c2.segment as segment_apres,
        COUNT(*) as nb_clients
    FROM clients_t1 c1
    JOIN clients_t2 c2 ON c1.client_id = c2.client_id
    GROUP BY c1.segment, c2.segment
)
SELECT * FROM migration;
```

**Visualisation:** Heatmap ou Sankey diagram

---

**Q9.** Quels KPIs pour mesurer la digitalisation bancaire?

**R9.**
- **Adoption:** % clients avec app mobile
- **Engagement:** Connexions / mois / client
- **Transactions:** % transactions digitales vs agence
- **Acquisition:** % ouvertures de compte en ligne
- **Coût:** Coût par transaction digitale vs physique

---

**Q10.** Comment calculer le coût d'acquisition client (CAC)?

**R10.**
```
CAC = Total Dépenses Marketing & Ventes / Nombre de Nouveaux Clients

Exemple:
Dépenses Q1: 5,000,000 HTG
Nouveaux clients Q1: 500
CAC = 5,000,000 / 500 = 10,000 HTG/client
```

**Benchmark:** CAC < CLV/3 généralement acceptable

---

**Q11.** Comment mesurer l'efficacité des campagnes marketing?

**R11.**
```
Métriques:
- Taux de réponse = Réponses / Contacts × 100
- Taux de conversion = Ventes / Leads × 100
- ROI = (Revenus - Coûts) / Coûts × 100
- CPL (Cost per Lead) = Coûts / Leads
```

---

**Q12.** Qu'est-ce que l'analyse des écarts (variance analysis)?

**R12.**
```
Écart = Réel - Budget

Analyse par composante:
- Écart de volume: (Qté réelle - Qté budget) × Prix budget
- Écart de prix: (Prix réel - Prix budget) × Qté réelle

Application bancaire:
- Écart sur marge d'intérêt
- Écart sur volume de dépôts
- Écart sur coûts opérationnels
```

---

**Q13.** Comment structurer un rapport de risque mensuel?

**R13.**
```
1. RÉSUMÉ EXÉCUTIF
   - KPIs clés (NPL, Coverage, CAR)
   - Alertes principales

2. QUALITÉ DU PORTEFEUILLE
   - NPL par segment/secteur
   - Migration des buckets
   - Vintage analysis

3. CONCENTRATION
   - Top expositions
   - Par secteur/région

4. PROVISIONS
   - Stock et flux
   - Coverage ratio

5. STRESS TESTS
   - Scénarios et impacts

6. RECOMMANDATIONS
```

---

**Q14.** Comment créer un scorecard équilibré (balanced scorecard)?

**R14.**
```
4 perspectives:
1. FINANCIÈRE: ROE, PNB, CIR
2. CLIENTS: NPS, Churn, CAC
3. PROCESSUS: Temps de traitement, Taux d'erreur
4. APPRENTISSAGE: Formation, Innovation, Turnover

Chaque perspective:
- Objectifs stratégiques
- KPIs
- Cibles
- Initiatives
```

---

**Q15.** Quels sont les indicateurs de liquidité règlementaires?

**R15.**
```
LCR (Liquidity Coverage Ratio):
LCR = Stock Actifs Liquides / Sorties Nettes 30j ≥ 100%

NSFR (Net Stable Funding Ratio):
NSFR = Financement Stable Disponible / Financement Stable Requis ≥ 100%
```

---

**Q16-20.** [Questions sur le reporting BRH, l'analyse multi-devises, et les dashboards opérationnels...]

---

## Scoring

| Score | Niveau |
|-------|--------|
| 0-8 | À améliorer |
| 9-13 | Intermédiaire |
| 14-17 | Avancé |
| 18-20 | Expert |
